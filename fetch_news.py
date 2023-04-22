import os
import json
import requests
from datetime import datetime, timedelta

API_KEY = 'AIzaSyAvqtbgkrt_UVjpzr_eBtdzZTd4Sqcn9v4'
CX = 'f2fbdfcd73fda4a7d'

def fetch_tesla_news():
    query = "tesla news"
    url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX}&q={query}&num=10'
    response = requests.get(url)
    data = response.json()

    print("Response data:", data)  # Add this line to print the response

    # Make sure 'items' key exists in the response data
    if 'items' not in data:
        print("Error: 'items' key not found in the response data")
        return

    tesla_news = []

    for item in data['items']:
        headline = item['title']
        source = item['displayLink']
        date = item['snippet']
        link = item['link']

        tesla_news.append({"headline": headline, "source": source, "date": date, "link": link})

    os.makedirs("news", exist_ok=True)
    with open("news/tesla_news.json", "w") as f:
        json.dump(tesla_news, f)

if __name__ == "__main__":
    fetch_tesla_news()
