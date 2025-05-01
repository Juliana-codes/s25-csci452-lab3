import os
import requests
from bs4 import BeautifulSoup

# Directory setup
INDEX_DIR = "press_briefings"
BRIEFINGS_DIR = "briefings"
os.makedirs(BRIEFINGS_DIR, exist_ok=True)

# Base URL for the press briefings
BASE_URL = "http://cs.millersville.edu/~sschwartz/mirror/www.whitehouse.gov"

# Process each index page
for index_file in os.listdir(INDEX_DIR):
    index_path = os.path.join(INDEX_DIR, index_file)
    
    with open(index_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    
    # Find all briefing links
    for link in soup.select("a[href]"):
        href = link["href"]
        if "/briefing-room/press-briefings/" in href:
            
            # Fetch the briefing page
            response = requests.get(BASE_URL + href)
            if response.status_code != 200:
                print(f"Failed to download briefing from {href}")
                continue
            
            briefing_soup = BeautifulSoup(response.text, "html.parser")
            title = briefing_soup.find("h1").get_text(strip=True) if briefing_soup.find("h1") else "Untitled"
            content = briefing_soup.get_text()
            
            # Save the briefing text
            safe_title = "_".join(title.split())[:50]  # Ensure filename safety
            file_path = os.path.join(BRIEFINGS_DIR, f"{safe_title}.txt")
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"{content}")
            
            print(f"Downloaded: {title}")

print("All available briefings have been downloaded.")
