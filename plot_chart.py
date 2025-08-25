import os
import pandas as pd
import mplfinance as mpf

def plot_tesla_chart():
    """
    Fetches Tesla stock data, plots a candlestick chart, identifies basic support/resistance levels,
    and saves the chart as a PNG image.
    """
    # Load stock data
    try:
        df = pd.read_csv("data/tesla_stock_data.csv", index_col="Date", parse_dates=True)
    except FileNotFoundError:
        print("Error: tesla_stock_data.csv not found. Please run fetch_data.py first.")
        return
    except Exception as e:
        print(f"Error loading stock data: {e}")
        return

    # Ensure the DataFrame has the required columns for mplfinance
    df.index.name = "Date"
    # Ensure the index is a DatetimeIndex before passing to mplfinance
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index)
    df = df[["Open", "High", "Low", "Close", "Volume"]]

    # Calculate basic support and resistance levels
    # This is a simplified approach, a more robust method would involve more complex algorithms
    support_levels = []
    resistance_levels = []
    window = 20 # Look back window for identifying S/R

    for i in range(window, len(df)):
        # Simple support: if current low is a new low within the window
        if df["Low"].iloc[i] == df["Low"].iloc[i-window:i].min():
            support_levels.append((df.index[i], df["Low"].iloc[i]))
        # Simple resistance: if current high is a new high within the window
        if df["High"].iloc[i] == df["High"].iloc[i-window:i].max():
            resistance_levels.append((df.index[i], df["High"].iloc[i]))

    # Convert S/R levels to scatter plots for mplfinance
    apds = []
    for date, price in support_levels:
        apds.append(mpf.make_addplot(pd.Series(price, index=[date]), type='scatter', marker='^', markersize=100, color='green'))
    for date, price in resistance_levels:
        apds.append(mpf.make_addplot(pd.Series(price, index=[date]), type='scatter', marker='v', markersize=100, color='red'))

    # Create the candlestick chart
    fig, axlist = mpf.plot(df, 
                           type='candle', 
                           style='yahoo', 
                           title='Tesla Stock Price (Candlestick) with Support/Resistance',
                           ylabel='Price',
                           ylabel_lower='Volume',
                           figscale=1.5,
                           addplot=apds, # Add support/resistance plots
                           returnfig=True
                          )

    # Add comments for support and resistance
    # This is a simplified display; more advanced charts might label specific levels
    if support_levels:
        axlist[0].text(df.index[-10], df["High"].max() * 0.95, "Green triangles: Support Levels", color='green', fontsize=10, ha='right')
    if resistance_levels:
        axlist[0].text(df.index[-10], df["High"].max() * 0.90, "Red triangles: Resistance Levels", color='red', fontsize=10, ha='right')

    # Create 'charts' directory if it doesn't exist
    os.makedirs("charts", exist_ok=True)
    # Save the chart
    mpf.savefig("charts/tesla_stock_chart.png", fig=fig)
    print("Candlestick chart with S/R levels saved to charts/tesla_stock_chart.png")

if __name__ == "__main__":
    plot_tesla_chart()
