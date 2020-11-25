# stdlib
import operator

# third party
import pytest
from sympc.session import Session
from sympc.tensor import AdditiveSharingTensor
from sympc.tensor import FixedPrecisionTensor
import torch

# syft absolute
import syft as sy

TEST_VALUES = [
    (4, -5),
    (torch.tensor([42, -32, 12]), 20),
    (25, torch.tensor([32, 12, -5])),
    (torch.tensor([15, 2353, 23, -50]), torch.tensor([123, 43, 23, -5])),
    (4.512312, torch.tensor([123.123, 5123.321, 123.32])),
]


def test_ast_exception_share() -> None:
    alice = sy.VirtualMachine(name="alice")
    bob = sy.VirtualMachine(name="bob")

    alice_client = alice.get_client()
    bob_client = bob.get_client()

    session = Session(parties=[alice_client, bob_client])

    with pytest.raises(ValueError):
        AdditiveSharingTensor(secret=42, session=session)


@pytest.mark.parametrize("private", [False])
@pytest.mark.parametrize("operation", ["add"])
def test_ast_operation(private: bool, operation: str) -> None:
    alice = sy.VirtualMachine(name="alice")
    bob = sy.VirtualMachine(name="bob")

    alice_client = alice.get_client()
    bob_client = bob.get_client()

    session = Session(parties=[alice_client, bob_client])
    Session.setup_mpc(session)

    for x_secret, y_secret in TEST_VALUES:
        if not isinstance(x_secret, torch.Tensor):
            x_tensor_secret = torch.Tensor([x_secret])
        else:
            x_tensor_secret = x_secret

        shape = x_tensor_secret.shape
        x_tensor_secret = x_tensor_secret.send(alice_client)
        x = AdditiveSharingTensor(secret=x_tensor_secret, shape=shape, session=session)

        if private:
            if not isinstance(y_secret, torch.Tensor):
                y_fpt_secret = FixedPrecisionTensor(data=torch.Tensor([y_secret]))

            shape = y_fpt_secret.shape
            y = AdditiveSharingTensor(secret=y_fpt_secret, shape=shape, session=session)
        else:
            y = y_secret

        op = getattr(operator, operation)
        res = op(x, y)
        res_expected = op(x_secret, y_secret)

        if not isinstance(res_expected, torch.Tensor):
            res_expected = torch.tensor([res_expected])

        res_expected = res_expected.float()

        assert torch.allclose(
            res.reconstruct(), res_expected
        ), f"Fail for {x_secret} and {y_secret}"