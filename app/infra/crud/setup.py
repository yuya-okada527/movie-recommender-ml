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


def create_table():
    with engine.connect() as connection:
        # テーブルの削除
        connection.execute(DROP_TABLE_SQL)

        # テーブルの作成
        connection.execute(CREATE_TABLE_SQL)

        # サンプルデータの作成
        for i in range(10):
            make_movie(f"{i}", f"{i}")
