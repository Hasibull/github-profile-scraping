import argparse
from scraper.github_scraper import Scraper

def read_usernames_from_file(filepath: str) -> list:
    with open(filepath, "r") as file:
        return [line.strip() for line in file if line.strip()]


def main() -> None:
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
        print(username, sep=" ")

if __name__ == "__main__":
    main()