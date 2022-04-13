import requests
from bs4 import BeautifulSoup


def get_url(path: str, port=8000):
    return f"https://www.ss.com/ru/transport/cars/{path}"
