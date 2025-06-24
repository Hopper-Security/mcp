from enum import Enum

import requests

from src.config import API_URL, JWT


class HTTPMethod(Enum):
    GET = "GET"
    POST = "POST"


def _call_api(path: str, payload: dict | None = None, method: HTTPMethod = HTTPMethod.POST):
    headers = {"Authorization": f"Bearer {JWT}"}
    url = f"{API_URL}/{path.lstrip('/')}"

    request_func = requests.post if method == HTTPMethod.POST else requests.get

    kwargs: dict = {"headers": headers, "timeout": 90}

    if method == HTTPMethod.POST:
        kwargs["json"] = payload or {}
    else:
        kwargs["params"] = payload or {}

    resp = request_func(url, **kwargs)
    resp.raise_for_status()
    return resp.json()


def api_post(path: str, payload: dict | None = None):
    return _call_api(path, payload, method=HTTPMethod.POST)


def api_get(path: str, payload: dict | None = None):
    return _call_api(path, payload, method=HTTPMethod.GET)
