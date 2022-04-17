import requests
import pytest


class EasyAPI:
    r = requests.get("https://yandex.ru/")
    if r.status_code == 200:
        print(r.status_code, "Ok")
    else:
        print("Warning! Response status code = ", r.status_code)

    w = requests.get("https://yandex.ru/testtt")
    if w.status_code == 200:
        print(w.status_code, "OK")
    else:
        print("Warning! Response status code = ", w.status_code)
