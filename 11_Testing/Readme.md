# Testing

## Overview

This folder contains the testing artifacts created for the **Student Performance Analytics & Decision Support System** project.

The testing phase was conducted to verify that all business requirements, functional requirements, calculations, SQL outputs, Python ETL processes, and Power BI dashboards function correctly before project closure.

Testing was performed at multiple levels, including functional testing, data validation, defect tracking, and User Acceptance Testing (UAT).

---

# Objectives

The testing activities were performed to ensure:

- All business requirements were implemented correctly.
- Functional requirements worked as expected.
- SQL-generated data was accurate and complete.
- Python ETL pipeline generated correct analytical datasets.
- Power BI dashboards displayed accurate KPIs and visualizations.
- Interactive features such as filters and drill-downs functioned properly.
- Business calculations matched the defined business rules.
- Stakeholders accepted the final solution.

---

# Folder Contents

## 01_Test_Plan.xlsx

Defines the overall testing strategy for the project.

Includes:

- Testing objectives
- Scope
- Test approach
- Testing environment
- Entry criteria
- Exit criteria
- Roles and responsibilities
- Testing schedule
- Deliverables

---

## 02_Test_Cases.xlsx

Contains detailed functional test cases created from the Functional Requirements Document (FRD).

Each test case includes:

- Test Case ID
- Requirement ID
- Test Scenario
- Preconditions
- Test Steps
- Expected Result
- Actual Result
- Status (Pass/Fail)
- Tester Name

---

## 03_Defect_Log.xlsx

Maintains a record of defects identified during testing.

Each defect includes:

- Defect ID
- Description
- Severity
- Priority
- Module
- Status
- Assigned To
- Resolution
- Closure Date

---

## 04_UAT_Test_Scenarios.xlsx

Contains User Acceptance Testing (UAT) scenarios executed by business stakeholders.

Each scenario verifies that the delivered solution satisfies the documented business requirements.

Includes:

- Scenario ID
- Business Requirement
- User Action
- Expected Outcome
- Actual Outcome
- Status
- Comments

---

## 05_UAT_Signoff_Template.xlsx

Formal sign-off document confirming successful completion of User Acceptance Testing.

Includes:

- Project Name
- Stakeholder Information
- UAT Summary
- Outstanding Issues
- Approval Status
- Stakeholder Signatures
- Sign-off Date

---

# Testing Scope

The following components were validated during testing:

- SQL database and imported datasets
- Data validation queries
- Python ETL pipeline outputs
- Generated analytical datasets
- Power BI data model
- DAX measures and KPIs
- Dashboard calculations
- Dashboard filters and slicers
- Charts and tables
- Business rules implementation

---

# Testing Types Performed

### Functional Testing

Verified that each dashboard feature behaved according to the Functional Requirements Document.

Examples include:

- Student selection updates all visuals
- KPI cards display correct values
- Subject and chapter charts refresh correctly
- Risk classification is accurate

---

### Data Validation Testing

Validated data quality before dashboard development.

Checks included:

- NULL value detection
- Duplicate record detection
- Percentage validation (0–100)
- Score validation
- Foreign key consistency
- Data completeness

---

### SQL Validation

Business queries were executed to verify:

- Student performance calculations
- Subject-wise averages
- Risk classifications
- Pass percentages
- Chapter accuracy
- Dashboard source metrics

---

### ETL Validation

Verified that Python scripts correctly:

- Generated assessment responses
- Calculated student scores
- Created student progress reports
- Generated chapter analytics
- Produced risk reports
- Created question analytics

---

### Dashboard Testing

Validated all Power BI reports, including:

- Executive Performance Overview
- Individual Student Performance Analysis
- Risk Analysis Dashboard
- Subject & Chapter Performance Analysis

---

### User Acceptance Testing (UAT)

Business users validated that the solution met the project objectives and stakeholder expectations before project closure.

---

# Testing Outcome

The solution successfully passed functional and business validation.

Final status:

- Functional Testing — Passed
- Data Validation — Passed
- SQL Validation — Passed
- ETL Validation — Passed
- Dashboard Testing — Passed
- UAT — Passed

---

# Related Documents

This testing phase is supported by documents available in other project folders:

- Business Requirements Document (BRD)
- Functional Requirements Document (FRD)
- Requirement Traceability Matrix (RTM)
- SQL Business Queries
- SQL Data Validation Queries
- Dashboard Requirements Document
- Dashboard User Guide
- Final Project Presentation

---

# Project

**Student Performance Analytics & Decision Support System**

**Prepared By:** Ramyashree GV  
**Role:** Business Analyst

---
```