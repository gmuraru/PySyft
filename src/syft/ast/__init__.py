# stdlib
from typing import Any as TypeAny
from typing import List as TypeList
from typing import Tuple as TypeTuple
from typing import Union

# syft relative
from . import attribute  # noqa: F401
from . import callable  # noqa: F401
from . import enum  # noqa: F401
from . import globals  # noqa: F401
from . import klass  # noqa: F401
from . import module  # noqa: F401
from . import property  # noqa: F401
from . import static_attr  # noqa: F401


def get_parent(path: str, root: globals.Globals) -> module.Module:
    parent = root
    for step in path.split(".")[:-1]:
        if step in parent.attrs:
            parent = parent.attrs[step]
    return parent


def add_modules(
    ast: globals.Globals,
    modules: Union[TypeList[str], TypeList[TypeTuple[str, TypeAny]]],
) -> None:
    for mod in modules:
        # We also have the reference
        if isinstance(mod, tuple):
            target_module, ref = mod
        else:
            target_module = mod
        parent = get_parent(target_module, ast)
        attr_name = target_module.rsplit(".", 1)[-1]
        parent.add_attr(
            attr_name=attr_name,
            attr=module.Module(
                path_and_name=target_module,
                object_ref=None,
                return_type_name="",
                client=ast.client,
            ),
        )


def add_classes(
    ast: globals.Globals,
    paths: TypeList[TypeTuple[str, str, TypeAny]],
) -> None:
    for path, return_type, ref in paths:
        parent = get_parent(path, ast)
        attr_name = path.rsplit(".", 1)[-1]
        parent.add_attr(
            attr_name=attr_name,
            attr=klass.Class(
                path_and_name=path,
                object_ref=ref,
                return_type_name=return_type,
                client=ast.client,
            ),
        )


def add_methods(
    ast: globals.Globals,
    paths: TypeList[TypeTuple[str, str]],
) -> None:
    for path, return_type in paths:
        parent = get_parent(path, ast)
        path_list = path.split(".")
        parent.add_path(
            path=path_list,
            index=len(path_list) - 1,
            return_type_name=return_type,
        )
