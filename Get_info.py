import Glassdoor_Scraper as gs
import pandas as pd

path = "C:/Users/mauri/Desktop/Proyecto Data Science/chromedriver"

gs.fetch_jobs('data scientist', 11, path)