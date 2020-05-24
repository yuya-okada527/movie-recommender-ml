from .infra.crud.setup import create_table, create_data
from .infra.crud.crud_movie import find_all_movies
from .infra.client import call_api
from .infra.s3 import put_object
from .logger import create_logger
from .config import settings
from .data import Movie

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
    return [(movie["movie_id"], movie["tmdb_id"]) for movie in movies]


def fetch_movies():
    movie_ids = fetch_all_movie_ids()
    base_url = settings.tmdb_url
    params = {
        "api_key": settings.tmdb_api_key,
        "lang": "ja"
    }
    movies = []

    log.info("Fetching movie data from TMDb API")
    for movie_id, tmdb_id in movie_ids:
        url = base_url + tmdb_id
        movie = call_api(url, params)
        movies.append(Movie(
            movie_id=movie_id,
            tmdb_id=tmdb_id,
            overview=movie["overview"]
        ))
    log.info("Data Fetched")
    return movies


def make_body():
    log.info("Makeing file data")
    movies = fetch_movies()
    body = "movie_id\toverview\n"
    for movie in movies:
        overview = movie.overview.replace("\t", "")[:512]
        body += "\t".join([movie.movie_id, overview]) + "\n"
    log.info("File data Made")
    return body


def upload():
    body = make_body()
    key = "data/movies.tsv"
    log.info("Uploading to S3")
    put_object(key, body)
    log.info("Upload finished")
