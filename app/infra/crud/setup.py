from ..database import engine
from .crud_movie import insert

# テーブル削除SQL
DROP_TABLE_SQL = "DROP IF EXISTS movie"

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
            insert(f"{i}", f"{i}")
