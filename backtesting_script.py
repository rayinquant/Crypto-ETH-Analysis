'''binance is used for backtesting because most of the volume traded is on binance

change the date, ticker, timeframe to extract data'''


import ccxt
import pandas as pd
from datetime import datetime, timedelta
import warnings
import seaborn as sns

# Suppress warnings
warnings.filterwarnings('ignore')

# CCXT exchange setup
exchange = ccxt.binance({
    'rateLimit': 1200,
    'enableRateLimit': True,
})

# Function to fetch kline (OHLCV) data
def fetch_kline_price_data():
    ticker = 'BNB/USDT'
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
price_data.to_csv('bnb_price_data.csv')

# Function to place an order
# def place_order(symbol, type, side, amount, price=None):
#     try:
#         order = exchange.create_order(symbol, type, side, amount, price)
#         send_telegram_message(f"Order placed: {order}")
#         return order
#     except Exception as e:
#         send_telegram_message(f"An error occurred while placing order: {e}")

# place_order('BTC/USDT', 'limit', 'buy', 0.001, 30000)


from telegram import Bot
# Telegram bot setup
telegram_token = '6404732928:AAFMM3jg8A7KdH0rOizCXcDNDCWKlmAcWS8'
chat_id = '-4158563907'
bot = Bot(token=telegram_token)

# Function to send Telegram messages
def send_telegram_message(message):
    bot.send_message(chat_id=chat_id, text=message)