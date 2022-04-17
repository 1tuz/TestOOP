import requests
import pytest


class TestEasyAPI:
    r = requests.get("https://github.com/1tuz/TestOOP")
    if r.status_code == 200:
        print(r.status_code, "Ok")
    else:
        print("Warning! Response status code = ", r.status_code)

    w = requests.get("https://github.com/1tuz/TestOOP/11111")
    if w.status_code == 200:
        print(w.status_code, "OK")
    else:
        print("Warning! Response status code = ", w.status_code)

    def test_github_assertion(self):
        y = requests.get("https://github.com/1tuz/TestOOP/11111")
        assert y.status_code == 200
