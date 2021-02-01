import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen

# Web scraping function
def web_scraper(url):
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(request).read()
    html_source = bs(webpage, "html.parser")
    return html_source

# Creating ticker urls
ticker_input = str(input("Enter a ticker(s) seperate ticker by spaces: " )).upper()
ticker_list = [ticker for ticker in ticker_input.split()]
    
# Data cleaning financial summary table from Finviz for multiple ticker comparison
tickers_df_list = []
for tickers in ticker_list:

    url = 'https://finviz.com/quote.ashx?t=' + tickers
    try:
        html_source = web_scraper(url)
    except Exception:
        raise NameError("Link invalid, re-enter ticker")

    df_list = []
    financial_df = pd.read_html(str(html_source), attrs = {'class': 'snapshot-table2'})[0]
    
    name = pd.read_html(str(html_source), attrs = {'class': 'fullview-title'})[0].iloc[1][0]
    print("Retrieving data for: " + name)
    
    length_columns = len(financial_df.columns.tolist())
    
    for split_times in range(2,length_columns + 2 ,2):
        split_df = financial_df.iloc[:,split_times - 2:split_times].set_index(split_times - 2)
        split_df.columns = [tickers]
        df_list.append(split_df)
        
    df_concat = pd.concat(df_list, axis = 0, sort = True)
    tickers_df_list.append(df_concat)
    
tickers_df = pd.concat(tickers_df_list, axis = 1)

# Removing unwanted rows for plotting

drop_unwanted_rows = tickers_df.drop('Index
'Employees'
Optionable
Shortable
Insider Own
Insider Trans
RSI(14)
Rel Volume
Avg Volume
Volume
ATR
Beta
Volatility
)