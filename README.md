# Simple github profile info scraper in Python

A Python-based GitHub profile scraper using **requests** and **BeautifulSoup**.

## ✨ Features
- Scrape public GitHub profile data
- Supports single or multiple usernames
- Clean JSON output
- No Selenium, no API usage

## 📦 Installation

```bash
git clone https://github.com/Hasibull/github-profile-scraping.git
cd github-profile-scraper
pip install -r requirements.txt
```

## 🚀 Usage
Single Username
```python
python main.py -u torvalds
```
Multiple usernames from file
```python
python main.py -f data/usernames.txt
```
Output the scraped data to specified file name
```python
python main.py -u octocat -o output/octocat.json
```
**N:B:** default path is output/Userinfo.json