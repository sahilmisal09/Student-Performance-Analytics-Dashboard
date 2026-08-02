# 10_Dashboard

## Overview

This folder contains the final Power BI dashboard developed for the **Student Performance Analytics & Decision Support System** project for **Mega Central High School**.

The dashboard transforms raw assessment data into interactive visualizations that help school stakeholders monitor academic performance, identify learning gaps, detect at-risk students, and support data-driven decision-making.

The dashboard was built using Microsoft Power BI and is based on the cleaned analytical dataset generated through the Python ETL pipeline and validated using Microsoft SQL Server (MSSQL).

---

# Folder Contents

| File | Description |
|------|-------------|
| Dashboard_User_Guide.pdf | Complete user guide explaining every dashboard page, KPIs, visuals, navigation, business rules, filters, and usage instructions. |
| Dashboard_User_Guide.docx | Editable source version of the dashboard user guide. |
| Student_Performance_Analytics.pbix | Final interactive Power BI dashboard containing the complete analytical solution. |

---

# Dashboard Pages

The Power BI report consists of four interactive dashboard pages.

## 1. Executive Performance Overview

Provides a school-wide academic performance summary.

### KPIs

- Total Students
- Tests Conducted
- Average Score
- Pass Percentage
- High Risk Students
- Top Performers

### Visualizations

- Subject-wise Performance
- Student Performance Distribution
- Student Risk Profile
- Monthly Academic Performance Trend

Business Purpose

Provides school leadership with a quick overview of academic performance and institutional health.

---

## 2. Individual Student Performance Analysis

Provides detailed academic insights for an individual student.

### Features

- Student Selection Slicer
- Student Profile Cards
- Subject-wise Performance
- Chapter-wise Learning Gaps
- Student Performance Trend
- Assessment History

Business Purpose

Supports teachers and academic coordinators in monitoring individual student progress and planning personalized interventions.

---

## 3. Risk Analysis Dashboard

Focuses on identifying academically vulnerable students.

### KPIs

- High Risk Students
- Medium Risk Students
- Low Risk Students
- Students Needing Academic Support

### Visualizations

- Student Risk Distribution
- Attendance Category Distribution
- Subject-wise Risk Assessment
- High Risk Student List

Business Purpose

Enables early identification of students requiring academic intervention and supports targeted remedial actions.

---

## 4. Subject & Chapter Performance Analysis

Evaluates curriculum performance at subject and chapter levels.

### KPIs

- Total Subjects
- Total Chapters
- Average Accuracy
- Chapters Below Target

### Visualizations

- Subject-wise Performance
- Question Difficulty Distribution
- Chapter Accuracy Distribution
- Chapters Requiring Attention
- Chapter Performance Table

Business Purpose

Helps teachers and curriculum planners identify weak chapters, evaluate assessment quality, and improve instructional effectiveness.

---

# Key Features

- Interactive dashboard navigation
- Dynamic KPI cards
- Drill-down analysis
- Cross-filtering across visuals
- Student-level analysis
- Risk-based categorization
- Chapter-wise performance monitoring
- Subject comparison
- Trend analysis
- Interactive slicers and filters

---

# Data Sources

The dashboard uses structured analytical datasets generated from the following source files:

- students.csv
- tests.csv
- responses.csv
- question_bank.csv

The data is processed through:

- Python ETL Pipeline
- Microsoft SQL Server (MSSQL) validation and business queries
- Power BI Data Model

---

# Technology Stack

- Microsoft Power BI
- Microsoft SQL Server (MSSQL)
- Python
- Pandas
- NumPy
- Microsoft Excel

---

# Business Value

The dashboard enables stakeholders to:

- Monitor overall school performance
- Identify high-risk students early
- Track individual student progress
- Analyze subject-wise performance
- Detect weak curriculum areas
- Evaluate assessment quality
- Support evidence-based academic planning
- Reduce manual reporting effort

---

# Related Documents

Additional project documentation is available in the following folders:

- 01_Project_Overview
- 02_Stakeholder_Analysis
- 03_Business_Analysis
- 04_Requirements
- 05_Data_Analysis
- 06_Process_Modeling
- 07_Solution_Design
- 08_Data_Pipeline
- 09_SQL
- 11_Testing
- 12_Project_Closure

---

# Project Information

**Project:** Student Performance Analytics & Decision Support System

**Domain:** Education Analytics

**Organization:** Mega Central High School (Fictional)

**Role:** Business Analyst

**Tools Used:**

- Microsoft Power BI
- Microsoft SQL Server
- Python
- Excel

---

# Note

This project has been developed for portfolio and learning purposes.

All datasets are synthetic and generated specifically for demonstrating Business Analysis, SQL, Data Analytics, ETL, and Power BI capabilities. No real student information has been used.


# Author

**Project:** Student Performance Analytics & Decision Support System

**Organization:** Mega Central High School

**Prepared By:** Ramyashree GV

**Role:** Business Analyst