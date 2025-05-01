import os
import re
from collections import Counter
from bs4 import BeautifulSoup

# Read the list of countries from countries.txt
# Each line in the file contains the name of a country
with open("countries.txt", "r", encoding="utf-8") as f:
    countries = [line.strip() for line in f.readlines()]

# Directory containing the press briefing HTML files
# Output file to write the country counts
INPUT_DIR = "press_briefings"
OUTPUT_FILE = "country_counts.txt"

# Initialize a counter for country mentions
country_counter = Counter()

# Process each briefing file
# Count occurrences of each country name - later write the results to an output file
for filename in os.listdir(INPUT_DIR):
    file_path = os.path.join(INPUT_DIR, filename)
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Parse HTML content
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text().lower()
    
    # Count occurrences of each country name
    for country in countries:
        country_lower = country.lower()
        matches = re.findall(rf'\b{re.escape(country_lower)}\b', text)
        country_counter[country] += len(matches)

# Write results to an output file
# Sort the countries by count in descending order
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for country, count in country_counter.most_common():
        f.write(f"{count} {country}\n")

print("Processing complete. Country counts saved to country_counts.txt.")
