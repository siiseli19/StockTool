
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import seaborn as sns


#user agent   headers = {'User-Agent': "your@email.com"}
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass


#api key = "C:\OMISTAJA\PycharmProjects".......



#The Extractor API returns individual sections from 10-Q, 10-K and 8-K filings.
# The extracted section is cleaned and standardized - in raw text or in standardized HTML.
# You can programmatically extract one or multiple sections from any 10-Q, 10-K and 8-K filing.