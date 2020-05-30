import os

ENV_FILE = ".env"


def get_settings(file):
    __settings = {}
    with open(file, encoding="utf-8") as f:
        for row in f:
            # 先頭が#の場合コメントなので無視、=のない行も無視する
            if row.startswith("#") or "=" not in row:
                continue
            columns = row.strip().split("=")
            # key=value形式になっていること
            assert len(columns) == 2, "file format is not key=value"

            # キーのセット
            key, value = columns
            assert key not in __settings, "duplicated keys"
            __settings[key] = value

    return __settings


class Settings:

    def __init__(self, file=ENV_FILE):
        # 設定の取得
        # __settings = get_settings(file)

        # 初期化
        self.db_engine = os.getenv("DB_ENGINE")
        self.db_port = os.getenv("DB_PORT")
        self.db_host = os.getenv("DB_HOST")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_name = os.getenv("DB_NAME")
        self.aws_user_access_key = os.getenv("AWS_USER_ACCESS_KEY")
        self.aws_user_secret_key = os.getenv("AWS_USER_SECRET_KEY")
        self.env = os.getenv("ENV")
        self.tmdb_url = os.getenv("TMDB_URL")
        self.tmdb_api_key = os.getenv("TMDB_API_KEY")
        self.bucket_name = os.getenv("BUCKET_NAME")


settings = Settings()
