import json
import argparse
from scraper.github_scraper import Scraper
from pathlib import Path

def read_usernames_from_file(filepath: str) -> list:
    with open(filepath, "r") as file:
        return [line.strip() for line in file if line.strip()]


def main() -> None:
    results = []
    scraper = Scraper()
    file_path = None
    parser = argparse.ArgumentParser(description="Github Profile Scraper")
    parser.add_argument("-u", "--user", help="Single Github Username")
    parser.add_argument("-f", "--file", help="File containing Github Usernames")
    parser.add_argument('-o', "--output", default="output/Userinfo.json", help="Output scraped user info into json file")

    args = parser.parse_args()
    usernames = []

    if args.user:
        usernames.append(args.user)
    
    if args.file:
        usernames.extend(read_usernames_from_file(args.file))
    
    if not usernames:
        print("No usernames provided!")
        return
    
    for username in usernames:
        print(f"[+] Scraping {username}")
        data = scraper.scrape_user(username)

        if data:
            results.append(data)

    file_path = Path(args.output)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    print(f"\n✅ Data saved to {args.output}")


if __name__ == "__main__":
    main()