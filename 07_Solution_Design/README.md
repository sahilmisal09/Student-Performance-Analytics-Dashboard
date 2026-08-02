# 07_Solution_Design

## Overview

This folder contains the solution design artifacts created for the **Student Performance Analytics & Decision Support System** project.

The purpose of this phase was to transform the approved business requirements into a practical analytics solution by defining dashboard requirements, designing user interface wireframes, proposing the technical solution architecture, and documenting the end-to-end data flow.

The solution integrates **CSV source files, a Python ETL pipeline, Microsoft SQL Server, and Microsoft Power BI** to provide automated academic analytics and interactive dashboards for school stakeholders.

---

# Folder Contents

## 01_Dashboard_Requirements

**Purpose**

Defines the functional and business requirements for each Power BI dashboard developed in the project.

**Dashboards Covered**

### Executive Performance Overview

Provides school-wide academic KPIs and performance trends.

### Individual Student Performance Dashboard

Provides detailed performance analysis for individual students.

### Risk Analysis Dashboard

Identifies academically at-risk students requiring intervention.

### Subject & Chapter Performance Analysis Dashboard

Analyzes curriculum effectiveness through subject and chapter-level insights.

**Document Includes**

- Dashboard objectives
- Business users
- KPIs
- Visual requirements
- Business questions answered
- Filters and slicers
- Drill-down capabilities
- Acceptance criteria

**Business Value**

Ensures dashboards meet stakeholder expectations and business objectives.

**Deliverable**

Dashboard Requirements Document

---

## 02_Wireframes

**Purpose**

Provides low-fidelity dashboard layouts created before Power BI development.

The wireframes define the placement of:

- KPI cards
- Charts
- Tables
- Filters
- Navigation
- Dashboard layout

**Dashboards Designed**

- Executive Performance Overview
- Individual Student Performance Dashboard
- Risk Analysis Dashboard
- Subject & Chapter Performance Analysis Dashboard

**Business Value**

- Validates user interface before development
- Improves stakeholder communication
- Reduces redesign effort during implementation

**Deliverable**

Dashboard Wireframes

---

## 03_Solution_Proposal

**Purpose**

Presents the proposed technical solution to address the school's reporting and academic monitoring challenges.

**Solution Components**

### Data Layer

Stores:

- Student Data
- Test Data
- Question Bank
- Assessment Responses

### Processing Layer

Python ETL pipeline performs:

- Data extraction
- Data cleaning
- Data validation
- Data transformation
- Business rule implementation

### Database Layer

Microsoft SQL Server provides:

- Structured relational database
- Fact and dimension tables
- Business queries
- Data validation queries

### Analytics Layer

Power BI provides:

- Interactive dashboards
- KPI monitoring
- Trend analysis
- Student performance analytics
- Risk monitoring

**Business Value**

Provides a scalable and maintainable analytics solution supporting data-driven academic decision-making.

**Deliverable**

Solution Proposal Document

---

## Data_Architecture

**Purpose**

Illustrates the complete end-to-end solution architecture.

The architecture demonstrates how data flows through the system from raw source files to interactive dashboards.

### Architecture Flow

```
Source CSV Files
(Student, Test, Response, Question Data)
                │
                ▼
        Python ETL Pipeline
 (Extract • Clean • Validate • Transform)
                │
                ▼
      Microsoft SQL Server Database
        (Fact & Dimension Tables)
                │
                ▼
      SQL Queries & Data Validation
                │
                ▼
        Power BI Data Model
                │
                ▼
 Interactive Power BI Dashboards
                │
                ▼
      Teachers • Principal
 Academic Coordinators • Management
```

**Business Value**

- Provides a clear understanding of the technical solution
- Demonstrates system integration
- Supports implementation planning
- Simplifies stakeholder communication

**Deliverable**

Solution Architecture Diagram

---

# Solution Design Workflow

The solution design followed the workflow below:

```
Business Requirements
          │
          ▼
Dashboard Requirements
          │
          ▼
Dashboard Wireframes
          │
          ▼
Solution Proposal
          │
          ▼
Technical Architecture
          │
          ▼
Python ETL Pipeline
          │
          ▼
SQL Database
          │
          ▼
Power BI Dashboards
```

---

# Technology Stack

| Component | Technology |
|-----------|------------|
| Data Source | CSV Files |
| ETL & Data Processing | Python (Pandas, NumPy) |
| Database | Microsoft SQL Server |
| Query Language | SQL |
| Data Modeling | Star Schema |
| Reporting & Visualization | Microsoft Power BI |
| Documentation | Microsoft Word, PDF |
| Diagramming | Draw.io |

---

# Key Deliverables

This phase produced the following Business Analysis artifacts:

- Dashboard Requirements Document
- Dashboard Wireframes
- Solution Proposal
- Solution Architecture Diagram

---

# Business Value

The deliverables in this folder helped to:

- Translate business requirements into a technical solution
- Define dashboard functionality before development
- Standardize dashboard layouts and user experience
- Design a scalable analytics architecture
- Integrate Python, SQL Server, and Power BI into a single reporting solution
- Improve communication between business and technical stakeholders

---

# Related Project Sections

The outputs from this phase were used in:

- Process Modeling
- Python ETL Development
- SQL Database Implementation
- Power BI Dashboard Development
- User Acceptance Testing (UAT)
- Final Project Presentation

---

# Author

**Project:** Student Performance Analytics & Decision Support System

**Organization:** Mega Central High School

**Prepared By:** Ramyashree GV

**Role:** Business Analyst