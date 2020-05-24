from .infra.crud.setup import create_table
from .logger import create_logger

log = create_logger(__name__)


def setup():
    log.info("DB setup started")
    create_table()
    log.info("DB setup finished")
