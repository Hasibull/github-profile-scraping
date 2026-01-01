import requests
from bs4 import BeautifulSoup

BASE_URL = "https://github.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

class Scraper:
    def __init__(self):
        pass

    def scrape_user(self, username: None) -> dict:
        """Extract profile information for the given username"""

        url = BASE_URL + username
        response = requests.get(url, headers=HEADERS)

        print("response type:", type(response))
        print(response)

scraper = Scraper()
scraper.scrape_user("Hasibull")