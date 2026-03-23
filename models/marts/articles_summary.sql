SELECT
    query,

    COUNT(*) AS total_articles,

    AVG(word_count) AS avg_word_count,

    AVG(avg_word_length) AS avg_word_length,

    AVG(CASE WHEN has_climate THEN 1 ELSE 0 END) AS pct_climate,
    AVG(CASE WHEN has_energy THEN 1 ELSE 0 END) AS pct_energy,
    AVG(CASE WHEN has_policy THEN 1 ELSE 0 END) AS pct_policy

FROM {{ ref('int_articles_features') }}

GROUP BY query
ORDER BY total_articles DESC