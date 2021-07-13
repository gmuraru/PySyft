# stdlib
import sys

# third party
import numpy as np
import pytest
import torch

# syft absolute
import syft as sy
from syft import logger
from syft.core.tensor.smpc.mpc_tensor import MPCTensor
from syft.core.tensor.smpc.share_tensor import ShareTensor
from syft.core.tensor.tensor import Tensor

vms = [sy.VirtualMachine(name=name) for name in ["alice", "bob", "theo", "andrew"]]
clients = [vm.get_client() for vm in vms]


def test_remote_sharing():
    value = np.array([[1, 2, 3, 4, -5]], dtype=np.int64)
    remote_value = clients[0].syft.core.tensor.tensor.Tensor(value)

    mpc_tensor = MPCTensor(
        parties=clients, secret=remote_value, shape=(1, 5), seed_shares=52
    )

    assert len(mpc_tensor.child) == len(clients)

    shares = [share.get_copy() for share in mpc_tensor.child]
    assert all([isinstance(share, ShareTensor) for share in shares])
    assert (mpc_tensor.reconstruct() == value).all()


@pytest.mark.parametrize("op_str", ["add", "sub"])
def test_mpc_private_op(op_str):
    value_1 = np.array([[1, 2, 3, 4, -5]], dtype=np.int64)
    value_2 = np.array([10], dtype=np.int64)

    remote_value_1 = clients[0].syft.core.tensor.tensor.Tensor(value)
    remote_value_2 = clients[4].syft.core.tensor.tensor.Tensor(value)

    mpc_tensor_1 = MPCTensor(
        parties=clients, secret=remote_value_1, shape=(1, 5), seed_shares=52
    )

    mpc_tensor_2 = MPCTensor(
        parties=clients, secret=remote_value_2, shape=(1,), seed_shares=42
    )

    op = getattr(operator, op_str)

    res = op(mpc_tensor_1, mpc_tensor_1)
    expected = op(value_1, value_2)

    assert (res == expected).all()
