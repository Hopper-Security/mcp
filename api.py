import requests

from config import API_URL, JWT


def _call_api(path: str, payload: dict = None, method: str = "POST"):
    headers = {"Authorization": f"Bearer {JWT}"}
    url = f"{API_URL}/{path.lstrip('/')}"
    request_func = requests.post if method.upper() == "POST" else requests.get
    kwargs = {"headers": headers, "timeout": 90}

    if method.upper() == "POST":
        kwargs["json"] = payload or {}
    else:
        kwargs["params"] = payload or {}

    resp = request_func(url, **kwargs)
    resp.raise_for_status()
    return resp.json()


def api_post(path: str, payload: dict = None):
    return _call_api(path, payload, method="POST")


def api_get(path: str, payload: dict = None):
    return _call_api(path, payload, method="GET")
