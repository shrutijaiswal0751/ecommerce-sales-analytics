# Data Source Strategy

## 1. Objective

This document describes the planned data sources and how data will move through the E-Commerce Sales Analytics pipeline.

## 2. Planned Data Sources

### API

A public practice e-commerce API will be used to learn API-based data ingestion.

Python's `requests` library will retrieve the API response in JSON format.

The selected API and available fields will be verified before implementation.

### CSV Files

CSV files may be used for additional reference data if required, such as customer or product information.

The source, fields, and usage of each CSV file will be documented before it is added to the project.

## 3. Data Pipeline

API / CSV
↓
Python Ingestion
↓
Raw Data Storage
↓
PostgreSQL RAW Layer
↓
STAGING Layer
↓
ANALYTICS Layer
↓
SQL / Python Analysis
↓
Dashboard
↓
Business Insights

## 4. Data Handling Principles

* Preserve the original API response before transformation.
* Keep credentials and secrets outside source code.
* Validate data before using it for analysis.
* Document source limitations and missing fields.
* Do not assume that practice API data represents real business activity.

## 5. Current Status

The data source is planned. The final source fields and ingestion approach will be confirmed after inspecting the selected API response.
