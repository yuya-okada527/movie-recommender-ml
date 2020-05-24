from .infra.crud.setup import create_table
from .infra.crud.crud_movie import find_all_movies
from .logger import create_logger

log = create_logger(__name__)


def setup():
    log.info("DB setup started")
    create_table()
    log.info("DB setup finished")


def fetch_all_movie_ids():
    log.info("fetching all movie ids")
    movies = find_all_movies()
    log.info("fetched all movie ids")
    return [movie["tmdb_id"] for movie in movies]
