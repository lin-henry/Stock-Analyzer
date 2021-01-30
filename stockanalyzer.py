import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen

# Web scraping function
def web_scraper(url):
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(request).read()
    html_source = str(bs(webpage, "html.parser"))
    return html_source

# Creating ticker urls
ticker_input = str(input("Enter a ticker(s) seperate ticker by spaces: ")).upper()
ticker_list = [ticker for ticker in ticker_input.split()]
print("Retrieving financial data for: {}".format(ticker_input + "\n"))

df_list = []
for tickers in ticker_list:
    url = 'https://finviz.com/quote.ashx?t=' + tickers
    try:
        html_source = web_scraper(url)
    except Exception:
        raise NameError("Link invalid, re-enter ticker")

    # Data cleaning financial summary table from Finviz for multiple ticker comparison
    financial_df = pd.read_html(html_source, attrs = {'class': 'snapshot-table2'})[0]
    length_columns = len(financial_df.columns.tolist())
    
    for split_times in range(2,length_columns +2 ,2):
        split_df = financial_df.iloc[:,split_times - 2:split_times].set_index(split_times - 2)
        df_list.append(split_df)
    
    df_concat = pd.concat(df_list, axis = 0)