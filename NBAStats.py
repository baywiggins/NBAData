from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import League
from basketball_reference_web_scraper.data import OutputType
import pandas as pd
from lxml.etree import ParseError
import dotenv
import os
import json

YEARS = [2024]
END_MONTH = 1
END_DAY = 1

OUTPUT_TYPE = OutputType.JSON
OUTPUT_FILE = 'data/output.csv'

needs_header = True

with open('data/def_rating.json') as file:
    def_rating_data = json.load(file)

def add_defensive_ratings(row):
    team_def_rtg = def_rating_data[row['opponent']]
    year = int(row['date'].split("-")[-1])
    
    for i in team_def_rtg:
        if i['year'] == year:
            return i['def_rtg'], i['def_rtg_adj']
    
    return -1, -1


for year in YEARS:
    for month in range(1, END_MONTH + 1):
        for day in range(1, END_DAY + 1):
            df = pd.read_json(client.player_box_scores(day=day, month=month, year=year, output_type=OUTPUT_TYPE))

            df.drop(columns=["slug"], inplace=True)

            df['date'] = f"{month}-{day}-{year}"

            df[['def_rtg', 'def_rtg_adj']] = df.apply(add_defensive_ratings, axis=1, result_type="expand")
            

            df.to_csv(OUTPUT_FILE, mode='a', index=False, header=True if needs_header else False)
            needs_header = False
