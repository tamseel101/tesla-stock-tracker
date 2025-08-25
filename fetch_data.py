import os
import pandas as pd
from datetime import datetime
from alpha_vantage.timeseries import TimeSeries
from dotenv import load_dotenv

load_dotenv()

def fetch_tesla_data():
    symbol = "TSLA"
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")  # Read from environment variable
    
    if not api_key:
        print("Warning: ALPHA_VANTAGE_API_KEY environment variable not set. Skipping live stock data fetch.")
        # If no API key, check if a data file already exists to avoid errors in subsequent steps
        if not os.path.exists("data/tesla_stock_data.csv"):
            print("No existing stock data file found. Creating an empty DataFrame.")
            df = pd.DataFrame(columns=['Open', 'High', 'Low', 'Close', 'Volume'])
            # Ensure index is datetime for compatibility with plot_chart.py
            df.index = pd.to_datetime(df.index)
            os.makedirs("data", exist_ok=True)
            df.to_csv("data/tesla_stock_data.csv")
        return # Exit the function, as we cannot fetch live data

    print(f"Attempting to fetch data for symbol: {symbol} using Alpha Vantage.")

    try:
        ts = TimeSeries(key=api_key, output_format='pandas')
        # Get daily data (free tier endpoint)
        # Using 'compact' to get the most recent 100 data points, then filter for today
        df, meta_data = ts.get_daily(symbol=symbol, outputsize='compact')
        
        # Alpha Vantage returns '4. close' for closing price, rename for consistency
        df = df.rename(columns={
            '1. open': 'Open',
            '2. high': 'High',
            '3. low': 'Low',
            '4. close': 'Close',
            '5. volume': 'Volume'
        })
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()
        df.index.name = 'Date' # Add this line to set the index name

        # Filter for the most recent day's data
        if not df.empty:
            latest_date = df.index.max()
            df = df.loc[df.index == latest_date]
            print(f"Fetched data for: {latest_date.strftime('%Y-%m-%d')}")

        print("Attempting to fetch data.")

        # Check if the dataframe is empty before trying to print head
        if not df.empty:
            print(f"DataFrame after fetch (first 5 rows):\n{df.head()}")
        else:
            print("DataFrame is empty after fetch (no rows to display).")

        print(f"DataFrame is empty: {df.empty}")

        if df.empty:
            print(f"Warning: No data fetched for {symbol} for today.")
            return

        os.makedirs("data", exist_ok=True)
        df.to_csv("data/tesla_stock_data.csv")
        print(f"Successfully fetched and saved {symbol} stock data to data/tesla_stock_data.csv")

    except Exception as e:
        print(f"Error fetching Tesla stock data: {e}")


if __name__ == "__main__":
    fetch_tesla_data()
