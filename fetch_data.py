import os
import yfinance as yf


def fetch_tesla_data():
    """
    Fetches Tesla (TSLA) stock data for the last year using yfinance and saves it to a CSV file.
    Includes error handling for data fetching issues.
    """
    symbol = "TSLA"
    try:
        stock = yf.Ticker(symbol)
        df = stock.history(period="1y")

        if df.empty:
            print(f"Warning: No data fetched for {symbol}. The DataFrame is empty.")
            return

        os.makedirs("data", exist_ok=True)  # create the directory if it doesn't exist
        df.to_csv("data/tesla_stock_data.csv")
        print(f"Successfully fetched and saved {symbol} stock data to data/tesla_stock_data.csv")
    except Exception as e:
        print(f"Error fetching Tesla stock data for {symbol}: {e}")


if __name__ == "__main__":
    fetch_tesla_data()

