import requests
from bs4 import BeautifulSoup
import os

URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
OUTPUT_FILE = "inputs/original_text.txt"

def scrape_chapter():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")

    content_div = soup.find("div", class_="mw-parser-output")
    paragraphs = content_div.find_all("p")

    text = "\n\n".join([para.get_text() for para in paragraphs if para.get_text(strip=True)])

    os.makedirs("inputs", exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"✅ Chapter saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    scrape_chapter()


### search_version.py

from vector_store import search_versions

query = input("🔎 Enter your search query: ")
search_versions(query, top_k=3)
