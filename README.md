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

![Tesla Stock Chart](charts/tesla_stock_chart.png?20260713165453)



































































































































































































































































































































## Latest Tesla News

**[Press Releases | Tesla Investor Relations](https://ir.tesla.com/press)**

_Source: ir.tesla.com - Jun 26, 2026. Please find below the latest company-compiled delivery consensus of sell-side analysts. Tesla does not endorse any information, recommendations or ..._

**[Tesla Investor Relations](https://ir.tesla.com/)**

_Source: ir.tesla.com - Tesla's mission is to accelerate the world's transition to sustainable energy. Today, Tesla builds not only all-electric vehicles but also infinitely ..._

**[Tesla Motors Releases Fourth Quarter & Full Year 2011 Financial ...](https://ir.tesla.com/press-release/tesla-motors-releases-fourth-quarter-full-year-2011-financial)**

_Source: ir.tesla.com - Feb 15, 2012 ... (NASDAQ: TSLA) today released its fourth quarter and full year 2011 financial results by posting the current Shareholder Letter on its website._

**[Tesla Motors Announces Offerings of Common Stock and ...](https://ir.tesla.com/press-release/tesla-motors-announces-offerings-common-stock-and-convertible)**

_Source: ir.tesla.com - May 15, 2013 ... PALO ALTO, CA -- (Marketwired) -- 05/15/13 -- Tesla Motors, Inc. (NASDAQ: TSLA) announced today offerings of 2703027 shares of common stock ..._

**[Tesla Motors Announces Major European Distribution Center in the ...](https://ir.tesla.com/press-release/tesla-motors-announces-major-european-distribution-center)**

_Source: ir.tesla.com - Dec 12, 2012 ... The new Tesla European Distribution Center will lead to the creation of approximately 50 jobs in the next few years. Tesla's decision to locate ..._

**[Tesla Motors Announces Follow-on Offering | Tesla Investor Relations](https://ir.tesla.com/press-release/tesla-motors-announces-follow-offering?releaseid=709221?releaseid=709221)**

_Source: ir.tesla.com - Sep 25, 2012 ... PALO ALTO, CA -- (Marketwire) -- 09/25/12 -- Tesla Motors, Inc. (NASDAQ: TSLA) announced today a follow-on offering of 4,344,930 shares of ..._

**[Tesla Motors Launches Revolutionary Supercharger Enabling ...](https://ir.tesla.com/press-release/tesla-motors-launches-revolutionary-supercharger-enabling)**

_Source: ir.tesla.com - Sep 24, 2012 ... Tesla revealed the locations of the first six Supercharger stations, which will allow the Model S to travel long distances with ultra fast charging._

**[Tesla Motors Announces 2012 Annual Shareholder Meeting](https://ir.tesla.com/press-release/tesla-motors-announces-2012-annual-shareholder-meeting)**

_Source: ir.tesla.com - May 2, 2012 ... PALO ALTO, CA -- (Marketwire) -- 05/02/12 -- Tesla Motors, Inc. (NASDAQ: TSLA) today announced the date and location of its 2012 Annual ..._

**[Tesla Motors Announces 2011 Annual Stockholder Meeting](https://ir.tesla.com/press-release/tesla-motors-announces-2011-annual-stockholder-meeting)**

_Source: ir.tesla.com - Feb 25, 2011 ... PALO ALTO, Calif.--(BUSINESS WIRE)-- Tesla Motors, Inc. (Nasdaq: TSLA) announced today that its 2011 annual meeting of stockholders will be ..._

**[Tesla Motors Announces Date for Second Quarter 2012 Financial ...](https://ir.tesla.com/press-release/tesla-motors-announces-date-second-quarter-2012-financial)**

_Source: ir.tesla.com - Jul 19, 2012 ... Tesla Motors, Inc. (NASDAQ: TSLA) announced today that it will post its financial results for the second quarter ended June 30, 2012, after market close on ..._

