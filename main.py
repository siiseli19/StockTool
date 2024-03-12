import requests
import pandas as pd
import time
from data_mining import get_cik_code, get_companyfacts


# Defining main function
def main():

    ticker = 'wsm'
    headers = {'User-Agent': "sami.ojala97@gmail.com"}
    #returns CIK code for further use
    CIK = get_cik_code(ticker, headers)
    print(CIK
    print('testi')






# __name__
if __name__ == "__main__":
    time.sleep(.1)
    main()