SELECT
    DATE(published_date) AS date,

    COUNT(*) AS total_articles,

    AVG(word_count) AS avg_word_count,

    SUM(CASE WHEN has_climate THEN 1 ELSE 0 END) AS climate_articles,
    SUM(CASE WHEN has_energy THEN 1 ELSE 0 END) AS energy_articles,
    SUM(CASE WHEN has_policy THEN 1 ELSE 0 END) AS policy_articles

FROM {{ ref('int_articles_features') }}

GROUP BY 1
ORDER BY 1 