import duckdb

# Connect to the DuckDB database
con = duckdb.connect(database='/workspaces/dbt-dlt-ingestion-pipeline/dlt_pipeline/alpaca_crypto.duckdb', read_only=True)

# List all schemas in the database
schemas = con.execute("SELECT schema_name FROM information_schema.schemata").fetchall()
print("Schemas in the database:", schemas)

# List all tables in the main schema
tables = con.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='main'").fetchall()
print("Tables in the main schema:", tables)

# Function to preview data from a table
def preview_table(schema_name, table_name, num_rows=5):
    query = f"SELECT * FROM {schema_name}.{table_name} LIMIT {num_rows}"
    df = con.execute(query).fetchdf()
    print(f"\nPreview of table {schema_name}.{table_name}:")
    print(df)

# Preview data from each table in the main schema
for table in tables:
    table_name = table[0]
    preview_table('main', table_name)
