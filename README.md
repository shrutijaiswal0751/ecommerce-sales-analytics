# E-Commerce Sales Analytics

An end-to-end data analytics project that collects product data from an API, cleans and transforms it using Python, stores it in PostgreSQL, analyzes it using SQL, and visualizes key metrics in Power BI.

## Project Overview

This project demonstrates a practical data analytics workflow using e-commerce product catalogue data. It focuses on data ingestion, data cleaning, exploratory data analysis (EDA), SQL-based analysis, and interactive dashboard development.

## Business Objectives

- Analyze product pricing and discount patterns.
- Identify product distribution across categories.
- Compare product stock levels across categories.
- Monitor product ratings and availability status.
- Build an interactive dashboard for exploring product data.
- Present useful observations through data visualizations.

## Technology Stack

- **Python:** Data ingestion and transformation
- **Pandas and NumPy:** Data cleaning and analysis
- **Requests:** API data collection
- **PostgreSQL:** Data storage
- **SQL:** Business analysis and querying
- **Matplotlib and Seaborn:** Exploratory data visualization
- **Jupyter Notebook:** Interactive analysis
- **Power BI:** Interactive dashboard development
- **Git and GitHub:** Version control and project documentation

## Data Source

Product data is collected from the DummyJSON Products API.

The dataset includes fields such as product title, category, price, discount percentage, rating, stock, brand, and availability status.

**Note:** The current dataset contains 30 product records from the API response used in this project. It represents product catalogue data, not actual customer orders or sales transactions.

## Project Workflow

1. Collect product data from the API.
2. Inspect and validate the raw data.
3. Clean and transform data using Python.
4. Handle missing brand values.
5. Store and query data in PostgreSQL.
6. Perform SQL-based analysis.
7. Conduct exploratory data analysis (EDA).
8. Develop KPIs and interactive visualizations in Power BI.
9. Document project findings and insights.

## Power BI Dashboard

The dashboard contains two report pages:

### Page 1 — Product Overview

- Total Products
- Total Stock
- Average Price
- Average Rating
- Average Discount
- Products by Category
- Availability Status
- Stock by Category

### Page 2 — Product and Pricing Analysis

- Price vs. Rating analysis
- Average Price by Category
- Average Rating by Category
- Average Discount by Category

### Dashboard Screenshots

**Page 1 — Product Overview**

![Power BI Dashboard - Page 1](image/Dashboard_page1.png)

**Page 2 — Product and Pricing Analysis**

![Power BI Dashboard - Page 2](image/Dashboard_page2.png)

## Key Metrics

The current dataset produces the following dashboard metrics:

| Metric | Value |
|---|---:|
| Total Products | 30 |
| Total Stock | 1,648 |
| Average Price | ₹219.25 |
| Average Rating | 3.86 |
| Average Discount | 9.84% |

*These values describe the current product dataset and may change if the data is refreshed.*

## Key Learnings

- Collecting data from a REST API using Python.
- Cleaning and transforming data with Pandas.
- Working with PostgreSQL and SQL queries.
- Performing exploratory data analysis.
- Building KPI cards, charts, and slicers in Power BI.
- Designing a multi-page dashboard with report navigation.
- Documenting an analytics project using GitHub.

## Project Structure

```text
Sales-analytics/
├── data/
│   └── raw/
├── docs/
├── notebook/
│   └── 01_eda_products.ipynb
├── image/
│   ├── dashboard_page1.png
│   └── dashboard_page2.png
├── sql/
│   └── 01_business_analysis.sql
├── src/
│   ├── ingestion/
│   └── cleaned/
├── .gitignore
├── README.md
└── requirements.txt
```
*The folder structure above should match the actual files in your repository; adjust it if your folders differ.*

## Key Insights

Based on the analysis of 30 product records:

- **Product Distribution:** Groceries is the largest category, with 15 products, representing 50% of the dataset.
- **Pricing Analysis:** Furniture has the highest average price at ₹1,199.99, while groceries has the lowest average price at ₹6.04.
- **Stock Analysis:** Groceries has the highest total stock at 731 units, accounting for approximately 44.4% of the total stock.
- **Rating Analysis:** Furniture has the highest average product rating at 4.01 out of 5.
- **Discount Analysis:** Beauty products have the highest average discount at 12.42%.
- **Category Comparison:** The dataset shows differences in pricing, stock levels, ratings, and discounts across the four product categories.

*These findings describe the current product catalogue dataset and do not represent actual sales, revenue, or customer purchasing behavior.*

## Key Insights

Based on the analysis of 30 products, the following insights were identified:

- **Largest Category:** Groceries has 15 products, representing 50% of the dataset.
- **Highest Average Price:** Furniture has the highest average price at ₹1,199.99.
- **Lowest Average Price:** Groceries has the lowest average price at ₹6.04.
- **Highest Total Stock:** Groceries has 731 units in stock, approximately 44.4% of the total stock.
- **Highest Average Rating:** Furniture has the highest average product rating of 4.01 out of 5.
- **Highest Average Discount:** Beauty products have the highest average discount at 12.42%.

### Business Observations

- The furniture category has significantly higher average prices than the other categories.
- Groceries contribute the largest share of products and available stock in the dataset.
- Average ratings and discounts vary across product categories.

**Note:** These insights describe the available product catalogue data. They do not represent actual sales, revenue, or customer purchasing behaviour.

## Future Improvements

- Implement API pagination to collect more product records.
- Automate data ingestion and refresh.
- Add data quality checks and validation.
- Expand SQL analysis and documentation.
- Improve dashboard insights and reporting.

## Author

**Shruti**

Aspiring Data Analyst | Python | SQL | PostgreSQL | Power BI | Excel
