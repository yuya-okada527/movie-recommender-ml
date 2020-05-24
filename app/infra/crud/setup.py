from ..database import engine
from .crud_movie import make_movie

# テーブル削除SQL
DROP_TABLE_SQL = "DROP TABLE IF EXISTS movie"

# テーブル作成SQL
CREATE_TABLE_SQL = """\
CREATE TABLE IF NOT EXISTS movie(
    movie_id    varchar(8),
    tmdb_id     varchar(8)
)
"""

MOVIES = [
    "807",   # Se7en
    "550",   # Fight Club
    "274",   # The Silence of the Lambs
    "1893",  # Star Wars Episode 1
    "1894",  # Star Wars Episode 2
    "862",   # Toy Story
    "863",   # Toy Story2
    "105",   # Back to the Future
    "12",    # Finding Nemo
    "128"
]


def create_table():
    with engine.connect() as connection:
        # テーブルの削除
        connection.execute(DROP_TABLE_SQL)

        # テーブルの作成
        connection.execute(CREATE_TABLE_SQL)


def create_data():
    # サンプルデータの作成
    for i in range(10):
        make_movie(f"{i}", f"{MOVIES[i]}")
