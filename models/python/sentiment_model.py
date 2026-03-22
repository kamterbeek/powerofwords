def model(dbt, session):
    """
    dbt Python model: sentiment analysis on article text
    """

    # Config
    dbt.config(
        materialized="table"
    )

    # Imports (inside function for dbt execution)
    from textblob import TextBlob
    import pandas as pd

    # Load data from your staging model
    df = dbt.ref("stg_articles").to_pandas()

    # Ensure text column is safe
    df["article_clean"] = df["article_clean"].fillna("").astype(str)

    # Apply sentiment analysis
    df["sentiment"] = df["article_clean"].apply(
        lambda x: TextBlob(x).sentiment.polarity
    )

    # classify sentiment
    def classify_sentiment(score):
        if score > 0:
            return "positive"
        elif score < 0:
            return "negative"
        else:
            return "neutral"

    df["sentiment_label"] = df["sentiment"].apply(classify_sentiment)

    # additional features
    df["word_count"] = df["article_clean"].apply(lambda x: len(x.split()))
    df["char_count"] = df["article_clean"].apply(len)

    # Select final columns (keep things clean)
    result = df[[
        "id",
        "title",
        "article_clean",
        "sentiment",
        "sentiment_label",
        "word_count",
        "char_count"
    ]]

    return result