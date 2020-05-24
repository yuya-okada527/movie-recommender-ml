import sys

from . import batch
from .logger import create_logger


log = create_logger(__name__)

JOBS = {
    "setup": batch.setup,
    "movie-ids": batch.fetch_all_movie_ids
}


def main(batch_name):
    log.info("JOB Started")
    job = JOBS[batch_name]
    log.info("Requested JOB is %s", batch_name)
    job()
    log.info("JOB Finished")


if __name__ == "__main__":
    assert len(sys.argv) == 2, "number of arguments must be 2"
    main(sys.argv[1])
