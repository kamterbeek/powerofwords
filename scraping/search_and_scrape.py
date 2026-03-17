from newsapi import NewsApiClient
from newspaper import Article
import pandas as pd

# Initialize API
newsapi = NewsApiClient(api_key="cbce3fd814e241adae414283322013f9")

queries = [
    "Trump Ashli Babbitt",
    "Trump Renee Good"
]

records = []

for query in queries:

    print("\nSearching:", query)

    articles = newsapi.get_everything(
        q=query,
        language="en",
        sort_by="relevancy",
        page_size=20
    )

    for article in articles["articles"]:

        url = article["url"]
        title = article["title"]

        try:

            print("Scraping:", url)

            art = Article(url)
            art.download()
            art.parse()

            text = art.text

            if len(text) > 200:

                records.append({
                    "query": query,
                    "title": title,
                    "url": url,
                    "text": text
                })

        except Exception as e:

            print("Skipping:", e)

            continue


df = pd.DataFrame(records)

df.to_csv("data_raw/articles.csv", index=False)

print("\nArticles collected:", len(df))
