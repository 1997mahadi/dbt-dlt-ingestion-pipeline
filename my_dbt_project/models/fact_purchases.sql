{{ config(
    materialized='table'
) }}

with symbol_mapping as (
    select
        symbol,
        symbol_id
    from {{ ref('dim_symbols') }}
)

select
    p.purchase_id,
    p.symbol,
    p.amount,
    p.price,
    p.purchase_date,
    s.symbol_id
from {{ ref('purchases') }} p
join symbol_mapping s on p.symbol = s.symbol
