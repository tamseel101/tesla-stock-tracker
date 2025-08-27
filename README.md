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

![Tesla Stock Chart](charts/tesla_stock_chart.png?20250827144147)





## Latest Tesla News

**[Tesla Investor Relations](https://ir.tesla.com/)**

_Source: ir.tesla.com - Tesla's mission is to accelerate the world's transition to sustainable energy. Today, Tesla builds not only all-electric vehicles but also infinitely ..._

**[Tesla Motors to Manufacture Sedan in California | Tesla Investor ...](https://ir.tesla.com/press-release/tesla-motors-manufacture-sedan-california)**

_Source: ir.tesla.com - Jun 29, 2008 ... Tesla's next product, a 4-door, 5-passenger sedan, will be manufactured at a facility in the state of California._

**[Press Releases | Tesla Investor Relations](https://ir.tesla.com/press)**

_Source: ir.tesla.com - Tesla has released its financial results for the first quarter of 2025 by posting an update on its Investor Relations website._

**[Tesla Motors Begins Regular Production of 2008 Tesla Roadster ...](https://ir.tesla.com/press-release/tesla-motors-begins-regular-production-2008-tesla-roadster)**

_Source: ir.tesla.com - Mar 16, 2008 ... Regular production of the 2008 Tesla Roadster commenced today, marking an historical milestone for Tesla Motors and a watershed in the development of clean, ..._

**[Tesla First Quarter 2025 Production, Deliveries & Deployments](https://ir.tesla.com/press-release/tesla-first-quarter-2025-production-deliveries-and-deployments)**

_Source: ir.tesla.com - Apr 2, 2025 ... At that time, Tesla will issue a brief advisory containing a link to the Q1 2025 update which will be available on Tesla's Investor Relations ..._

**[Tesla, Inc. (TSLA) Stock Price, News, Quote & History - Yahoo Finance](https://ca.finance.yahoo.com/quote/TSLA/)**

_Source: ca.finance.yahoo.com - Find the latest Tesla, Inc. (TSLA) stock quote, history, news and other vital information to help you with your stock trading and investing._

**[Tesla Motors Announces Offerings of Common Stock and ...](https://ir.tesla.com/press-release/tesla-motors-announces-offerings-common-stock-and-convertible)**

_Source: ir.tesla.com - May 15, 2013 ... PALO ALTO, CA -- (Marketwired) -- 05/15/13 -- Tesla Motors, Inc. (NASDAQ: TSLA) announced today offerings of 2703027 shares of common stock ..._

**[Tesla Motors Releases Second Quarter 2011 Financial Results ...](https://ir.tesla.com/press-release/tesla-motors-releases-second-quarter-2011-financial-results)**

_Source: ir.tesla.com - Aug 3, 2011 ... PALO ALTO, CA -- (MARKET WIRE) -- 08/03/11 -- Tesla Motors, Inc. (NASDAQ: TSLA) today released its second quarter 2011 financial results by ..._

**[Tesla Motors Launches Revolutionary Supercharger Enabling ...](https://ir.tesla.com/press-release/tesla-motors-launches-revolutionary-supercharger-enabling)**

_Source: ir.tesla.com - Sep 24, 2012 ... Tesla revealed the locations of the first six Supercharger stations, which will allow the Model S to travel long distances with ultra fast charging._

**[Tesla Motors and Toyota Motor Corporation Intend to Work Jointly ...](https://ir.tesla.com/press-release/tesla-motors-and-toyota-motor-corporation-intend-work-jointly-ev)**

_Source: ir.tesla.com - May 19, 2010 ... The two companies intend to form a specialist team to further those efforts. TMC has agreed to purchase $50 million of Tesla's common stock ..._

