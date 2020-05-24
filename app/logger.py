import logging

from .config import settings


def create_logger(name):
    # ログの設定
    log = logging.getLogger(name)
    if settings.env == "local":
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)

    # 標準出力へのハンドラを設定
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s;%(name)s;%(levelname)s; %(message)s")
    handler.setFormatter(formatter)
    log.addHandler(handler)

    return log
