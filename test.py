from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
import pandas
import json
import sys
from lxml.etree import ParserError


x = json.loads(client.player_box_scores(day=35, month=5, year=2024, output_type=OutputType.JSON))


df = pandas.DataFrame(x)

print(df)