from .infra.crud.setup import create_table, create_data
from .infra.crud.crud_movie import find_all_movies
from .infra.client import call_api
from .logger import create_logger
from .config import settings

log = create_logger(__name__)


def setup():
    log.info("Creating Table")
    create_table()
    log.info("Created Table")
    log.info("Creating data")
    create_data()
    log.info("Creating data")


def fetch_all_movie_ids():
    log.info("fetching all movie ids")
    movies = find_all_movies()
    log.info("fetched all movie ids")
    return [movie["tmdb_id"] for movie in movies]


def fetch_overviews():
    movie_ids = fetch_all_movie_ids()
    base_url = settings.tmdb_url
    params = {
        "api_key": settings.tmdb_api_key,
        "lang": "ja"
    }

    for movie_id in movie_ids:
        url = base_url + movie_id
        movie = call_api(url, params)
