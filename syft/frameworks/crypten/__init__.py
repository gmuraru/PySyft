import crypten
import crypten.communicator as comm
import syft
from syft.frameworks.crypten.context import run_party


def load(tag: str, src: int = 0, **kwargs):
    """Load an object tagged with 'tag' located at the syft worker running
    party with rank 'src'.

    Args:
        tag: tag of the object to be looked up.
        src: rank of the party that should attempt to fetch the object.
    """

    if src == comm.get().get_rank():
    if src == comm.get().get_rank():
        worker = syft.local_worker.get_worker_from_rank(src)
        results = worker.search(tag)

        # Make sure there is only one result
        assert len(results) == 1

        result = results[0].get()
        result = crypten.load(preloaded=result, src=src, **kwargs)

    else:
        result = crypten.load(src=src, **kwargs)

    return result


__all__ = ["run_party", "load", "get_plain_text"]
