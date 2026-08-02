import pandas as pd

print("Loading scores.csv...")

scores = pd.read_csv("scores.csv")

# CHECK DATE COLUMN

scores["date"] = pd.to_datetime(scores["date"],format="%d-%m-%Y")

# Sort by student and date
scores = scores.sort_values(["student_id", "date"])

print("Calculating student progress...")

student_progress = (scores.groupby("student_id").agg(
        avg_percentage=("percentage", "mean"),
        best_score=("percentage", "max"),
        worst_score=("percentage", "min"),
        first_score=("percentage", "first"),
        latest_score=("percentage", "last"),
        tests_attempted=("test_id", "count")).reset_index())


#Performance Band
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
student_progress["performance_band"] = (student_progress["avg_percentage"].apply(performance_band))

# IMPROVEMENT

student_progress["improvement"] = (student_progress["latest_score"] - student_progress["first_score"])

# Round values
cols = ["avg_percentage", "best_score", "worst_score", "first_score", "latest_score", "improvement"]

student_progress[cols] = (student_progress[cols].round(2))

# SAVE

student_progress.to_csv("student_progress.csv",index=False)

print("\nstudent_progress.csv created successfully.\n")

print(student_progress.head())
print("\nShape:")
print(student_progress.shape)





# To check the details of the created file
progress = pd.read_csv("student_progress.csv")

print(progress.shape)
print("\nAverage Percentage")
print(progress["avg_percentage"].describe())

print("\nImprovement")
print( progress["improvement"].describe())

print(progress.sort_values("avg_percentage",ascending=False).head(10))

print(progress.sort_values("avg_percentage").head(10))





