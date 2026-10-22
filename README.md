# E-Commerce Product Analytics

An end-to-end data analytics project that collects product catalogue data from an API, cleans and transforms it using Python, stores it in PostgreSQL, analyzes it with SQL, and presents the results through an interactive Power BI dashboard.

## Project Overview

This project demonstrates a practical data analytics workflow using Python, Pandas, PostgreSQL, SQL, and Power BI.

The pipeline covers API data ingestion, data cleaning, transformation, database loading, SQL analysis, dashboard development, and execution logging.

**Important:** The data source contains product catalogue information, not actual customer orders or transactions. Therefore, the current project focuses on product prices, ratings, discounts, stock levels, and categories rather than actual sales revenue.

## Business Objectives

- Collect product data from an external API.
- Clean and validate raw data.
- Transform data into an analysis-ready format.
- Store processed data in PostgreSQL.
- Analyze product categories, prices, ratings, discounts, and stock.
- Build an interactive Power BI dashboard.
- Automate pipeline execution and maintain execution logs.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data ingestion and pipeline orchestration |
| Requests | API communication |
| Pandas | Data cleaning and transformation |
| NumPy | Numerical operations |
| PostgreSQL | Structured data storage |
| SQL | Data querying and analysis |
| Power BI | Interactive dashboard and visualizations |
| Jupyter Notebook | Exploratory data analysis |
| Git and GitHub | Version control and project hosting |
| Windows Task Scheduler | Scheduled pipeline execution |
| Python Logging | Execution logs and error tracking |
| VS Code | Development environment |

## Data Source

**Source:** DummyJSON Products API

**Endpoint:** https://dummyjson.com/products

The API provides the following product attributes:

- Product ID
- Product title
- Category
- Price
- Discount percentage
- Rating
- Stock
- Brand
- Availability status

The current pipeline processes 30 product records per configured API request. Pagination is a planned improvement for retrieving the complete product catalogue.

## Project Workflow

```text
DummyJSON Products API
          |
          v
API Data Ingestion
          |
          v
Raw JSON Storage
          |
          v
Data Cleaning
          |
          v
Data Transformation
          |
          v
PostgreSQL Database
          |
          v
SQL Analysis
          |
          v
Power BI Dashboard
```

The workflow is orchestrated through the Python entry-point script `run_pipeline.py`.

## Automated Data Pipeline

The pipeline runs the existing scripts in sequence:

1. **Data Ingestion:** Fetches product data from the API and saves the raw response.
2. **Data Cleaning:** Cleans product data and checks for duplicate product IDs.
3. **Data Transformation:** Prepares data for analysis and performs data-quality checks.
4. **PostgreSQL Loading:** Loads processed data into the target database table.

Pipeline execution details are recorded in `pipeline.log`, which helps with troubleshooting and reviewing previous runs.

### Latest Recorded Pipeline Test

The latest recorded successful test reported the following results:

| Check | Result |
|---|---:|
| Products processed | 30 |
| Duplicate IDs after cleaning | 0 |
| Duplicate IDs after transformation | 0 |
| Missing values after transformation | 0 |
| CSV rows loaded | 30 |
| Rows in the target PostgreSQL table | 30 |
| Pipeline status | Successful |

These are results from the recorded test and may change when the source data or pipeline changes.

## PostgreSQL Database

**Database:** `ecommerce_analytics`

The project uses two PostgreSQL tables for different analysis workflows.

| Table | Purpose |
|---|---|
| `public.products` | Source table used by the business analysis SQL queries |
| `public.products_transformed` | Table populated by the Python loading script and used for transformed-data analysis |

Both tables were previously verified to contain 30 rows with the same nine product columns:

`id`, `title`, `category`, `price`, `discountpercentage`, `rating`, `stock`, `brand`, and `availabilitystatus`.

### Data Loading

**Script:** `src/database/load_to_postgres.py`

The loading script:

- Reads `data/processed/products_cleaned.csv`.
- Loads database connection settings from `.env`.
- Validates required configuration values.
- Selects the expected product columns.
- Replaces existing rows in `public.products_transformed` with the current CSV data.
- Compares the CSV row count with the database row count.

The current loading approach replaces the existing target-table data rather than maintaining historical records.

## SQL Analysis

The project includes two SQL analysis files.

### 1. Business Analysis

**File:** `sql/01_business_analysis.sql`

This file analyzes the `products` table and includes:

- Overall product KPIs
- Category-wise pricing, ratings, discounts, and stock
- High-discount products with discounts of 20% or more
- Low-stock products with stock below 20
- Highly rated products with ratings of 4 or more
- Product availability summary

### 2. Transformed Data Analysis

**File:** `src/analysis/sales_analysis.sql`

This file analyzes `public.products_transformed` and includes:

- Overall product KPIs
- Category-wise product and stock analysis
- Low-stock products with stock below 50
- Category-wise low-stock counts
- Low-stock percentage calculation

## Power BI Dashboard

The Power BI report contains two pages for exploring product catalogue data through KPI cards, charts, and interactive visualizations.

### Dashboard Page 1

![Power BI Dashboard Page 1](image/Dashboard_page1.png)

### Dashboard Page 2

![Power BI Dashboard Page 2](image/Dashboard_page2.png)

## Key Performance Indicators

The following values were recorded in the current project analysis.

| KPI | Recorded Value |
|---|---:|
| Total Products | 30 |
| Total Stock | 1,648 |
| Average Price | ₹219.25 |
| Average Rating | 3.86 |
| Average Discount | 9.84% |

These values describe the recorded dataset and should be refreshed after the data pipeline runs with updated data.

## Key Analytical Questions

The project explores questions such as:

- Which product categories contain the most products?
- How do product prices vary across categories?
- Which products have higher or lower ratings?
- How are discounts distributed across products?
- Which products have relatively low stock?
- How does product availability vary?
- Are there any missing values or duplicate product IDs?

Specific business conclusions should be based on the latest SQL results and dashboard outputs.

## Data Quality Checks

The pipeline includes checks for:

- Duplicate product IDs
- Missing values after transformation
- Consistency between CSV and database row counts
- Successful completion of pipeline stages

The latest recorded successful test reported no duplicate IDs and no missing values after transformation.

## Project Structure

```text
Sales-analytics/
├── dashboard/
│   └── E-commerce_Mo.pbix
├── data/
│   ├── raw/
│   └── processed/
│       └── products_cleaned.csv
├── docs/
│   ├── business_requirements.md
│   ├── data_dictionary.md
│   └── data_source_strategy.md
├── image/
│   ├── Dashboard_page1.png
│   └── Dashboard_page2.png
├── notebook/
│   └── 01_eda_products.ipynb
├── sql/
│   └── 01_business_analysis.sql
├── src/
│   ├── analysis/
│   │   └── sales_analysis.sql
│   ├── cleaning/
│   │   └── clean_products.py
│   ├── database/
│   │   └── load_to_postgres.py
│   ├── ingestion/
│   │   ├── api_client.py
│   │   └── inspect_raw_data.py
│   └── transformation/
│       └── clean_data.py
├── tests/
├── run_pipeline.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/shrutijaiswal0751/ecommerce-sales-analytics.git
cd ecommerce-sales-analytics
```

### 2. Create and Activate a Virtual Environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a local `.env` file in the project root directory.

Use the following example and replace the placeholder values with your own local PostgreSQL settings:

```dotenv
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ecommerce_analytics
DB_USER=your_postgres_username
DB_PASSWORD=your_postgres_password
```

Do not commit your real `.env` file, database passwords, or other secrets to GitHub. Check the project scripts for any additional configuration variables they require.

### 5. Configure PostgreSQL

- Ensure PostgreSQL is installed and running.
- Create the `ecommerce_analytics` database.
- Configure the connection settings in `.env`.
- Ensure the required target table, `public.products_transformed`, exists with the expected columns before running the loader.

### 6. Run the Pipeline

From the project root, activate the virtual environment and execute:

```powershell
python run_pipeline.py
```

Review the terminal output and `pipeline.log` to check whether all pipeline stages completed successfully.

## Windows Task Scheduler

The pipeline has been configured in Windows Task Scheduler for daily execution at **9:00 AM**.

The task was manually tested using the Task Scheduler's **Run** option, with a reported Last Run Result of `0x0`. Automatic execution at the next scheduled time still needs to be verified independently.

### How to Verify a Scheduled Run

1. Open Windows Task Scheduler.
2. Locate the configured project pipeline task.
3. Check its Last Run Time and Last Run Result.
4. Open `pipeline.log` in the project folder.
5. Confirm that the latest execution completed successfully.

## What I Learned

- Working with a REST API using Python.
- Organizing ingestion, cleaning, transformation, and database loading scripts.
- Performing data-quality checks using Pandas.
- Loading structured data into PostgreSQL.
- Writing SQL queries for product analysis.
- Building an interactive Power BI dashboard.
- Orchestrating pipeline stages using Python.
- Recording execution details and errors using logging.
- Configuring a Windows scheduled task.
- Managing a project with Git and GitHub.

## Future Improvements

- Implement API pagination to retrieve the complete product catalogue.
- Add automated data-quality tests.
- Improve database upsert and historical data handling.
- Document findings from actual SQL query results.
- Configure and verify automated Power BI dataset refresh.
- Add pipeline monitoring and failure notifications.
- Extend the analysis when genuine order and transaction data becomes available.

## Author

**Shruti Jaiswal**

Aspiring Data Analyst | Python | SQL | PostgreSQL | Power BI

GitHub: [shrutijaiswal0751](https://github.com/shrutijaiswal0751)
