# 05_Data_Analysis

## Overview

This folder contains all data analysis and data preparation deliverables created for the **Student Performance Analytics & Decision Support System** project.

The objective of this phase was to understand the structure and quality of the source data, define business metrics, establish data mappings, assess data quality, and design the analytical data model that supports SQL analysis, the Python ETL pipeline, and Power BI dashboards.

These documents ensure that data is accurate, consistent, and suitable for reliable business reporting and decision-making.

---

# Folder Contents

## 01_Data_Dictionary

**Purpose**

Provides detailed metadata for every field used in the project datasets and SQL database.

**Contents**

- Table names
- Column names
- Data types
- Business descriptions
- Primary Keys
- Foreign Keys
- Allowed values
- Sample values

**Business Value**

- Establishes a common understanding of data elements
- Improves communication between business and technical teams
- Supports SQL database design and ETL development

**Deliverable**

Data Dictionary

---

## 02_KPI_Definition_Document

**Purpose**

Defines all Key Performance Indicators (KPIs) used throughout the Power BI dashboards.

**KPIs Included**

- Total Students
- Tests Conducted
- Average Score
- Pass Percentage
- High Risk Students
- Low Risk Students
- Medium Risk Students
- Top Performers
- Students Needing Academic Support
- Average Subject Accuracy
- Chapter Accuracy
- Weak Chapters

**Business Value**

Ensures that all stakeholders interpret dashboard metrics consistently.

**Deliverable**

KPI Definition Document

---

## 03_Data_Mapping_Document

**Purpose**

Maps source data fields to the SQL database, Python ETL outputs, and Power BI data model.

**Contents**

- Source CSV file
- Source column
- SQL table and column
- ETL transformation rules
- Target analytical field
- Power BI usage

**Business Value**

- Improves traceability of data
- Simplifies ETL development
- Ensures accurate dashboard reporting

**Deliverable**

Data Mapping Document

---

## 04_Data_Quality_Assessment

**Purpose**

Evaluates the quality, completeness, and reliability of the project datasets before analysis.

**Validation Checks**

- Missing values
- Duplicate records
- Invalid data types
- Percentage range validation
- Referential integrity
- Data consistency
- Business rule validation

**Business Value**

- Improves reporting accuracy
- Reduces analytical errors
- Ensures trustworthy insights

**Deliverable**

Data Quality Assessment Report

---

## Data_Model

**Purpose**

Illustrates the logical analytical data model used in the project.

The model demonstrates how raw CSV files are transformed through the Python ETL pipeline, structured into SQL tables, and consumed by Power BI for reporting and analytics.

**Architecture Includes**

### Source Layer

- students.csv
- tests.csv
- responses.csv
- question_bank.csv

↓

### Python ETL Layer

- Data Cleaning
- Data Validation
- Data Transformation
- Business Rule Application

↓

### SQL Database Layer

Fact Tables

- Fact_Assessment_Response
- Fact_Test_Score

Dimension Tables

- Dim_Student
- Dim_Test
- Dim_Question
- Dim_Subject
- Dim_Date

↓

### Power BI Data Model

- Star Schema
- DAX Measures
- Dashboard Relationships
- Interactive Reports

↓

### End Users

- Principal
- Teachers
- Academic Coordinator
- School Management

**Business Value**

Provides a clear understanding of the end-to-end data flow from raw source files to business intelligence dashboards.

**Deliverable**

Logical Data Model Diagram

---

# Data Analysis Workflow

The following workflow was followed during this phase:

```
Raw CSV Files
       │
       ▼
Data Understanding
       │
       ▼
Data Dictionary
       │
       ▼
KPI Definition
       │
       ▼
Data Mapping
       │
       ▼
Data Quality Assessment
       │
       ▼
Python ETL Pipeline
       │
       ▼
SQL Database
       │
       ▼
Power BI Data Model
       │
       ▼
Interactive Dashboards
```

---

# Key Deliverables

This phase produced the following Business Analysis artifacts:

- Data Dictionary
- KPI Definition Document
- Data Mapping Document
- Data Quality Assessment Report
- Logical Data Model

---

# Business Value

The deliverables in this folder helped to:

- Understand the structure of source data
- Define standardized business metrics
- Improve data quality and consistency
- Support SQL database implementation
- Guide Python ETL development
- Enable accurate Power BI reporting
- Ensure reliable analytical insights for stakeholders

---

# Related Project Sections

The outputs from this phase were used in:

- Requirements Engineering
- SQL Database Design
- Python ETL Pipeline
- Process Modeling
- Dashboard Development
- Testing & Validation

---

# Author

**Project:** Student Performance Analytics & Decision Support System

**Organization:** Mega Central High School

**Prepared By:** Ramyashree GV

**Role:** Business Analyst