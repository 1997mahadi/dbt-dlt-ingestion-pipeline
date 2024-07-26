# 🚀 Alpaca Crypto Data Pipeline

## 🌟 Overview

The Alpaca Crypto Data Pipeline project is designed to help you seamlessly ingest, transform, and store cryptocurrency trading data from the Alpaca Crypto API into DuckDB. This pipeline allows you to fetch historical trading data, generate relevant metadata, and simulate purchase data, providing a comprehensive dataset for analysis and reporting.

## 🤔 Why Use This Project?

- **Automated Data Ingestion**: Streamline the process of collecting and storing large volumes of cryptocurrency data.
- **Historical Data Analysis**: Access and analyze historical trading data to make informed decisions.
- **Simulated Purchase Data**: Generate random purchase data to enrich your dataset and support various analytical scenarios.
- **Efficient Data Storage**: Store the collected data in DuckDB, a fast and reliable analytical database.
- **Flexibility and Customization**: Easily configure the data pipeline to fetch data for different cryptocurrencies, date ranges, and timeframes.

## 🔧 Features

- **Fetch Historical Crypto Data**: Retrieve comprehensive cryptocurrency trading data, including open, high, low, close prices, and volume for specified symbols and timeframes.
- **Generate Metadata**: Collect metadata about the data load, such as the date range and involved symbols.
- **Simulate Purchases**: Create random purchase records for specified cryptocurrencies, providing additional data for analysis.
- **Data Storage**: Efficiently store the fetched and generated data in DuckDB for easy access and analysis.

## 📂 Repository Structure


```plaintext
├── README.md
├── alpaca_crypto.duckdb
├── alpaca_crypto_dlt_pipeline.py
├── crypto_data_dlt
│   ├── __init__.py
│   ├── __pycache__
│   ├── exceptions.py
│   ├── helpers.py
│   ├── schemas.py
│   └── settings.py
└── schemas
    └── export

```



## 📋 Usage

### ✅ Prerequisites

- Python 3.7 or higher
- DuckDB
- Required Python packages listed in `requirements.txt`

### 🚀 Running the Pipeline

1. **Clone the repository**:
    ```sh
    git clone https://github.com/1997mahadi/dbt-dlt-ingestion-pipeline.git
    cd dbt-dlt-ingestion-pipeline
    ```

2. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the pipeline**:
    ```sh
    python alpaca_crypto_dlt_pipeline.py
    ```

### ⚙️ Configuration

The pipeline configuration can be customized using the default settings in the `settings.py` file, including start date, end date, timeframe, and symbols.

## 📊 Data Model

The following diagram represents the data model used in this project. Note that the time_dim is optional and is included for flexibility in time-based data divisions, although it may not be necessary for all use cases.
![Diagram](images/diagram2.png)

## 🔚 Conclusion

This project provides a robust and flexible pipeline for ingesting and analyzing cryptocurrency data. By leveraging the Alpaca Crypto API and DuckDB, you can efficiently collect, store, and analyze historical trading data and simulated purchase records. This pipeline is ideal for anyone looking to perform detailed analysis and reporting on cryptocurrency trading activities.

---

Feel free to contribute to the project by forking the repository and submitting pull requests. For any questions or issues, please open an issue on the GitHub repository.

