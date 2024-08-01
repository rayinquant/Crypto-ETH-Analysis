'''binance is used for backtesting because most of the volume traded is on binance

change the date, ticker, timeframe to extract data'''


import ccxt
import pandas as pd
from datetime import datetime, timedelta
import warnings
import seaborn as sns
import matplotlib.pyplot as plt

# Suppress warnings
warnings.filterwarnings('ignore')

# CCXT exchange setup
exchange = ccxt.binance({
    'rateLimit': 1200,
    'enableRateLimit': True,
})

# Function to fetch kline (OHLCV) data
def fetch_kline_price_data():
    ticker = 'ETH/USDT'
    timeframe = '1d'
    start_time = datetime(2020, 5, 11)
    end_time = datetime.now()

    since = int(start_time.timestamp() * 1000)
    ohlcv_data = []

    while since < int(end_time.timestamp() * 1000):
        try:
            ohlcv = exchange.fetch_ohlcv(ticker, timeframe, since, limit=1500)
            if not ohlcv:
                break
            since = ohlcv[-1][0] + 1
            ohlcv_data.extend(ohlcv)
            print(f'Fetched {len(ohlcv)} records from {ticker} at {exchange.iso8601(since)}')
        except ccxt.BaseError as e:
            print(f'Error fetching data: {e}')
            break

    # Convert to DataFrame
    columns = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
    df = pd.DataFrame(ohlcv_data, columns=columns)

    # Convert timestamp to datetime
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='ms')

    # Set the index
    df.set_index('Timestamp', inplace=True)

    return df

# Fetch the data and print the first few rows
price_data = fetch_kline_price_data()
print(price_data)

# change the csv filename to the token you are doing backtesting on
price_data.to_csv('eth_price_data.csv')

# create a line plot of the closing price
plt.figure(figsize=(12, 6))
sns.lineplot(data=price_data, x=price_data.index, y='Close')
plt.title('ETH/USDT Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price (USDT)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('eth_price_chart.png')
plt.show()
