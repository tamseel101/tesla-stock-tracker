import json
import datetime
import os

def update_readme():
    """
    Updates the README.md file with the latest Tesla stock chart and news.
    Handles file reading/writing errors and ensures proper section updates.
    """
    # 1. Load Tesla news data
    tesla_news = []
    try:
        with open("news/tesla_news.json", "r", encoding="utf-8") as f:
            tesla_news = json.load(f)
    except FileNotFoundError:
        print("Error: news/tesla_news.json not found. Cannot update news section.")
    except json.JSONDecodeError:
        print("Error: Could not decode JSON from news/tesla_news.json. File might be corrupted.")
    except Exception as e:
        print(f"An unexpected error occurred while reading news/tesla_news.json: {e}")

    # Prepare the news section content
    news_section = "## Latest Tesla News\n\n"
    if tesla_news:
        for news_item in tesla_news:
            headline = news_item.get('headline', 'N/A')
            link = news_item.get('link', '#')
            source = news_item.get('source', 'N/A')
            date = news_item.get('date', 'N/A')
            news_section += f"**[{headline}]({link})**\n\n"
            news_section += f"_Source: {source} - {date}_\n\n"
    else:
        news_section += "_No recent news available._\n\n"

    # 2. Read existing README.md content
    readme_contents = ""
    readme_path = "README.md"
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            readme_contents = f.read()
    except FileNotFoundError:
        print(f"Error: {readme_path} not found. Creating a new one.")
        # If README.md doesn't exist, start with a basic structure
        readme_contents = "# tesla-stock-tracker\n\n## Tesla Stock Chart\n\n![Tesla Stock Chart](charts/tesla_stock_chart.png)\n\n"
    except Exception as e:
        print(f"An unexpected error occurred while reading {readme_path}: {e}")
        return # Exit if we can't read the README

    # 3. Update the stock chart and prepare new content for README
    lines = readme_contents.split("\n")
    new_readme_contents_parts = []
    chart_updated = False
    news_section_reached = False

    for line in lines:
        if line.startswith("![Tesla Stock Chart](") and not chart_updated:
            # Update the chart image URL with a timestamp to bust cache
            timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            new_readme_contents_parts.append(f"![Tesla Stock Chart](charts/tesla_stock_chart.png?{timestamp})")
            chart_updated = True
        elif line.startswith("## Latest Tesla News"):
            # Stop adding lines from old README once news section is reached
            news_section_reached = True
            break
        else:
            new_readme_contents_parts.append(line)
    
    # Join parts and add updated news section
    new_readme_contents = "\n".join(new_readme_contents_parts) + "\n\n" + news_section

    # If chart section was not found, add it to the top (basic fallback)
    if not chart_updated and "## Tesla Stock Chart" not in new_readme_contents:
        new_readme_contents = "# tesla-stock-tracker\n\n## Tesla Stock Chart\n\n" \
                              f"![Tesla Stock Chart](charts/tesla_stock_chart.png?{datetime.datetime.now().strftime('%Y%m%d%H%M%S')})\n\n" \
                              + new_readme_contents

    # 4. Write the updated content back to README.md
    try:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_readme_contents)
        print(f"Successfully updated {readme_path}")
    except IOError as e:
        print(f"Error writing to {readme_path}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while writing to {readme_path}: {e}")

if __name__ == "__main__":
    update_readme()
