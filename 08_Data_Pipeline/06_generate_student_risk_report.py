import pandas as pd

print("Loading files...")

students = pd.read_csv("students.csv")
progress = pd.read_csv("student_progress.csv")

# MERGE DATA

print("Merging datasets...")

risk = progress.merge(students[["student_id", "name", "ability_level", "attendance_category"]], on="student_id", how="left")

# PERFORMANCE BAND

def performance_band(x):

    if x >= 85:
        return "Top Performer"

    elif x >= 70:
        return "High Performer"

    elif x >= 50:
        return "Average"

    elif x >= 35:
        return "Needs Support"

    else:
        return "At Risk"

risk["performance_band"] = (risk["avg_percentage"].apply(performance_band))

# RISK MODEL

def assign_risk(row):

    score = row["avg_percentage"]
    attendance = row["attendance_category"]

    # High Risk
    if (score < 35 or (score < 50 and attendance == "Poor")):
        return "High Risk"

    # Medium Risk
    elif (score < 50 or attendance == "Poor"):
        return "Medium Risk"

    # Low Risk
    else:
        return "Low Risk"

risk["risk_level"] = risk.apply(assign_risk, axis=1)

# INTERVENTION FLAG

risk["intervention_required"] = (risk["risk_level"].apply(lambda x:"Yes" if x in ["High Risk", "Medium Risk"] else "No"))

# SORT

risk = risk.sort_values(["risk_level", "avg_percentage"])

# SAVE

risk.to_csv("student_risk_report.csv", index=False)

print("\nstudent_risk_report.csv created successfully.\n")

print(risk.head())

print("\nShape:")
print(risk.shape)

print("\nRisk Distribution")
print(risk["risk_level"].value_counts())

print("\nIntervention Required")
print(risk["intervention_required"].value_counts())



# Validation Checks
risk = pd.read_csv("student_risk_report.csv")
print(risk["risk_level"].value_counts())
print(risk.groupby("risk_level")["avg_percentage"].mean())


