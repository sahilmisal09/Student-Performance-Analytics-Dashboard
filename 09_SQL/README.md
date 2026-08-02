# SQL Scripts

## Overview

This folder contains the Microsoft SQL Server (MSSQL) scripts used for the **Student Performance Analytics Dashboard** project.

The primary objective of these scripts is to demonstrate SQL proficiency in business data analysis, data validation, and stakeholder reporting. While the Power BI dashboards in this project are built using curated CSV datasets generated through a Python ETL pipeline, SQL Server was used as an additional analytical layer to validate data quality and answer business questions.

---

## SQL Environment

- **Database:** StudentPerformanceAnalytics
- **Database Management System:** Microsoft SQL Server 2022 Express
- **SQL Client:** SQL Server Management Studio (SSMS)

---

## Folder Structure

```
SQL/
│
├── 01_Create_Database.sql
├── 02_Business_Queries.sql
├── 03_Data_Validation_Queries.sql
└── README.md
```

---

## Files Description

### 01_Create_Database.sql

Creates the SQL Server database used for the project.

**Purpose**

- Create the project database
- Prepare the environment for importing datasets

---

### 02_Business_Queries.sql

Contains SQL queries written to answer business questions raised by different stakeholders.

The queries focus on:

- School performance analysis
- Student performance analysis
- Subject-wise performance
- Test performance
- Chapter-wise performance
- Question analytics
- Risk analysis
- KPI reporting

Example business questions answered:

- How many students are enrolled?
- What is the school's overall pass percentage?
- Which subject has the highest average score?
- Which chapters require improvement?
- Who are the top-performing students?
- Which students are at high academic risk?

---

### 03_Data_Validation_Queries.sql

Contains SQL queries used to validate the quality and integrity of the generated datasets before analysis.

The validation includes:

- NULL value checks
- Duplicate record detection
- Percentage range validation
- Marks validation
- Grade validation
- Pass/Fail validation
- Foreign key consistency checks
- Student-test relationship validation
- Accuracy rate validation
- Dataset summary verification

These checks help ensure that the data used for reporting is accurate, complete, and reliable.

---

## SQL Concepts Demonstrated

This project demonstrates practical SQL skills commonly expected from Business Analysts and BI Analysts.

### Data Retrieval

- SELECT
- DISTINCT

### Filtering

- WHERE
- IN
- NOT IN

### Aggregation

- COUNT()
- SUM()
- AVG()
- MIN()
- MAX()

### Grouping

- GROUP BY
- HAVING

### Sorting

- ORDER BY
- TOP

### Conditional Logic

- CASE

### Joins

- INNER JOIN
- LEFT JOIN

### Data Validation

- NULL Checks
- Duplicate Detection
- Referential Integrity Validation
- Business Rule Validation

---

## SQL Workflow

```
Python ETL Pipeline
        │
        ▼
Generated CSV Files
        │
        ▼
Microsoft SQL Server
        │
        ▼
Data Validation Queries
        │
        ▼
Business Analysis Queries
        │
        ▼
Power BI Dashboard
```

---

## Stakeholders Supported

The SQL scripts were written to answer business questions from:

- Principal
- Academic Coordinator
- Teachers
- School Management

---

## Key Business Insights Generated

- Overall school performance
- Student performance trends
- Subject-wise performance comparison
- Pass percentage analysis
- Grade distribution
- High-risk student identification
- Chapter-wise accuracy analysis
- Question difficulty analysis
- Test performance comparison

---

## Purpose of Using SQL

SQL was incorporated into this project to:

- Validate generated datasets before reporting
- Perform exploratory business analysis
- Answer stakeholder questions using SQL
- Verify business KPIs
- Demonstrate SQL competency as part of a Business Analyst portfolio

The Power BI dashboards consume the prepared analytical datasets, while SQL serves as a complementary analysis and validation layer.

---

## Tools Used

- Microsoft SQL Server 2022 Express
- SQL Server Management Studio (SSMS)
- Python
- Power BI Desktop

---

## Author

**Ramyashree G V**

**Business Analyst Portfolio Project**

**Student Performance Analytics Dashboard**