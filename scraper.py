from bs4 import BeautifulSoup
import requests
import json

YEARS = [2000 + i for i in range(3, 25)]
OUTPUT_FILE = 'data/def_rating.json'


data = {}

for year in YEARS:
    r = requests.get(f"https://www.basketball-reference.com/leagues/NBA_{year}_ratings.html")

    soup = BeautifulSoup(r.content, 'html.parser')

    # Find all the rows in the table
    # Find the table rows (all rows except for header rows)
    rows = soup.find_all('tr')
    data_to_add = []

    # Iterate through each row
    for row in rows:
        # Find all 'td' elements in the row (data cells)
        cols = row.find_all('td')

        # Check if the row contains the correct number of columns
        if len(cols) > 0:
            # Extract team name, def_rtg, and def_rtg_adj
            team_name = cols[0].get_text(strip=True)
            def_rtg = cols[8].get_text(strip=True)
            def_rtg_adj = cols[12].get_text(strip=True)
            
            # Append the extracted data to the list
            data_to_add.append({'team': team_name, 'def_rtg': def_rtg, 'def_rtg_adj': def_rtg_adj})
            data[year] = data_to_add


with open(OUTPUT_FILE, 'w') as f:
    json.dump(data, f, indent=4)