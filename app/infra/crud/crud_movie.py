from ..database import engine

# データ挿入
INSERT_MOVIE_SQL = "INSERT INTO movie VALUES (%s, %s)"

# 全件取得
ALL_MOVIES = "SELECT * FROM movie"


def make_movie(movie_id, tmdb_id):
    with engine.connect() as connection:
        connection.execute(INSERT_MOVIE_SQL, [movie_id, tmdb_id])


def find_all_movies():
    with engine.connect() as connection:
        return connection.execute(ALL_MOVIES)
