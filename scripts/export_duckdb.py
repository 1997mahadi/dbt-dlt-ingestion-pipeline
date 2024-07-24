import duckdb
import pandas as pd

# Connect to the DuckDB database
con = duckdb.connect('/workspaces/dbt-dlt-ingestion-pipeline/dlt_pipeline/alpaca_crypto.duckdb')

# List of tables to export
tables_to_export = ['clean_crypto_data', 'crypto_data', 'dim_metadata', 'dim_symbols', 'dim_time', 'distinct_symbols', 'fact_crypto_prices', 'fact_purchases', 'metadata', 'purchases', 'timestamps']

# Fetch existing tables
existing_tables = [table[0] for table in con.execute("PRAGMA show_tables").fetchall()]

# Export each table to CSV if it exists
for table in tables_to_export:
    if table in existing_tables:
        df = con.execute(f'SELECT * FROM {table}').fetchdf()
        df.to_csv(f'/workspaces/dbt-dlt-ingestion-pipeline/{table}.csv', index=False)
        print(f"Exported {table} to CSV.")
    else:
        print(f"Table {table} does not exist in the database.")
