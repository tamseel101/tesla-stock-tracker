import os
import yfinance as yf


def fetch_tesla_data():
    symbol = "TSLA"
    stock = yf.Ticker(symbol)
    df = stock.history(period="1y")

    os.makedirs("data", exist_ok=True)  # create the directory if it doesn't exist
    df.to_csv("data/tesla_stock_data.csv")


if __name__ == "__main__":
    fetch_tesla_data()

