WITH source AS (

    SELECT *
    FROM {{ source('raw', 'raw_data') }}

),

cleaned AS (

    SELECT
        -- search query used to find the article
        TRIM(query) AS query,

        -- title cleanup
        TRIM(title) AS title,

        -- URL cleanup
        TRIM(url) AS url,

        -- raw text (preserved)
        IFNULL(text, '') AS article_raw,

        -- normalized text for NLP
        LOWER(IFNULL(text, '')) AS article_lower,

        -- remove extra whitespace (line breaks, tabs, etc.)
        REGEXP_REPLACE(IFNULL(text, ''), r'\s+', ' ') AS article_clean,

        -- remove problematic quotes
        REGEXP_REPLACE(IFNULL(text, ''), r'[\"“”]', '') AS article_no_quotes,

        -- basic metrics (useful later)
        LENGTH(IFNULL(text, '')) AS char_count,

        ARRAY_LENGTH(SPLIT(REGEXP_REPLACE(IFNULL(text, ''), r'\s+', ' '), ' ')) AS word_count

    FROM source

)

SELECT
    query,
    title,
    url,

    article_clean,
    article_lower,
    article_raw,

    char_count,
    word_count

FROM cleaned