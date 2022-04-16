from ftplib import all_errors
import requests
from bs4 import BeautifulSoup

SAVE_TO_FILE = False


def get_url(path: str):
    return f"https://www.ss.com/ru/transport/cars{path}"


def get_root():
    path = "/"
    url = get_url(path)
    response = requests.get(url)
    return response


def get_last_part_path(path):
    new_path = path.split("/")[-2]
    return f"/{new_path}/"


def get_links(save_to_file=False):
    response = get_root()
    soup = BeautifulSoup(response.text, "html.parser")
    all_links = soup.find_all("a", {"class": "a_category"})
    clean_links = []
    for link in all_links:
        if "cars" in link.get("href"):
            clean_links.append(link.get("href"))
    return clean_links


def get_nested_links(path, cls):
    new_path = get_last_part_path(path)
    url = get_url(new_path)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    all_links = soup.find_all("a", {"class": "am"})
    paths = []
    for link in all_links:
        paths.append(f'https://www.ss.com{link.get("href")}')

    return paths


def print_links(links):
    for link in links:
        print(link)


def save_links(links):
    with open("links.txt", "w", encoding="utf-8") as f:
        for link in links:
            f.write(f"{link}\n")


def main(save_to_file=False):
    out = []
    links = get_links()
    for link in links:
        nested = get_nested_links(link, "am")
        out.append(link)
        out.extend(nested)
    if save_to_file:
        save_links(out)
    else:
        print_links(out)


if __name__ == "__main__":
    main(SAVE_TO_FILE)
