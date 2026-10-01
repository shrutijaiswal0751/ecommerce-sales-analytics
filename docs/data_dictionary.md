# Data Dictionary

## Purpose

This document describes the fields used in the project. The definitions below are provisional and will be updated after the actual API response and database schema are inspected.

## Planned Entities

### Orders

| Column       | Description             | Expected Type   |
| ------------ | ----------------------- | --------------- |
| order_id     | Unique order identifier | Integer or Text |
| customer_id  | Customer identifier     | Integer or Text |
| order_date   | Date of the order       | Date/Timestamp  |
| order_status | Status of the order     | Text            |

### Products

| Column       | Description               | Expected Type   |
| ------------ | ------------------------- | --------------- |
| product_id   | Unique product identifier | Integer or Text |
| product_name | Name of the product       | Text            |
| category     | Product category          | Text            |
| unit_price   | Product price             | Numeric         |

### Customers

| Column        | Description                | Expected Type   |
| ------------- | -------------------------- | --------------- |
| customer_id   | Unique customer identifier | Integer or Text |
| customer_name | Customer name              | Text            |
| region        | Customer region            | Text            |

## Notes

These are planned analytical entities, not confirmed API fields. The dictionary will be updated when the real source structure is known.
