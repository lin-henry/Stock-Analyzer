import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen

# Creating ticker url
ticker_input = str(input("Enter a ticker: "))
print("Retrieving financial data for: {}".format(ticker_input))
url = 'https://finviz.com/quote.ashx?t={}'.format(ticker_input.upper())

# Scraping webpage
def web_scraper(url):
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(request).read()
    html_source = str(bs(webpage, "html.parser"))
    return html_source

html_source = web_scraper(url)

# Data cleaning financial summary table from Finviz for multiple ticker comparison
financial_df = pd.read_html(html_source, attrs = {'class': 'snapshot-table2'})[0]

length_columns = len(financial_df.columns.tolist())

for split_times in range(2,length_columns +2 ,2):
    split_df = financial_df.iloc[:,split_times - 2:split_times]
    