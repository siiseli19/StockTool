
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import seaborn as sns
import time
time.sleep(.1)





    #main
if __name__ == '__main__':
    # headers for requests
    headers = {'User-Agent': "sami.ojala97@gmail.com"}

    #set up
    tickers_cik = requests.get("https://www.sec.gov/files/company_tickers.json", headers=headers)
    tickers_cik = pd.json_normalize(pd.json_normalize(tickers_cik.json(), max_level=0).values[0])
    tickers_cik["cik_str"] = tickers_cik["cik_str"].astype(str).str.zfill(10)
    tickers_cik.set_index("ticker", inplace=True)
    print(tickers_cik)


def retrieve_data():
    response = requests.get("https://data.sec.gov/api/xbrl/companyconcept/CIK0000320193/us-gaap/Assets.json",headers=headers)
    print(response)