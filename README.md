# Binance Historical Price Data Extraction and Visualization

This script extracts historical price data for a specified cryptocurrency trading pair from Binance using the CCXT library. It fetches OHLCV (Open, High, Low, Close, Volume) data, saves it as a CSV file, and visualizes the closing prices over time.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [Example Output](#example-output)
- [License](#license)

## Overview

This project uses the `ccxt` library to access Binance and retrieve historical price data, specifically OHLCV data for the `ETH/USDT` trading pair. The data is stored in a CSV file and plotted using `seaborn` and `matplotlib`. You can customize the trading pair, timeframe, start and end dates.

### Key Features
- Fetches OHLCV data from Binance.
- Stores data in a structured CSV file.
- Visualizes the closing price trend over time.

## Requirements

To run this script, you need:

- Python 3.11.9
- ccxt
- pandas
- seaborn
- matplotlib

You can install the required packages with:

```bash
pip install ccxt pandas seaborn matplotlib
```

## Setup

1. **Clone this repository:**

    ```bash
    git clone <your-repository-url>
    ```

2. **Navigate to the project folder:**

    ```bash
    cd <your-repository-folder>
    ```
    
## Usage

Run the script with:

```bash
python <script_name>.py
```

## Configuration

You can modify the following variables in the script to customize the data extraction:

- **`ticker`**: The cryptocurrency pair to fetch (default: `'ETH/USDT'`).
- **`timeframe`**: Time interval for OHLCV data (default: `'1d'`).
- **`start_time`**: Start date for data extraction (default: `datetime(2020, 5, 11)`).
- **`end_time`**: End date for data extraction (default: current date).

After making any modifications, re-run the script to fetch and save the updated data.

## Example Output

The script will generate a line plot of the closing price trend for the specified asset over time.

### Example CSV file:

```csv
Timestamp,Open,High,Low,Close,Volume
2020-05-11 00:00:00,195.2,199.5,193.8,198.4,31840.23
...
```

## License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for more details.

## Notes

- **Binance Rate Limits**: Binance rate limits apply to this script. If needed, adjust the `rateLimit` parameter in `ccxt.binance()` to avoid hitting these limits.

Happy backtesting!

