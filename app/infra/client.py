import requests

from ..logger import create_logger


log = create_logger(__name__)


def call_api(url, params):
    log.info(f"Calling API(url={url})")
    response = requests.get(url, params=params)

    if response.status_code != 200:
        log.error(f"Error Occurred when calling API (code={response.status_code}, reason={response.reason})")

    log.info(f"Called API")
    return response.json()
