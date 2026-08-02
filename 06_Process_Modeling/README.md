# 06_Process_Modeling

## Overview

This folder contains the process modeling artifacts created for the **Student Performance Analytics & Decision Support System** project.

Process modeling is an essential Business Analysis activity used to understand the existing ("As-Is") business process, identify inefficiencies, and design an improved ("To-Be") process that supports automation, data-driven decision-making, and streamlined academic performance monitoring.

The process models developed in this project illustrate how assessment data flows from teachers through the Python ETL pipeline and SQL database into interactive Power BI dashboards for reporting and decision support.

---

# Folder Contents

## 01_AS_IS_Process_Flow

**Purpose**

Illustrates the current manual process followed by the school before implementing the proposed analytics solution.

**Process Includes**

- Teachers conduct assessments
- Marks are recorded manually
- Data stored in multiple Excel files
- Manual report preparation
- Limited performance analysis
- Delayed identification of at-risk students

**Business Value**

- Documents the current business process
- Highlights operational inefficiencies
- Establishes a baseline for process improvement

**Deliverable**

As-Is Process Flow Diagram

---

## 02_BPMN_AS_IS_Process

**Purpose**

Represents the current ("As-Is") academic performance monitoring process using BPMN (Business Process Model and Notation).

**Activities Included**

- Conduct Assessment
- Record Student Marks
- Consolidate Data
- Prepare Reports
- Review Student Performance
- Identify Students Requiring Support

**Business Value**

- Standardizes process documentation
- Identifies bottlenecks and manual activities
- Facilitates stakeholder discussions

**Deliverable**

BPMN As-Is Process Diagram

---

## 03_BPMN_TO_BE_Process

**Purpose**

Illustrates the redesigned ("To-Be") business process after implementing the analytics solution.

**Improved Process Includes**

- Import assessment data
- Python ETL data processing
- SQL database storage
- Automated data validation
- Power BI dashboard generation
- Real-time performance monitoring
- Early identification of at-risk students

**Business Value**

- Demonstrates the future-state process
- Highlights automation opportunities
- Supports solution implementation planning

**Deliverable**

BPMN To-Be Process Diagram

---

## 04_TO_BE_Process_Flow

**Purpose**

Shows the improved end-to-end workflow after implementing the proposed solution.

**Process Flow**

```
Teacher Assessment Data
        │
        ▼
CSV Source Files
        │
        ▼
Python ETL Pipeline
        │
        ▼
SQL Database
        │
        ▼
Power BI Dashboards
        │
        ▼
Academic Decision Making
```

**Business Value**

- Visualizes the future-state solution
- Demonstrates system integration
- Supports stakeholder understanding

**Deliverable**

To-Be Process Flow Diagram

---

## 05_Use_Case_Diagram

**Purpose**

Illustrates the interactions between system users and the Student Performance Analytics System.

**Actors**

- Principal
- Teacher
- Academic Coordinator
- School Management

**Major Use Cases**

- View Executive Dashboard
- Analyze Student Performance
- Search Student
- Monitor Subject Performance
- Review Chapter Analytics
- Identify High-Risk Students
- Track Performance Trends
- Generate Academic Reports

**Business Value**

- Defines system boundaries
- Identifies user interactions
- Supports functional requirement validation

**Deliverable**

Use Case Diagram

---

# Process Modeling Lifecycle

The following approach was followed during process modeling:

```
Current Business Process
          │
          ▼
As-Is Process Flow
          │
          ▼
BPMN As-Is Model
          │
          ▼
Gap Analysis
          │
          ▼
Solution Design
          │
          ▼
BPMN To-Be Model
          │
          ▼
Future Process Flow
          │
          ▼
Use Case Diagram
```

---

# Business Improvements Achieved

| Current Process (As-Is) | Improved Process (To-Be) |
|--------------------------|--------------------------|
| Manual data entry | Automated ETL processing |
| Multiple Excel files | Centralized SQL database |
| Manual report preparation | Interactive Power BI dashboards |
| Delayed analysis | Near real-time insights |
| Difficult student tracking | Individual student analytics |
| Reactive interventions | Early risk identification |
| Limited reporting | Self-service dashboards |

---

# Key Deliverables

This phase produced the following Business Analysis artifacts:

- As-Is Process Flow
- BPMN As-Is Process Diagram
- BPMN To-Be Process Diagram
- To-Be Process Flow
- Use Case Diagram

---

# Business Value

The process modeling deliverables helped to:

- Understand existing business workflows
- Identify process inefficiencies
- Design an optimized future-state process
- Visualize system interactions
- Support solution architecture
- Improve stakeholder communication
- Enable data-driven academic decision-making

---

# Related Project Sections

The outputs from this phase were used in:

- Requirements Engineering
- Solution Design
- SQL Database Design
- Python ETL Pipeline
- Power BI Dashboard Development
- User Acceptance Testing (UAT)

---

# Author

**Project:** Student Performance Analytics & Decision Support System

**Organization:** Mega Central High School

**Prepared By:** Ramyashree GV

**Role:** Business Analyst