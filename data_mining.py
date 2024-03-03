#Set up a generic data pipeline
import requests
import pandas as pd



# set up
def get_cik_code(ticker, headers):

    ticker = ticker.upper().replace('.', '-')
    tickers_cik = requests.get("https://www.sec.gov/files/company_tickers.json", headers=headers).json()

    for company in tickers_cik.values():
        if company['ticker'] == ticker:
            CIK = str(company['cik_str']).zfill(10)
            return CIK

    # go through CIK codes and return ticker for further use?

def get_companyfacts():
    rpns = requests.get('https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json')
    print(rpns)