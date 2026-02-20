# tesla-stock-tracker-UPDATED-DAILY-9-30-AM
[![Daily Tesla Update](https://github.com/tamseel101/tesla-stock-tracker/actions/workflows/daily_update.yml/badge.svg)](https://github.com/tamseel101/tesla-stock-tracker/actions/workflows/daily_update.yml)

This project tracks Tesla stock data and news, generating a daily chart and updating the `README.md` automatically via GitHub Actions.

## Setup and Usage

### Running Locally

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/tesla-stock-tracker.git
    cd tesla-stock-tracker
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **API Keys (Optional - for live data)**:

    By default, the project uses static data files (`data/tesla_stock_data.csv` and `news/tesla_news.json`) included in the repository, allowing it to run out-of-the-box without any API keys.

    To fetch live stock data from Alpha Vantage and live news from Google Custom Search, you'll need to obtain free API keys:

    *   **Alpha Vantage**: [Get your free API key](https://www.alphavantage.co/support/#api-key)
    *   **Google Custom Search**: [Get your API key and Custom Search Engine ID (CX)](https://developers.google.com/custom-search/v1/overview)

    Once you have your keys, set them as environment variables (e.g., in your shell or a `.env` file that you don't commit to Git):

    ```bash
    export ALPHA_VANTAGE_API_KEY="YOUR_ALPHA_VANTAGE_API_KEY"
    export GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
    export GOOGLE_CX="YOUR_GOOGLE_CUSTOM_SEARCH_ENGINE_ID"
    ```

4.  **Run the scripts**:
    ```bash
    python fetch_data.py
    python plot_chart.py
    python fetch_news.py
    python update_readme.py
    ```

### GitHub Actions Workflow (for automated daily updates)

For automated daily updates on GitHub, you need to set your API keys as **GitHub Secrets** in your repository settings:

1.  Go to your repository on GitHub.
2.  Navigate to `Settings` > `Secrets and variables` > `Actions`.
3.  Add the following secrets:
    *   `ALPHA_VANTAGE_API_KEY`
    *   `GOOGLE_API_KEY`
    *   `GOOGLE_CX`

    The workflow `.github/workflows/daily_update.yml` will then use these secrets to fetch live data and update the `README.md` automatically.

## Project Structure

*   `fetch_data.py`: Fetches Tesla stock data (from Alpha Vantage or uses static data).
*   `plot_chart.py`: Plots a candlestick chart of Tesla stock data.
*   `fetch_news.py`: Fetches Tesla news (from Google Custom Search or uses static data).
*   `update_readme.py`: Updates the `README.md` with the latest chart and news.
*   `data/`: Stores `tesla_stock_data.csv`.
*   `news/`: Stores `tesla_news.json`.
*   `charts/`: Stores `tesla_stock_chart.png`.


## Tesla Stock Chart

![Tesla Stock Chart](charts/tesla_stock_chart.png?20260220150555)






















































































































































































## Latest Tesla News

**[Tesla Investor Relations](https://ir.tesla.com/)**

_Source: ir.tesla.com - Tesla's mission is to accelerate the world's transition to sustainable energy. Today, Tesla builds not only all-electric vehicles but also infinitely ..._

**[Tesla Motors Launches Revolutionary Supercharger Enabling ...](https://ir.tesla.com/press-release/tesla-motors-launches-revolutionary-supercharger-enabling)**

_Source: ir.tesla.com - Sep 24, 2012 ... Tesla revealed the locations of the first six Supercharger stations, which will allow the Model S to travel long distances with ultra fast charging._

**[Tesla Motors Begins Regular Production of 2008 Tesla Roadster](https://ir.tesla.com/press-release/tesla-motors-begins-regular-production-2008-tesla-roadster)**

_Source: ir.tesla.com - Mar 16, 2008 ... ... Roadster commenced today, marking an historical milestone for Tesla Motors and a watershed in the development of clean, zero-emissions vehicles._

**[Tesla Motors Announces Offerings of Common Stock and ...](https://ir.tesla.com/press-release/tesla-motors-announces-offerings-common-stock-and-convertible)**

_Source: ir.tesla.com - May 15, 2013 ... PALO ALTO, CA -- (Marketwired) -- 05/15/13 -- Tesla Motors, Inc. (NASDAQ: TSLA) announced today offerings of 2703027 shares of common stock ..._

**[Tesla Motors Announces Date for Second Quarter 2012 Financial ...](https://ir.tesla.com/press-release/tesla-motors-announces-date-second-quarter-2012-financial)**

_Source: ir.tesla.com - Jul 19, 2012 ... Tesla Motors, Inc. (NASDAQ: TSLA) announced today that it will post its financial results for the second quarter ended June 30, 2012, after market close on ..._

**[Tesla Motors Announces Date for Second Quarter 2013 Financial ...](https://ir.tesla.com/press-release/tesla-motors-announces-date-second-quarter-2013-financial)**

_Source: ir.tesla.com - Jul 16, 2013 ... PALO ALTO, CA -- (Marketwired) -- 07/16/13 -- Tesla Motors, Inc. (NASDAQ: TSLA) announced today that it will post its financial results for ..._

**[Tesla Motors to Begin Customer Deliveries of Model S on June 22nd](https://ir.tesla.com/press-release/tesla-motors-begin-customer-deliveries-model-s-june-22nd)**

_Source: ir.tesla.com - May 22, 2012 ... PALO ALTO, CA -- (Marketwire) -- 05/22/12 -- Tesla Motors (NASDAQ: TSLA) will begin delivering Model S, the world's first premium electric ..._

**[Tesla Motors Announces 2013 Annual Shareholder Meeting Webcast](https://ir.tesla.com/press-release/tesla-motors-announces-2013-annual-shareholder-meeting-webcast)**

_Source: ir.tesla.com - Jun 3, 2013 ... PALO ALTO, CA -- (Marketwired) -- 06/03/13 -- Tesla Motors, Inc. (NASDAQ: TSLA) announces the webcast for its 2013 Annual Shareholder ..._

**[Tesla Motors Releases Second Quarter 2012 Financial Results](https://ir.tesla.com/press-release/tesla-motors-releases-second-quarter-2012-financial-results)**

_Source: ir.tesla.com - Jul 25, 2012 ... PALO ALTO, CA -- (Marketwire) -- 07/25/12 -- Tesla Motors, Inc. (NASDAQ: TSLA) today released its second quarter 2012 financial results by ..._

**[Tesla Motors Releases Fourth Quarter & Full Year 2011 Financial ...](https://ir.tesla.com/press-release/tesla-motors-releases-fourth-quarter-full-year-2011-financial)**

_Source: ir.tesla.com - Feb 15, 2012 ... PALO ALTO, CA -- (MARKET WIRE) -- 02/15/12 -- Tesla Motors, Inc. (NASDAQ: TSLA) today released its fourth quarter and full year 2011 ..._

