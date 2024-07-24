import duckdb

# Connect to the DuckDB database
con = duckdb.connect('/workspaces/dbt-dlt-ingestion-pipeline/dlt_pipeline/alpaca_crypto.duckdb')

# List all tables in the main schema
tables = con.execute("PRAGMA show_tables").fetchall()
print("Tables in the main schema:", tables)
