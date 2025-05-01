import os
import requests

# Base URL for press briefings
BASE_URL = "http://cs.millersville.edu/~sschwartz/mirror/www.whitehouse.gov/briefing-room/press-briefings%3fpage="
OUTPUT_DIR = "press_briefings"

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

page = 1
while True:
    url = f"{BASE_URL}{page}"
    response = requests.get(url)
    
    if response.status_code == 404:
        print(f"No more pages found. Stopping at page {page - 1}.")
        break
    
    file_path = os.path.join(OUTPUT_DIR, f"{page}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(response.text)
    
    print(f"Downloaded page {page}")
    page += 1

print("All available press briefing pages have been downloaded.")