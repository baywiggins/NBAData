from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.basketball-reference.com/leagues/NBA_2023_ratings.html")

soup = BeautifulSoup(r.content, 'html.parser')

# Find all the rows in the table
# Find the table rows (all rows except for header rows)
rows = soup.find_all('tr')

# Initialize a list to store extracted data
data = []

# Iterate through each row
for row in rows:
    # Find all 'td' elements in the row (data cells)
    cols = row.find_all('td')

    # Check if the row contains the correct number of columns
    if len(cols) > 0:
        # Extract team name, def_rtg, and def_rtg_adj
        print(cols)
        team_name = cols[0].get_text(strip=True)
        def_rtg = cols[9].get_text(strip=True)
        def_rtg_adj = cols[13].get_text(strip=True)
        
        # Append the extracted data to the list
        data.append({'team': team_name, 'def_rtg': def_rtg, 'def_rtg_adj': def_rtg_adj})

# Display the extracted data
for entry in data:
    print(entry)


# # Extract team names and defensive ratings
# for row in rows:
#     team_name = row.find('td', {'data-stat': 'team_name'}).text
#     def_rtg = row.find('td', {'data-stat': 'def_rtg'}).text
#     print(f'Team: {team_name}, Defensive Rating: {def_rtg}')