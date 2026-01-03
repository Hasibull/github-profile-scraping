import requests
from bs4 import BeautifulSoup

BASE_URL = "https://github.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

class Scraper:
    def __init__(self):
        pass

    def get_text(self, bsi, selector: str) -> str:
        tag = bsi.select_one(selector)
        return tag.text.strip() if tag else None

    def scrape_user(self, username: None) -> dict:
        """Extract profile information for the given username"""

        url = BASE_URL + username
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            return None
        
        soup = BeautifulSoup(response.text, "html.parser")

        profile = {
            "username": username,
            "name": self.get_text(soup, "span.p-name"),
            "bio": self.get_text(soup, "div.p-note"),
            "location": self.get_text(soup, "li[itemprop='homeLocation'] span"),
            "company": self.get_text(soup, "li[itemprop='worksFor'] span"),
            "email": self.get_text(soup, "li[itemprop='email'] a"),
            "website": self.get_text(soup, "li[itemprop='url'] a"),
            "followers": self.get_text(soup, "a[href$='?tab=followers'] span"),
            "following": self.get_text(soup, "a[href$='?tab=following'] span"),
            "repositories": self.get_text(soup, "span.Counter"),
            "profile_url": url
        }

        return profile