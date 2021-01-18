# stdlib
from typing import Any
from typing import Callable as CallableT
from typing import Optional
from typing import Union

# syft relative
from .. import ast
from .. import lib
from ..core.node.common.action.get_or_set_static_attribute_action import (
    GetSetStaticAttributeAction,
)
from ..core.node.common.action.get_or_set_static_attribute_action import (
    StaticAttributeAction,
)


class StaticAttribute(ast.attribute.Attribute):
    """A method, function, or constructor which can be directly executed"""

    def __init__(
        self,
        parent: ast.attribute.Attribute,
        path_and_name: Optional[str] = None,
        return_type_name: Optional[str] = None,
        client: Optional[Any] = None,
    ):
        self.parent = parent
        super().__init__(
            path_and_name=path_and_name,
            return_type_name=return_type_name,
            client=client,
        )

    def get_remote_value(self):
        if self.path_and_name is None:
            raise ValueError("MAKE PROPER SCHEMA - Can't get static_attribute")

        return_tensor_type_pointer_type = self.client.lib_ast.query(
            path=self.return_type_name
        ).pointer_type

        ptr = return_tensor_type_pointer_type(client=self.client)

        msg = GetSetStaticAttributeAction(
            path=self.path_and_name,
            id_at_location=ptr.id_at_location,
            address=self.client.address,
            action=StaticAttributeAction.GET,
        )
        self.client.send_immediate_msg_without_reply(msg=msg)
        return ptr

    def solve_get_value(self):
        return getattr(self.parent.object_ref, self.path_and_name.rsplit(".")[-1])

    def solve_set_value(self, set_value):
        setattr(self.parent.object_ref, self.path_and_name.rsplit(".")[-1], set_value)

    def set_remote_value(self, set_arg: Any):
        resolved_pointer_type = self.client.lib_ast.query(self.return_type_name)
        result = resolved_pointer_type.pointer_type(client=self.client)
        result_id_at_location = getattr(result, "id_at_location", None)

        downcasted_set_arg = lib.python.util.downcast(set_arg)
        downcasted_set_arg_ptr = downcasted_set_arg.send(self.client)

        cmd = GetSetStaticAttributeAction(
            path=self.path_and_name,
            id_at_location=result_id_at_location,
            address=self.client.address,
            action=StaticAttributeAction.SET,
            set_arg=downcasted_set_arg_ptr,
        )
        self.client.send_immediate_msg_without_reply(msg=cmd)
        return result

    def __call__(
        self, action: StaticAttributeAction
    ) -> Optional[Union["Callable", CallableT]]:
        raise ValueError("MAKE PROPER SCHEMA, THIS SHOULD NEVER BE CALLED")

    def add_path(self, *args, **kwargs):
        raise ValueError("MAKE PROPER SCHEMA")