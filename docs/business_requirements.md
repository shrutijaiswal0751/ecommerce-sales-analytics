# Business Requirements — E-Commerce Sales Analytics

## 1. Business Background

An e-commerce business generates data from orders, customers, products, payments, and sales activities. Analyzing this data can help stakeholders understand business performance and identify areas for improvement.

## 2. Business Objective

The objective is to analyze e-commerce sales data and provide reliable metrics and insights about revenue, products, customers, regions, and order status.

## 3. Stakeholders

* Sales Manager
* Product Manager
* Business Manager
* Senior Management

## 4. Business Questions

### Sales

* What is the total revenue?
* How many orders were placed?
* What is the monthly revenue trend?
* What is the average order value?

### Products

* Which products generate the highest revenue?
* Which categories perform well?
* Which products have low sales?

### Customers

* How many unique customers placed orders?
* Which customers generate the highest revenue?
* How frequently do customers place orders?

### Regions

* Which regions generate the most revenue?
* How does sales performance vary by region?

### Orders and Payments

* What is the distribution of order statuses?
* Which payment methods are most commonly used?
* What percentage of orders are cancelled?

## 5. Planned KPIs

* Total Revenue
* Total Orders
* Unique Customers
* Average Order Value (AOV)
* Cancellation Rate
* Monthly Revenue Growth

Profit and profit margin will only be calculated if the selected source provides reliable cost or profit data.

## 6. Project Scope

### In Scope

* API and CSV ingestion
* Raw data preservation
* Data quality validation
* Data cleaning and transformation
* PostgreSQL database
* SQL analysis
* Exploratory data analysis
* KPI development
* Tableau dashboard
* Business insights
* Pipeline automation

### Out of Scope

* Processing real customer payments
* Building a customer-facing e-commerce application
* Production payment infrastructure

## 7. Success Criteria

* Data can be collected from documented sources.
* Original raw data is preserved.
* Data quality checks are implemented.
* Clean data is available for analysis.
* SQL queries answer the business questions.
* KPIs and dashboard are documented.
* The pipeline can be rerun using documented instructions.
