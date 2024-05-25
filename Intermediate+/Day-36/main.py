import requests
import datetime
import os
from dateutil.relativedelta import relativedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_prices():
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": os.environ['STOCK_API_KEY']
    }
    response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()
    print(os.environ['M2'])
    print(response.json()['Time Series (Daily)'])
    time_series = response.json()['Time Series (Daily)']
    print(list(time_series.items())[0][1])
    open_price = float(list(time_series.items())[0][1]['1. open'])
    close_price = float(list(time_series.items())[1][1]['4. close'])
    return open_price, close_price

def get_news():
    #last_month = datetime.datetime.now() - relativedelta(months=1)
    last_month = datetime.datetime.now() - datetime.timedelta(days=3)
    parameters = {
        "q": "tesla",
        "from": last_month,
        "apikey": os.environ['NEWS_API_KEY'],
        "sortBy": "publishedAt"
    }
    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
    last_news = []
    for i in range(0, 4):
        last_news.append(response.json()['articles'][i]['title'])
    print(last_news)


if __name__ == "__main__":
    yesterday, past_yesterday = get_prices()
    is_high_change = past_yesterday < yesterday * 0.9 or past_yesterday > yesterday * 1.1
    if not is_high_change:
        get_news()
