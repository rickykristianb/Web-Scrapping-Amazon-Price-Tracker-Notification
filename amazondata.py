import requests
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26",
    "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
}

class AmazonData:

    def __init__(self):
        self.URL = "https://www.amazon.com/Instant-Pot-Air-Fryer-One-Touch/dp/B07VT23JDM/ref=sr_1_1_sspa?crid=3PSQ1CR8UUPPA&" \
              "keywords=Instant+Pot+Duo+Evo+Plus+10-in-1+Pressure+Cooker&qid=1667359455&qu=eyJxc2MiOiIzLjAwIiwicXNhIjoiMi4" \
              "4OSIsInFzcCI6IjIuNTkifQ%3D%3D&sprefix=instant+pot+duo+evo+plus+10-in-1+pressure+cooker%2Caps%2C206&sr=8-1-" \
              "spons&psc=1"
        response = requests.get(url=self.URL, headers=header)
        data = response.content
        self.soup = BeautifulSoup(data, "html.parser")

    def get_price(self):
        price_scrap = self.soup.find(name="span", class_="a-offscreen")
        price = price_scrap.getText().split("$")[1]
        return price

    def get_product_name(self):
        product_name_scrap = self.soup.find(name="span", id="productTitle")
        name = product_name_scrap.getText()
        return name

