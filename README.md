# E-Commerce Sales Analytics

An end-to-end data analytics project that collects product data from an API, cleans and transforms it using Python, loads it into PostgreSQL, and presents insights through an interactive Power BI dashboard.

## Project Overview

This project demonstrates a practical data analytics workflow using Python, Pandas, PostgreSQL, and Power BI. It automates the main data pipeline steps and helps analyze product pricing, ratings, discounts, stock availability, and product categories.

**Important:** The source contains product catalogue data, not actual customer orders or sales transactions. Therefore, the current analysis focuses on product-level metrics rather than real revenue or sales performance.

## Business Objectives

- Collect product data from an external API.
- Clean and validate raw data.
- Transform data into an analysis-ready format.
- Store processed data in PostgreSQL.
- Analyze product prices, ratings, discounts, and stock.
- Build an interactive Power BI dashboard.
- Automate pipeline execution and maintain execution logs.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data ingestion and pipeline orchestration |
| Requests | API communication |
| Pandas | Data cleaning and transformation |
| NumPy | Numerical operations |
| PostgreSQL | Structured data storage and SQL analysis |
| SQL | Data querying and business analysis |
| Power BI | Interactive dashboards and visualizations |
| Jupyter Notebook | Exploratory data analysis |
| Git and GitHub | Version control and project hosting |
| Windows Task Scheduler | Scheduled pipeline execution |
| Python Logging | Pipeline execution logs and error tracking |
| VS Code | Development environment |

## Data Source

**API:** DummyJSON Products API  
**Endpoint:** `https://dummyjson.com/products`

The API provides product information such as:

- Product ID
- Product title
- Category
- Price
- Discount percentage
- Rating
- Stock
- Brand
- Availability status

The pipeline currently processes the 30 product records returned by the configured API request. The API catalogue contains more products, so pagination can be added to retrieve the full catalogue.

## Project Workflow

```text
DummyJSON Products API
          |
          v
API Data Ingestion
          |
          v
Raw Data Storage
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

The workflow is orchestrated through a single Python entry point, `run_pipeline.py`.

## Automated Data Pipeline

The root-level `run_pipeline.py` script runs the existing pipeline stages in sequence:

1. **Data Ingestion:** Fetches product data from the API and saves the raw response.
2. **Data Cleaning:** Cleans product data and checks for duplicate product IDs.
3. **Data Transformation:** Prepares the cleaned data for analysis and checks data quality.
4. **PostgreSQL Loading:** Loads transformed data into the PostgreSQL table.

The pipeline uses subprocess execution to run the existing scripts and captures their output. If a step fails, the pipeline reports the failure rather than silently continuing.

### Pipeline Logging

Execution details are recorded in the root-level `pipeline.log` file.

The log includes:

- Pipeline step start and completion messages
- Script output
- Errors and failed steps
- PostgreSQL loading results
- Overall pipeline completion status

Logging makes it easier to troubleshoot problems and review previous pipeline executions.

### Latest Successful Test

The latest recorded pipeline test completed successfully with the following results:

| Check | Result |
|---|---:|
| Products processed | 30 |
| Duplicate product IDs after cleaning | 0 |
| Duplicate product IDs after transformation | 0 |
| Missing values after transformation | 0 |
| CSV rows loaded into PostgreSQL | 30 |
| Rows in PostgreSQL table | 30 |
| Pipeline status | Successful |

These results represent the latest recorded test, not a guarantee that every future run will return identical data.

## Power BI Dashboard

The Power BI report contains two pages designed to explore product catalogue data.

### Dashboard Page 1

- Product catalogue overview
- Key performance indicators
- Product category analysis
- Product pricing and stock overview

### Dashboard Page 2

- Additional product-level analysis
- Product rating and discount comparisons
- Interactive visual exploration

Dashboard screenshots:

**Page 1**

![Power BI Dashboard Page 1](image/Dashboard_page1.png)

**Page 2**

![Power BI Dashboard Page 2](image/Dashboard_page2.png)

The dashboard is designed to make product-level patterns easier to understand through charts, KPI cards, and interactive filtering.

## Key Metrics

The dashboard includes metrics such as:

| Metric | Reported Value |
|---|---:|
| Products analyzed | 30 |
| Total stock | 1,648 |
| Average product price | ₹219.25 |
| Average product rating | 3.86 |
| Average discount | 9.84% |

These values reflect the dataset used for the reported analysis and may change when the source data changes.

## Key Insights

The project explores questions such as:

- Which product categories contain more products?
- How do product prices vary across categories?
- Which products have higher or lower ratings?
- How are discounts distributed across products?
- Which products have higher stock availability?
- Are there product records that need additional data-quality checks?

Specific business conclusions should be drawn from the latest dashboard and SQL query results rather than assumed from the API structure alone.

## Data Quality Checks

The pipeline includes checks for:

- Duplicate product IDs
- Missing values after transformation
- Consistency between exported CSV rows and database rows
- Successful completion of each pipeline stage

The latest successful test reported no duplicate IDs and no missing values after transformation.

## Project Structure

```text
Sales-analytics/
│
├── src/
│   ├── ingestion/
│   │   └── api_client.py
│   │
│   ├── cleaning/
│   │   └── clean_products.py
│   │
│   ├── transformation/
│   │   └── clean_data.py
│   │
│   └── database/
│       └── load_to_postgres.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebook/
│   └── 01_eda_products.ipynb
│
├── sql/
│   └── 01_business_analysis.sql
│
├── dashboard/
│   └── E-commerce_Mo.pbix
│
├── image/
│   ├── Dashboard_page1.png
│   └── Dashboard_page2.png
│
├── run_pipeline.py
├── pipeline.log
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

Some files and folders may differ depending on the local version of the project. The `.env` file contains configuration values and should not be committed if it contains secrets or private settings.

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

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create or update `.env` with the configuration variables expected by the project scripts.

Do not publish API credentials, database passwords, or other secrets in GitHub. Use placeholder values in public documentation instead of real credentials.

### 5. Configure PostgreSQL

Ensure PostgreSQL is running and that the target database and connection settings match the configuration expected by the loading script.

The pipeline loads transformed product data into the `products_transformed` table in the `ecommerce_analytics` database.

### 6. Run the Complete Pipeline

From the project root directory, activate the virtual environment and run:

```powershell
python run_pipeline.py
```

This executes the ingestion, cleaning, transformation, and PostgreSQL loading stages in sequence.

Review the terminal output and `pipeline.log` to verify the result.

## Windows Task Scheduler

The pipeline has been configured in Windows Task Scheduler to run daily at **9:00 AM**.

The scheduled task was manually tested using the Task Scheduler's **Run** option. The test completed successfully with Last Run Result `0x0`.

The actual automatic execution at the next scheduled time has not yet been independently verified. The task's status and the latest `pipeline.log` should be checked to confirm future scheduled runs.

### To Verify a Run

1. Open Windows Task Scheduler.
2. Locate the configured project pipeline task.
3. Check its **Last Run Time** and **Last Run Result**.
4. Open `pipeline.log` in the project folder.
5. Confirm that the latest execution ends with a successful completion message.

## What I Learned

- Working with a REST API using Python
- Organizing data ingestion, cleaning, transformation, and loading into separate scripts
- Performing data-quality checks with Pandas
- Loading structured data into PostgreSQL
- Writing SQL queries for analysis
- Building an interactive Power BI report
- Orchestrating multiple scripts through Python
- Recording execution details and errors using logging
- Configuring a Windows scheduled task
- Managing a project with Git and GitHub

## Future Improvements

- Add API pagination to retrieve the full product catalogue.
- Add automated data-quality tests.
- Improve database upsert and historical data handling.
- Add database query outputs and documented analytical findings.
- Configure and verify automated Power BI dataset refresh.
- Add pipeline monitoring and clearer failure notifications.
- Expand the analysis when genuine order and transaction data becomes available.

## Author

**Shruti Jaiswal**

Aspiring Data Analyst | Python | SQL | PostgreSQL | Power BI

GitHub: [shrutijaiswal0751](https://github.com/shrutijaiswal0751)
