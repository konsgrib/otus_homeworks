from ftplib import all_errors
import requests
from bs4 import BeautifulSoup


def get_url(path: str, port=8000):
    return f"https://www.ss.com/ru/transport/cars/{path}"


def get_root():
    path = "/"
    url = get_url(path)
    response = requests.get(url)
    print(response)
    print(response.status_code)
    return response


def get_main_links(save_to_file=False):
    response = get_root()
    soup = BeautifulSoup(response.text, "html.parser")
    all_links = soup.find_all("a", {"class": "a_category"})
    if not save_to_file:
        for link in all_links:
            print(link)
        return all_links

    with open("links.txt", "w", encoding="utf-8") as f:
        for link in all_links:
            f.write(f"{link}\n")
        return all_links


if __name__ == "__main__":
    get_main_links()
