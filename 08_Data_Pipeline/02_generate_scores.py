import pandas as pd

print("Loading files...")

responses = pd.read_csv("responses.csv")

tests = pd.read_csv("tests.csv")


print("Calculating test scores...")


# Calculate student performance per test
scores = (
    responses
    .groupby(["student_id", "test_id"])
    .agg(
        correct_answers=("score", "sum"),
        total_questions=("score", "count")
    )
    .reset_index()
)


# Wrong answers

scores["wrong_answers"] = (
    scores["total_questions"]
    -
    scores["correct_answers"]
)


print("Merging test information...")


# Bring maximum marks from tests table

scores = scores.merge(
    tests[
        [
            "test_id",
            "date",
            "subject",
            "test_type",
            "test_difficulty",
            "duration_minutes",
            "chapter_coverage",
            "term",
            "max_marks"
        ]
    ],
    on="test_id",
    how="left"
)


# Calculate marks obtained based on accuracy

scores["marks_obtained"] = (
    scores["correct_answers"]
    /
    scores["total_questions"]
) * scores["max_marks"]


# Percentage

scores["percentage"] = (
    scores["marks_obtained"]
    /
    scores["max_marks"]
) * 100



# Pass / Fail

scores["pass_fail"] = scores["percentage"].apply(
    lambda x: "Pass" if x >= 35 else "Fail"
)



# Grade calculation

def assign_grade(x):

    if x >= 90:
        return "A1"

    elif x >= 80:
        return "A2"

    elif x >= 70:
        return "B1"

    elif x >= 60:
        return "B2"

    elif x >= 50:
        return "C1"

    elif x >= 40:
        return "C2"

    elif x >= 35:
        return "D"

    else:
        return "E"



scores["grade"] = scores["percentage"].apply(assign_grade)



print("Saving scores.csv...")


scores.to_csv(
    "scores.csv",
    index=False
)


print("\nScores generated successfully")

print(scores.head())


print("\nShape:")
print(scores.shape)


print("\nPercentage Summary")
print(scores["percentage"].describe())


print("\nPass / Fail")
print(scores["pass_fail"].value_counts())


print("\nGrades")
print(scores["grade"].value_counts())