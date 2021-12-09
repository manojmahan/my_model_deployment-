def top20():
    import datetime
    import pandas as pd
    import numpy as np
    import time
    import yfinance as yf
    import pandas_datareader as pdr
    import yfinance as yf
    def save_sp500_tickers():
        import requests
        from bs4 import BeautifulSoup
        import bs4 as bs
        import pickle


        resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        table = soup.find('table', {'class': 'wikitable sortable'})
        tickers = []
        for row in table.findAll('tr')[1:]:
            ticker = row.findAll('td')[0].text
            tickers.append(ticker)
        with open("sp500tickers.pickle", "wb") as f:
            pickle.dump(tickers, f)
        return tickers
    tickers = save_sp500_tickers()
    a = []
    for i in tickers:
        a.append(i[:-1])
    #a = a[:10]
    final_dataframe = pd.DataFrame(a,columns=["company_name"])
    data = yf.download(a,'2021-12-8')['Adj Close']
    data =data.T
    
    return data




