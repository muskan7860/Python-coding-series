Each 5-minute candle contains:

Tag	Meaning
1. open	Price at start of 5-min
2. high	Highest price in 5-min
3. low	Lowest price in 5-min
4. close	Price at end of 5-min
5. volume	Number of shares traded

👉 These are standard stock market terms, not Python terms.

code:
import requests

def get_stock_data():
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        last_refreshed = data["Meta Data"]["3. Last Refreshed"]
        price = data["Time Series (5min)"][last_refreshed]["1. open"]
        return price
    else:
        return None

price = get_stock_data()
symbol = "IBM"
if price is not None:
    print(f"{symbol}: {price}")
else:
    print("Failed to retrieve data.")

