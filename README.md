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

![Tesla Stock Chart](charts/tesla_stock_chart.png?20261008200153)

























































































































































































































































































































































































































## Latest Tesla News

**[Tesla Motors Receives $40 Million Financing Commitment](https://ir.tesla.com/press-release/tesla-motors-receives-40-million-financing-commitment)**

_Source: ir.tesla.com - Nov 2, 2008 ... The financing will be used primarily to accelerate manufacturing of the Tesla Roadster, an all-electric, high performance sports car. In ..._

**[Tesla Motors Announces 2012 Annual Shareholder Meeting](https://ir.tesla.com/press-release/tesla-motors-announces-2012-annual-shareholder-meeting)**

_Source: ir.tesla.com - May 2, 2012 ... PALO ALTO, CA -- (Marketwire) -- 05/02/12 -- Tesla Motors, Inc. (NASDAQ: TSLA) today announced the date and location of its 2012 Annual ..._

**[Tesla Motors Announces Major European Distribution Center in the ...](https://ir.tesla.com/press-release/tesla-motors-announces-major-european-distribution-center)**

_Source: ir.tesla.com - Dec 12, 2012 ... The new Tesla European Distribution Center will lead to the creation of approximately 50 jobs in the next few years. Tesla's decision to locate ..._

**[Tesla Motors Launches Revolutionary Supercharger Enabling ...](https://ir.tesla.com/press-release/tesla-motors-launches-revolutionary-supercharger-enabling)**

_Source: ir.tesla.com - Sep 24, 2012 ... The Supercharger is substantially more powerful than any charging technology to date, providing almost 100 kilowatts of power to the Model S, ..._

**[Press Releases | Tesla Investor Relations](https://ir.tesla.com/press)**

_Source: ir.tesla.com - Sep 29, 2026. Please find below the latest company-compiled delivery consensus of sell-side analysts. Tesla does not endorse any information, recommendations or ..._

**[Tesla Investor Relations](https://ir.tesla.com/)**

_Source: ir.tesla.com - Tesla's mission is to accelerate the world's transition to sustainable energy. Today, Tesla builds not only all-electric vehicles but also infinitely ..._

**[Tesla Motors Releases Fourth Quarter & Full Year 2011 Financial ...](https://ir.tesla.com/press-release/tesla-motors-releases-fourth-quarter-full-year-2011-financial)**

_Source: ir.tesla.com - Feb 15, 2012 ... Tesla has delivered more than 2,150 Roadsters, the world's first electric sports car, to customers world-wide. Model S, the first premium sedan ..._

**[Tesla Motors to Officially Open Tesla Factory - Home of the Model S](https://ir.tesla.com/press-release/tesla-motors-officially-open-tesla-factory-home-model-s)**

_Source: ir.tesla.com - Oct 26, 2010 ... Tesla officially unveils the Tesla Factory in Fremont, CA. The former NUMMI factory closed in April 2010. Tesla purchased the factory in May to ..._

**[Tesla Motors and Toyota Motor Corporation Intend to Work Jointly ...](https://ir.tesla.com/press-release/tesla-motors-and-toyota-motor-corporation-intend-work-jointly-ev)**

_Source: ir.tesla.com - May 19, 2010 ... The two companies intend to form a specialist team to further those efforts. TMC has agreed to purchase $50 million of Tesla's common stock ..._

**[Tesla Motors Selects BorgWarner for Production of New Gearbox for ...](https://ir.tesla.com/press-release/tesla-motors-selects-borgwarner-production-new-gearbox-tesla)**

_Source: ir.tesla.com - Sep 8, 2008 ... The new powertrain achieves an EPA combined range of 244 miles on a single charge, up from Tesla's previously announced EPA range of 221 miles._

