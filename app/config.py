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
        __settings = get_settings(file)

        # 初期化
        self.db_engine = __settings["DB_ENGINE"]
        self.db_port = __settings["DB_PORT"]
        self.db_host = __settings["DB_HOST"]
        self.db_user = __settings["DB_USER"]
        self.db_password = __settings["DB_PASSWORD"]
        self.db_name = __settings["DB_NAME"]
        self.aws_user_access_key = __settings["AWS_USER_ACCESS_KEY"]
        self.aws_user_secret_key = __settings["AWS_USER_SECRET_KEY"]
        self.env = __settings["ENV"]
        self.tmdb_url = __settings["TMDB_URL"]
        self.tmdb_api_key = __settings["TMDB_API_KEY"]
        self.bucket_name = __settings["BUCKET_NAME"]


settings = Settings()
