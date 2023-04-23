import json
import datetime

def update_readme():
    with open("news/tesla_news.json", "r") as f:
        tesla_news = json.load(f)

    news_section = "## Latest Tesla News\n\n"
    for news_item in tesla_news:
        news_section += f"**[{news_item['headline']}]({news_item['link']})**\n\n"
        news_section += f"_Source: {news_item['source']} - {news_item['date']}_\n\n"

    with open("README.md", "r", encoding="ISO-8859-1") as f:
    readme_contents = f.read()

    lines = readme_contents.split("\n")
    new_readme_contents = ""
    for line in lines:
        if line.startswith("![Tesla Stock Chart]("):
            new_readme_contents += f"![Tesla Stock Chart](charts/tesla_stock_chart.png?{datetime.datetime.now().strftime('%Y%m%d%H%M%S')})\n"
        elif line.startswith("## Latest Tesla News"):
            break
        else:
            new_readme_contents += line + "\n"

    new_readme_contents += news_section

    with open("README.md", "w", encoding="ISO-8859-1") as f:
    f.write(new_readme_contents)

if __name__ == "__main__":
    update_readme()
