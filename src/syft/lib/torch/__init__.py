# stdlib
from typing import Dict
from typing import Union

# third party
from packaging import version
import torch

# syft relative
from . import parameter  # noqa: 401
from . import uppercase_tensor  # noqa: 401
from ...ast.globals import Globals
from .allowlist import allowlist
from .allowlist import fallback

TORCH_VERSION = version.parse(torch.__version__.split("+")[0])


def get_return_type(support_dict: Union[str, Dict[str, str]]) -> str:
    if isinstance(support_dict, str):
        return support_dict
    else:
        return support_dict["return_type"]


def version_supported(support_dict: Union[str, Dict[str, str]]) -> bool:
    if isinstance(support_dict, str):
        return True
    else:
        # if we are on either side of the min or max versions we don't support this op
        if "min_version" in support_dict and TORCH_VERSION < version.parse(
            support_dict["min_version"]
        ):
            return False
        if "max_version" in support_dict and TORCH_VERSION > version.parse(
            support_dict["max_version"]
        ):
            return False
        return True


def create_torch_ast(client=None) -> Globals:
    ast = Globals(client)

    # most methods work in all versions and have a single return type
    # for the more complicated ones we pass a dict with keys like return_type and
    # min_version
    for method, return_type_name_or_dict in allowlist.items():
        if version_supported(support_dict=return_type_name_or_dict):
            return_type = get_return_type(support_dict=return_type_name_or_dict)
            if return_type == "unknown":
                # this allows us to import them for testing
                continue
            ast.add_path(
                path=method, framework_reference=torch, return_type_name=return_type
            )
            # add all the torch.nn.Parameter hooks
            if method.startswith("torch.Tensor."):
                method = method.replace("torch.Tensor.", "torch.nn.Parameter.")
                return_type = return_type.replace("torch.Tensor", "torch.nn.Parameter")
                ast.add_path(
                    path=method, framework_reference=torch, return_type_name=return_type
                )
        else:
            pass
            # TODO: Replace with logging
            # print(f"Skipping {method} not supported in {TORCH_VERSION}")

    for method, location in fallback.items():
        target_node = ast.query(location)
        prefix_path = ".".join(method.split(".")[:-1])
        name = method.split(".")[-1]

        ast.add_path(
            path=prefix_path,
            framework_reference=torch,
        )

        end_node = ast.query(prefix_path)
        end_node.attrs[name] = target_node

    for klass in ast.classes:
        klass.create_pointer_class()
        klass.create_send_method()
        klass.create_serialization_methods()
        klass.create_storable_object_attr_convenience_methods()
    return ast
