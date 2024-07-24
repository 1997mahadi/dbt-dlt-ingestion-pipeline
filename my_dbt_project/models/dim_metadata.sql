-- models/dim_metadata.sql
{{ config(
    materialized='table'
) }}

SELECT
    ROW_NUMBER() OVER () AS metadata_id,
    start_date,
    end_date,
    timeframe
FROM {{ ref('metadata') }}
