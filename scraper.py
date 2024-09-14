from bs4 import BeautifulSoup
import requests
import json

YEARS = [2000 + i for i in range(3, 25)]
OUTPUT_FILE = 'data/def_rating.json'

# Initialize a dictionary to store data by team
team_data = {}

for year in YEARS:
    r = requests.get(f"https://www.basketball-reference.com/leagues/NBA_{year}_ratings.html")
    soup = BeautifulSoup(r.content, 'html.parser')

    # Find the table rows (all rows except for header rows)
    rows = soup.find_all('tr')

    # Iterate through each row
    for row in rows:
        # Find all 'td' elements in the row (data cells)
        cols = row.find_all('td')

        # Check if the row contains the correct number of columns
        if len(cols) > 0:
            # Extract team name, def_rtg, and def_rtg_adj
            team_name = cols[0].get_text(strip=True).upper()
            def_rtg = cols[8].get_text(strip=True)
            def_rtg_adj = cols[12].get_text(strip=True)

            # If the team is not already in the dictionary, add it
            if team_name not in team_data:
                team_data[team_name] = []

            # Append the defensive ratings for this year to the team's list
            team_data[team_name].append({
                'year': year,
                'def_rtg': def_rtg,
                'def_rtg_adj': def_rtg_adj
            })

# Save the data to a JSON file
with open(OUTPUT_FILE, 'w') as f:
    json.dump(team_data, f, indent=4)
