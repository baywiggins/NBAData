import pandas as pd
import json

df = pd.read_csv('data/output.csv')

with open("data/def_rating.json", "r") as file:
    data = json.load(file)

# Must return 
def add_defensive_ratings(row):
    team_def_rtg = data[row['opponent']]
    year = int(row['date'].split("-")[-1])
    
    for i in team_def_rtg:
        if i['year'] == year:
            return i['def_rtg'], i['def_rtg_adj']
    
    return -1, -1
    

df[["def_rtg", "def_rtg_adj"]] = df.apply(add_defensive_ratings, axis=1, result_type="expand")

print(df)