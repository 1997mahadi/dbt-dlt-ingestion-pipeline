# DBT-DLT Ingestion Pipeline Project

This project is designed to build a data ingestion pipeline using DLT and dbt to fetch and transform cryptocurrency data from Alpaca API, and then visualize it using tools like Power BI.

## Project Structure

- `dlt_pipeline`: Contains scripts and configurations for the DLT ingestion pipeline.
- `my_dbt_project`: Contains dbt models, configurations, and tests for data transformation.
- `scripts`: Utility scripts for data exploration and export.

## Prerequisites

- Python 3.10+
-dlt
- dbt 1.8.4
- DuckDB
- Alpaca API access

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/1997mahadi/dbt-dlt-ingestion-pipeline.git
    cd dbt-dlt-ingestion-pipeline
    ```

2. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure your environment variables for Alpaca API.

4. Run the DLT pipeline to ingest data:
    ```bash
    python dlt_pipeline/alpaca_crypto_dlt_pipeline.py
    ```

5. Transform data using dbt:
    ```bash
    cd my_dbt_project
    dbt run
    ```

6. Explore data:
    ```bash
    cd scripts
    python explore_duckdb.py
    ```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
