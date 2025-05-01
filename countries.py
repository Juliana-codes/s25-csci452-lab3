import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the wiki page
response = requests.get("https://en.wikipedia.org/wiki/List_of_sovereign_states")

# Check if the request was successful (status code 200)
if response.status_code != 200:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    ()  # Exit the program if the webpage couldn't be retrieved

# Parse the HTML content of the webpage using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")


# Find the table containing the list of countries and get the names of the countries
# each row contains the name of a country, so we need to find it
countries = [
    link.get("title") if link and link.get("title") else link.text.strip()
    for row in soup.select("table.wikitable tbody tr")
    if (link := row.find("a"))
]

# Remove duplicates (just in case it picked up from the link and a) and sort the list alphabetically - sorting not needed for the task
countries = sorted(set(countries))
print("Retrieved the countries, now writing countries to countries.txt")

# Save to a txt file
with open("countries.txt", "w", encoding="utf-8") as f:
    for country in countries:
        f.write(f'{country}\n')
    f.close()

print("Scraping complete. Countries saved in countries.txt.")
