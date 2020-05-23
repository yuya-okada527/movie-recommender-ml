import sys

from . import batch

BATCH = {
    "setup": batch.setup
}


def main(batch_name):
    job = BATCH[batch_name]
    job()


if __name__ == "__main__":
    assert len(sys.argv) == 2, "number of arguments must be 2"
    main(sys.argv[1])
