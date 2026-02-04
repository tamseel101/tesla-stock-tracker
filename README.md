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

![Tesla Stock Chart](charts/tesla_stock_chart.png?20260204150704)






































































































































































## Latest Tesla News

**[Tesla Investor Relations](https://ir.tesla.com/)**

_Source: ir.tesla.com - Tesla's mission is to accelerate the world's transition to sustainable energy. Today, Tesla builds not only all-electric vehicles but also infinitely ..._

**[Tesla Motors Announces Offerings of Common Stock and ...](https://ir.tesla.com/press-release/tesla-motors-announces-offerings-common-stock-and-convertible)**

_Source: ir.tesla.com - May 15, 2013 ... In addition, Tesla has granted the underwriters a 30-day option to purchase up to an additional 405,454 shares of common stock and $67.5 million ..._

**[Tesla Motors Announces Major European Distribution Center in the ...](https://ir.tesla.com/press-release/tesla-motors-announces-major-european-distribution-center)**

_Source: ir.tesla.com - Dec 12, 2012 ... Tesla's decision to locate the new European Distribution Center in Tilburg is the result of almost two years of on-going cooperation between ..._

**[Tesla Motors Begins Regular Production of 2008 Tesla Roadster](https://ir.tesla.com/press-release/tesla-motors-begins-regular-production-2008-tesla-roadster)**

_Source: ir.tesla.com - Mar 16, 2008 ... Regular production of the 2008 Tesla Roadster commenced today, marking an historical milestone for Tesla Motors and a watershed in the development of clean, ..._

**[Press Releases | Tesla Investor Relations](https://ir.tesla.com/press)**

_Source: ir.tesla.com - AUSTIN, Texas, January 28, 2026 – Tesla has released its financial results for the fourth quarter and full year ended December 31, 2025 by posting an update ..._

**[Tesla Motors Announces Date for Second Quarter 2013 Financial ...](https://ir.tesla.com/press-release/tesla-motors-announces-date-second-quarter-2013-financial)**

_Source: ir.tesla.com - Jul 16, 2013 ... Tesla Motors Announces Date for Second Quarter 2013 Financial Results ... PALO ALTO, CA -- (Marketwired) -- 07/16/13 -- Tesla Motors, Inc. (NASDAQ ..._

**[Tesla Motors Releases Fourth Quarter & Full Year 2011 Financial ...](https://ir.tesla.com/press-release/tesla-motors-releases-fourth-quarter-full-year-2011-financial)**

_Source: ir.tesla.com - Feb 15, 2012 ... Tesla Motors Releases Fourth Quarter & Full Year 2011 Financial Results ... PALO ALTO, CA -- (MARKET WIRE) -- 02/15/12 -- Tesla Motors, Inc. ( ..._

**[Tesla Motors Releases Second Quarter 2012 Financial Results](https://ir.tesla.com/press-release/tesla-motors-releases-second-quarter-2012-financial-results)**

_Source: ir.tesla.com - Jul 25, 2012 ... Tesla Motors Releases Second Quarter 2012 Financial Results ... PALO ALTO, CA -- (Marketwire) -- 07/25/12 -- Tesla Motors, Inc. (NASDAQ: TSLA) ..._

**[Tesla Motors Announces Date for First Quarter 2011 Results](https://ir.tesla.com/press-release/tesla-motors-announces-date-first-quarter-2011-results)**

_Source: ir.tesla.com - Apr 18, 2011 ... Tesla has delivered more than 1,500 Roadsters to customers world-wide, and through its strategic partners is powering thousands of additional ..._

**[Tesla Motors Launches Revolutionary Supercharger Enabling ...](https://ir.tesla.com/press-release/tesla-motors-launches-revolutionary-supercharger-enabling)**

_Source: ir.tesla.com - Sep 24, 2012 ... Tesla revealed the locations of the first six Supercharger stations, which will allow the Model S to travel long distances with ultra fast charging._

