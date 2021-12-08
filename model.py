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
    final_dataframe = pd.DataFrame(a,columns=["company_name"])
    data = yf.download(a,'2021-12-8')['Adj Close']
    data =data.T
    data1 = data.copy()
    c = data.columns[1].date()
    year = c.year
    month = c.month
    day = c.day
    month = str(month).zfill(2)
    day = str(day).zfill(2)
    y = f"{year}-{month}-{day}"
    data["previous_close"] = data[y]
    #data1 = yf.download(a,'2021-12-8')['Adj Close']
    #data1 =data1.T
    c = data1.columns[0]
    year = c.year
    month = c.month
    day = c.day
    month = str(month).zfill(2)
    day = str(day).zfill(2)
    x = f"{year}-{month}-{day}"
    data1["2nd_last_day"] = data1[x]
    d = [data1["2nd_last_day"], data["previous_close"]]
    headers = ["2nd_last_day","previous_close"]
    final_dataframe = pd.concat(d, axis=1, keys=headers)
    final_dataframe["%change in last 2 days"]=(final_dataframe["previous_close"]-final_dataframe["2nd_last_day"])/final_dataframe["2nd_last_day"]*100
    final_dataframe= final_dataframe.sort_values('%change in last 2 days',ascending=False)
    final_dataframe= final_dataframe.head(20)
    return final_dataframe
