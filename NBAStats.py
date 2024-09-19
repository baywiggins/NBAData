from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import League
from basketball_reference_web_scraper.data import OutputType
import pandas as pd
from lxml.etree import ParserError
import dotenv
import os
import json

YEARS = [2023]
MONTHS = [1, 2, 3, 4, 5, 6, 10, 11, 12]
# MONTHS = [6]
END_DAY = 31

OUTPUT_TYPE = OutputType.JSON
OUTPUT_FILE = 'data/output.csv'

needs_header = False

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
    for month in MONTHS:
        for day in range(4, END_DAY + 1):
            try:
                j = json.loads(client.player_box_scores(day=day, month=month, year=year, output_type=OUTPUT_TYPE))
                if not j:
                    continue
            except ParserError:
                continue

            df = pd.DataFrame(j)

            df.drop(columns=["slug"], inplace=True)

            df['date'] = f"{month}-{day}-{year}"

            df[['def_rtg', 'def_rtg_adj']] = df.apply(add_defensive_ratings, axis=1, result_type="expand")
            

            df.to_csv(OUTPUT_FILE, mode='a', index=False, header=True if needs_header else False)
            needs_header = False
