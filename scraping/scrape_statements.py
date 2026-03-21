import requests
from bs4 import BeautifulSoup
import pandas as pd

keywords = ["Ashli Babbitt", "Renee Good"]

urls = ["https://www.presidency.ucsb.edu/documents/trump-twitter-archive"]

records = []

for url in urls:
  
    print("Scraping:", url)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = soup.find_all("p")

    print("Paragraphs found:", len(paragraphs))

    for p in paragraphs:

        text = p.get_text()

        for keyword in keywords:

            if keyword.lower() in text.lower():

                 print("MATCH:", text)

                 records.append({
                     "source_url": url,
                     "keyword": keyword,
                     "text": text
                 })
              

df = pd.DataFrame(records)

df.to_csv("data_raw/statements.csv", index=False)

print("Records found:", len(records))
print("Scraping complete:")
