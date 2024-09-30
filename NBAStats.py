from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import League
from basketball_reference_web_scraper.data import OutputType
import pandas as pd
from lxml.etree import ParserError
import dotenv
import os
import json

x = client.player_box_scores(day=1, month=1, year=2017, output_type=OutputType.JSON)

print(x)