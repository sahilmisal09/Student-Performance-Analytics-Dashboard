import pandas as pd
import numpy as np


# LOAD FILES

students = pd.read_csv("students.csv")
tests = pd.read_csv("tests.csv")
questions = pd.read_csv("question_bank.csv")

np.random.seed(42)

# PROBABILITY TABLES

ABILITY_PROBS = {"Excellent": {"Easy": 0.95, "Medium": 0.85, "Hard": 0.70},
                 "Good": {"Easy": 0.85, "Medium": 0.70, "Hard": 0.50},
                 "Average": {"Easy": 0.70, "Medium": 0.50, "Hard": 0.30},
                 "Weak": {"Easy": 0.50, "Medium": 0.30, "Hard": 0.15},
                 "At Risk": {"Easy": 0.35, "Medium": 0.20, "Hard": 0.05}}

ATTENDANCE_ADJ = {"Excellent": 0.05, "Good": 0.00, "Average": -0.05, "Poor": -0.10}

TEST_FACTOR = {"Easy": 1.10, "Medium": 1.00, "Hard": 0.90}

# SELECT QUESTIONS FOR EACH TEST

test_question_list = []

for _, test in tests.iterrows():
    subject = test["subject"]
    subject_questions = questions[questions["subject"] == subject]
    selected = subject_questions.sample(n=21, replace=False, random_state=int(str(test["test_id"]).replace("T", "")))
    selected["test_id"] = test["test_id"]
    test_question_list.append(selected)

test_questions = pd.concat(test_question_list,ignore_index=True)

# STUDENT × TEST CROSS JOIN

students["key"] = 1
tests["key"] = 1

student_tests = students.merge(tests,on="key").drop("key", axis=1)

# ABSENTEEISM

attendance_mask = np.random.choice([1, 0], size=len(student_tests), p=[0.96, 0.04])

student_tests = student_tests[attendance_mask == 1]

# ATTACH QUESTIONS

responses = student_tests.merge(test_questions, on="test_id", suffixes=("_student", "_question"))

# CALCULATE PROBABILITIES

def get_probability(row):
    ability = row["ability_level"]
    difficulty = row["difficulty"]
    p = ABILITY_PROBS[ability][difficulty]
    if (row["strong_subject"] == row["subject_student"]):
        p += 0.10
    p += ATTENDANCE_ADJ[row["attendance_category"]]

    p *= TEST_FACTOR[row["test_difficulty"]]

    p = max(min(p, 0.99), 0.01)

    return p

responses["probability"] = (responses.apply(get_probability, axis=1))

# GENERATE SCORE

responses["score"] = np.random.binomial(n=1, p=responses["probability"])

# FINAL DATASET

responses = responses[["student_id", "test_id", "question_id", "score"]]

# SAVE

responses.to_csv("responses.csv", index=False)

print("\nResponses Created Successfully\n")
print(responses.head())
print()
print("Rows:", len(responses))

responses = pd.read_csv("responses.csv")
print(responses.shape)
print(responses["score"].value_counts(normalize=True))