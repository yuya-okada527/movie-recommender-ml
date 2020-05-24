from ..database import engine

# データ挿入
INSERT_MOVIE_SQL = "INSERT INTO movie VALUES (%s, %s)"


def insert(movie_id, tmdb_id):
    with engine.connect() as connection:
        connection.execute(INSERT_MOVIE_SQL, [movie_id, tmdb_id])
