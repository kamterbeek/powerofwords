import requests
from bs4 import BeautifulSoup
import pandas as pd
from newspaper import Article

queries = [
    "Trump Ashli Babbitt",
    "Trump Renee Good"
]

records = []

for query in queries:

    print("Searching:", query)

    search_url = f"https://www.google.com/search?q={query}&tbm=nws"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(search_url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.select("a")

    for link in links:

        href = link.get("href")

        if href and "http" in href:

            try:

                print("Scraping article:", href)

                article = Article(href)

                article.download()
                article.parse()

                text = article.text

                if len(text) > 200:

                    records.append({
                        "query": query,
                        "url": href,
                        "title": article.title,
                        "text": text
                    })

            except:
                continue

df = pd.DataFrame(records)

df.to_csv("data_raw/articles.csv", index=False)

print("Articles collected:", len(df))
