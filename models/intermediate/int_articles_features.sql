SELECT
    id,
    title,

    article_clean,

    -- 📊 Basic NLP features
    LENGTH(article_clean) AS char_count,

    ARRAY_LENGTH(SPLIT(article_clean, ' ')) AS word_count,

    -- avg word length
    SAFE_DIVIDE(
        LENGTH(article_clean),
        ARRAY_LENGTH(SPLIT(article_clean, ' '))
    ) AS avg_word_length,

    -- keyword flags
    REGEXP_CONTAINS(article_clean, r'\bclimate\b') AS has_climate,
    REGEXP_CONTAINS(article_clean, r'\benergy\b') AS has_energy,
    REGEXP_CONTAINS(article_clean, r'\bpolicy\b') AS has_policy

FROM {{ ref('stg_articles') }}