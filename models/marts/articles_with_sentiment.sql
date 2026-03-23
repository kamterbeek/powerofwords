SELECT
    f.*,
    s.sentiment,
    s.sentiment_label

FROM {{ ref('int_articles_features') }} f
LEFT JOIN `cognitivelinguisticspolitcs.power_of_words.article_sentiment` s
USING (url)