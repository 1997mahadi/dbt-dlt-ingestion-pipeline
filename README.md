# DBT-DLT Ingestion Pipeline


## 📍 Overview

Welcome to the dbt-DLT Ingestion Pipeline project! This project leverages dlt (Data Loading Tool) to provide a robust and scalable data ingestion pipeline. dlt simplifies the process of loading data from various sources into data warehouses, making it ideal for Python developers and data engineers.

The primary objective of this project is to streamline the ingestion, transformation, and analysis of cryptocurrency trading data using dbt (data build tool) and DuckDB. By leveraging dbt, we aim to provide a robust and scalable ETL (Extract, Transform, Load) pipeline that ensures data quality and consistency across your analytical workflows.

This project specifically focuses on ingesting and analyzing cryptocurrency trading data from Alpaca. The data includes detailed trading information such as open, high, low, close prices, and volume for various cryptocurrency trading pairs.

### 🔑 Key Points

- **Robust and Scalable**: Designed to handle large volumes of data efficiently.
- **Simplified Data Loading**: Easy integration with modern data stacks and seamless data ingestion process.
- **Data Quality and Consistency**: Ensures high-quality data through robust ETL processes.

This project is tailored for data professionals seeking to enhance their data ingestion and transformation processes, ensuring efficient and reliable data handling for analytical purposes.


![Diagram](images/diagram5.png)

## 🎯Purpose

The primary purpose of this project is to facilitate the efficient ingestion and transformation of cryptocurrency trading data, making it accessible and insightful for data analysis and reporting. Given the rapid rise in popularity and complexity of cryptocurrencies, having a reliable and scalable data pipeline is essential for making informed decisions based on accurate and up-to-date market data. This project aims to empower data professionals with the tools needed to transform raw trading data into actionable insights.


##  🌟Key Features

- **Automated Data Ingestion**: Seamlessly fetch cryptocurrency trading data from Alpaca API.
- **Dimensional Modeling**: Organize data into fact and dimension tables for efficient querying and reporting.
- **Data Quality Assurance**: Implement robust data quality tests to ensure data integrity.
- **Documentation**: Comprehensive documentation of data models for better understanding and maintenance.
- **Integration with DuckDB**: Utilize DuckDB for efficient data storage and retrieval.
- **Seamless Integration**: Compatible with modern data stacks (AWS, Google BigQuery, Snowflake, etc.).
- **Community-Driven**: Leverage dltHub for sharing solutions and code snippets.
- **Open-Source and Customizable**: Fully customizable to fit specific project needs.

## 📦Why Use dlt?

- **Pythonic Data Ingestion**: Easy integration with Python tools and environments.
- **Scalable**: Suitable for both small projects and large enterprises.
- **Data Lineage**: Track and manage data lineage effectively.



## 📂 Repository Structure

\``plaintext
├── README.md
├── alpaca_crypto.duckdb
├── dlt_pipeline
│   ├── README.md
│   ├── alpaca_crypto.duckdb
│   ├── alpaca_crypto_dlt_pipeline.py
│   ├── crypto_data_dlt
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── exceptions.py
│   │   ├── helpers.py
│   │   ├── schemas.py
│   │   └── settings.py
│   └── schemas
│       └── export
├── logs
│   └── dbt.log
├── my_dbt_project
│   ├── README.md
│   ├── analyses
│   ├── dbt_project.yml
│   ├── logs
│   │   └── dbt.log
│   ├── macros
│   ├── models
│   │   ├── clean_crypto_data.sql
│   │   ├── crypto_data.sql
│   │   ├── dim_metadata.sql
│   │   ├── dim_symbols.sql
│   │   ├── dim_time.sql
│   │   ├── distinct_symbols.sql
│   │   ├── fact_crypto_prices.sql
│   │   ├── fact_purchases.sql
│   │   ├── metadata.sql
│   │   ├── purchases.sql
│   │   ├── schema.yml
│   │   └── timestamps.sql
│   ├── profiles.yml
│   ├── seeds
│   ├── snapshots
│   ├── target
│   │   ├── catalog.json
│   │   ├── compiled
│   │   ├── graph.gpickle
│   │   ├── graph_summary.json
│   │   ├── index.html
│   │   ├── manifest.json
│   │   ├── partial_parse.msgpack
│   │   ├── run
│   │   ├── run_results.json
│   │   └── semantic_manifest.json
│   └── tests
├── requirements.txt
└── scripts
    └── explore_duckdb.py
\``

---

## 🧩 Modules

This project is organized to maintain clear separation of concerns and enhance maintainability. Each module handles a distinct part of the data pipeline. Below is an overview of each module:

### ➡️ Data Ingestion

**Overview**: This module handles the extraction and loading of cryptocurrency trading data from the Alpaca API using DLT.

**Folder**: `dlt_pipeline`

**Files**:
- `alpaca_crypto_dlt_pipeline.py`: Main script for extracting and loading cryptocurrency data.
- `crypto_data_dlt/`: Contains supporting scripts and configurations.
  - `__init__.py`: Initialization script.
  - `exceptions.py`: Custom exceptions for error handling.
  - `helpers.py`: Utility functions.
  - `schemas.py`: Schema definitions for data validation.
  - `settings.py`: Configuration settings.

### ➡️ Data Transformation

**Overview**: Utilizes dbt (data build tool) and DuckDB for transforming and modeling the ingested data.

**Folder**: `my_dbt_project`

**Files**:
- `dbt_project.yml`: dbt project configuration.
- `models/`: Contains dbt models for various stages of data transformation.
  - `clean_crypto_data.sql`: Cleaning script for crypto data.
  - `crypto_data.sql`: Raw crypto data model.
  - `dim_metadata.sql`: Dimension table for metadata.
  - `dim_symbols.sql`: Dimension table for symbols.
  - `dim_time.sql`: Dimension table for time.
  - `distinct_symbols.sql`: Model for distinct symbols.
  - `fact_crypto_prices.sql`: Fact table for crypto prices.
  - `fact_purchases.sql`: Fact table for purchases.
  - `metadata.sql`: Model for metadata.
  - `purchases.sql`: Model for purchase data.
  - `schema.yml`: Defines the schema and data quality tests.
  - `timestamps.sql`: Model for timestamps.

### ➡️ Utility Scripts

**Overview**: Contains additional scripts for data exploration and validation.

**Folder**: `scripts`

**Files**:
- `explore_duckdb.py`: Script to explore and validate data in DuckDB.

### ➡️ Configuration and Logs

**Overview**: Manages project dependencies, configurations, and logs.

**Files**:
- `requirements.txt`: Lists the dependencies needed for the project.
- `logs/`: Directory for log files.
  - `dbt.log`: Log file for dbt operations.


## Community and Support

Join the dltHub community for support and collaboration: [dltHub](https://dlthub.com)
