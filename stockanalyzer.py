import pandas as pd
from bs4 import BeautifulSoup as bs
import requests


# Creating user ticker input
ticker_input = str(input("Enter a ticker: "))
print("Retrieving financial data for: {}".format(ticker_input))

# Scraping webpage
url = 'https://finviz.com/quote.ashx?t={}'.format(ticker_input.upper())
webpage_request = requests.get(url)
webpage_content = webpage_request.content
webpage_source = bs(webpage_content, 'lxml')

