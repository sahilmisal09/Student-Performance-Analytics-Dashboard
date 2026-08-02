import pandas as pd

print("Loading files...")

responses = pd.read_csv("responses.csv")
question_bank = pd.read_csv("question_bank.csv")

print("Merging datasets...")

df = responses.merge(question_bank[["question_id", "subject", "chapter", "difficulty"]], on="question_id", how="left")

print("Calculating question analytics...")

question_analytics = (df.groupby(["question_id", "subject", "chapter", "difficulty"]).agg(attempts=("score", "count"), correct=("score", "sum")).reset_index())

# Incorrect answers
question_analytics["incorrect"] = (question_analytics["attempts"] - question_analytics["correct"])

# Accuracy Rate
question_analytics["accuracy_rate"] = (question_analytics["correct"] / question_analytics["attempts"]) * 100

# Round values
question_analytics["accuracy_rate"] = (question_analytics["accuracy_rate"].round(2))

# PERFORMANCE CATEGORY

def classify_question(x):

    if x >= 80:
        return "Easy"

    elif x >= 50:
        return "Moderate"

    else:
        return "Difficult"

question_analytics["performance_category"] = (question_analytics["accuracy_rate"].apply(classify_question))


print("Saving question_analytics.csv...")

question_analytics.to_csv("question_analytics.csv",index=False)

print("\nquestion_analytics.csv created successfully.\n")

print(question_analytics.head())

print("\nShape:")
print(question_analytics.shape)


# Validation Checks
qa = pd.read_csv("question_analytics.csv")
print(qa.shape)
print(qa["accuracy_rate"].describe())


#Check Performance Categories
print(qa["performance_category"].value_counts())


# Most Difficult Questions
print(qa.sort_values("accuracy_rate").head(10))


# Easiest Questions
print(qa.sort_values("accuracy_rate", ascending=False).head(10))


print(qa.groupby("difficulty")["accuracy_rate"].mean())


