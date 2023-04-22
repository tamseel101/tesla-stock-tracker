import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_tesla_chart():
    df = pd.read_csv("data/tesla_stock_data.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    plt.figure(figsize=(12, 6))
    plt.plot(df["Date"], df["Close"])
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.title("Tesla Stock Price (Last 1 Year)")
    plt.grid()
    os.makedirs("charts", exist_ok=True)
    plt.savefig("charts/tesla_stock_chart.png")

if __name__ == "__main__":
    plot_tesla_chart()
