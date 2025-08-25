import os
import json
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# NOTE: It is highly recommended to store API keys in environment variables
# rather than directly in the code for security reasons.
API_KEY = os.getenv("GOOGLE_API_KEY")  # Read from environment variable
CX = os.getenv("GOOGLE_CX")  # Read from environment variable

def fetch_tesla_news():
    """
    Fetches the latest Tesla news using the Google Custom Search API and saves it to a JSON file.
    Includes error handling for network issues, API errors, and unexpected response formats.
    """
    if not API_KEY or not CX:
        print("Warning: GOOGLE_API_KEY or GOOGLE_CX environment variable not set. Skipping live news fetch.")
        # If no API keys, check if a news file already exists to avoid errors in subsequent steps
        if not os.path.exists("news/tesla_news.json"):
            print("No existing news data file found. Creating an empty JSON file.")
            os.makedirs("news", exist_ok=True)
            with open("news/tesla_news.json", "w", encoding="utf-8") as f:
                json.dump([], f, indent=4) # Write an empty JSON array
        return # Exit the function, as we cannot fetch live news

    query = "tesla news"
    url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX}&q={query}&num=10'

    try:
        response = requests.get(url, timeout=10) # Added timeout for robustness
        response.raise_for_status() # Raises HTTPError for bad responses (4xx or 5xx)
        data = response.json()

    except requests.exceptions.Timeout:
        print("Error: Request to Google Custom Search API timed out.")
        return
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news from Google Custom Search API: {e}")
        return
    except json.JSONDecodeError:
        print("Error: Could not decode JSON response from Google Custom Search API.")
        print(f"Response content: {response.text[:500]}...") # Print first 500 chars of response
        return
    except Exception as e:
        print(f"An unexpected error occurred during news fetching: {e}")
        return

    # Removed print("Response data:", data) as it's for debugging

    if 'items' not in data:
        print("Error: 'items' key not found in the API response data. No news articles found or API structure changed.")
        if 'error' in data:
            print(f"API Error details: {data['error']}")
        return

    tesla_news = []
    for item in data['items']:
        # Safely get item details, providing default values if a key is missing
        headline = item.get('title', 'N/A')
        source = item.get('displayLink', 'N/A')
        # The 'snippet' often contains the date and a description, taking it as is for now.
        date_snippet = item.get('snippet', 'N/A')
        link = item.get('link', '#')

        tesla_news.append({"headline": headline, "source": source, "date": date_snippet, "link": link})

    os.makedirs("news", exist_ok=True)
    try:
        with open("news/tesla_news.json", "w", encoding="utf-8") as f:
            json.dump(tesla_news, f, indent=4)
        print(f"Successfully saved {len(tesla_news)} news articles to news/tesla_news.json")
    except IOError as e:
        print(f"Error writing news data to file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while saving news: {e}")

if __name__ == "__main__":
    fetch_tesla_news()
