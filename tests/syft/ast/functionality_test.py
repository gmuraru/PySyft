"""
The following test suit serves as a set of examples of how to integrate different classes
into our AST and use them.
"""
# stdlib
from importlib import reload

# syft absolute
import syft
from syft.ast.globals import Globals
from syft.core.node.common.client import Client
from syft.lib import create_lib_ast
from syft.lib import registered_callbacks

# syft relative
from . import test_module


def create_AST(client: Client) -> Globals:
    ast = Globals(client)

    methods = [
        ("test_module.A", "test_module.A"),
        ("test_module.A.test_method", "syft.lib.python.Int"),
        ("test_module.A.test_property", "syft.lib.python.Float"),
        ("test_module.A._private_attr", "syft.lib.python.Float"),
        ("test_module.A.static_method", "syft.lib.python.Float"),
        ("test_module.A.static_attr", "syft.lib.python.Int"),
        ("test_module.B.Car", "test_module.B"),
        ("test_module.global_value", "syft.lib.python.Int"),
        ("test_module.global_function", "syft.lib.python.Int"),
    ]

    for method, return_type in methods:
        ast.add_path(
            path=method, framework_reference=test_module, return_type_name=return_type
        )

    for klass in ast.classes:
        klass.create_pointer_class()
        klass.create_send_method()
        klass.create_serialization_methods()
        klass.create_storable_object_attr_convenience_methods()

    return ast


def get_custom_client() -> Client:
    registered_callbacks["test_module"] = create_AST
    syft.lib_ast = create_lib_ast(None)
    alice = syft.VirtualMachine(name="alice")
    alice_client = alice.get_root_client()
    return alice_client


def test_method() -> None:
    client = get_custom_client()
    a_ptr = client.test_module.A()
    result_ptr = a_ptr.test_method()

    a = test_module.A()
    result = a.test_method()

    assert result == result_ptr.get()


def test_property_get() -> None:
    client = get_custom_client()
    a_ptr = client.test_module.A()
    result_ptr = a_ptr.test_property

    a = test_module.A()
    result = a.test_property

    assert result == result_ptr.get()


def test_property_set() -> None:
    value_to_set = 7.5
    client = get_custom_client()

    a_ptr = client.test_module.A()
    a_ptr.test_property = value_to_set
    result_ptr = a_ptr.test_property  # type: ignore

    a = test_module.A()
    a.test_property = value_to_set
    result = a.test_property

    assert result == result_ptr.get()


def test_slot_get() -> None:
    client = get_custom_client()

    a_ptr = client.test_module.A()
    result_ptr = a_ptr._private_attr

    a = test_module.A()
    result = a._private_attr

    assert result == result_ptr.get()


def test_slot_set() -> None:
    value_to_set = 7.5
    client = get_custom_client()

    a_ptr = client.test_module.A()
    a_ptr._private_attr = value_to_set
    result_ptr = a_ptr._private_attr

    a = test_module.A()
    a._private_attr = value_to_set
    result = a._private_attr

    assert result == result_ptr.get()  # type: ignore


def test_global_function() -> None:
    client = get_custom_client()

    result_ptr = client.test_module.global_function()
    result = test_module.global_function()

    assert result == result_ptr.get()  # type: ignore


def test_global_attribute_get() -> None:
    client = get_custom_client()

    result_ptr = client.test_module.global_value
    result = test_module.global_value

    assert result == result_ptr.get()  # type: ignore


def test_global_attribute_set() -> None:
    global test_module

    set_value = 5
    client = get_custom_client()

    client.test_module.global_value = set_value
    result_ptr = client.test_module.global_value
    sy_result = result_ptr.get()  # type: ignore

    test_module = reload(test_module)
    test_module.set_value = set_value
    local_result = test_module.global_value

    assert local_result == sy_result


def test_static_method() -> None:
    client = get_custom_client()

    result_ptr = client.test_module.A.static_method()
    result = test_module.A.static_method()
    assert result == result_ptr.get()  # type: ignore


def test_static_attribute_get() -> None:
    client = get_custom_client()

    result_ptr = client.test_module.A.static_attr
    result = test_module.A.static_attr

    assert result == result_ptr.get()  # type: ignore


def test_static_attribute_set() -> None:
    value_to_set = 5
    client = get_custom_client()

    client.test_module.A.static_attr = value_to_set
    result_ptr = client.test_module.A.static_attr

    test_module.A.static_attr = value_to_set
    result = test_module.A.static_attr

    assert result == result_ptr.get()  # type: ignore


def test_enum() -> None:
    client = get_custom_client()

    result_ptr = client.test_module.B.Car
    result = test_module.B.Car

    assert result == result_ptr.get()  # type: ignore
