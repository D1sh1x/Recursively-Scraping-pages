import requests
from bs4 import BeautifulSoup
from time import sleep


def get_url():
    for count in range(1, 8):
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
        for i in data:
            card_url = "https://scrapingclub.com" + i.find("a").get("href")
            yield card_url


def array():
    for card_url in get_url():
        response = requests.get(card_url)
        sleep(3)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find("div", class_="card mt-4 my-4")
        img_url = "https://scrapingclub.com" + data.find("img", class_="card-img-top img-fluid").get("src")
        name = data.find("h3", class_="card-title").text
        price = data.find("h4").text
        desc = data.find("p", class_="card-text").text
        yield name, price, desc, img_url