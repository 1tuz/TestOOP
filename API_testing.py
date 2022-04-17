import requests
import pytest


response = requests.get("https://yandex.ru/")

print(response.text)
