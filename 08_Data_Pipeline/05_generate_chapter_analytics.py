import pandas as pd

print("Loading files...")

responses = pd.read_csv("responses.csv")
question_bank = pd.read_csv("question_bank.csv")

# MERGE DATA
print("Merging datasets...")

df = responses.merge(question_bank[["question_id", "subject", "chapter"]], on="question_id", how="left")

# CHAPTER ANALYTICS

print("Calculating chapter analytics...")

chapter_analytics = (df.groupby(["subject", "chapter"]).agg(attempts=("score", "count"), correct=("score", "sum")).reset_index())

# Incorrect responses
chapter_analytics["incorrect"] = (chapter_analytics["attempts"] - chapter_analytics["correct"])

# Accuracy %

chapter_analytics["accuracy_rate"] = (chapter_analytics["correct"] / chapter_analytics["attempts"]) * 100

chapter_analytics["accuracy_rate"] = (chapter_analytics["accuracy_rate"].round(2))

# PERFORMANCE CATEGORY

def classify_chapter(x):

    if x >= 65:
        return "Strong"

    elif x >= 55:
        return "Average"

    else:
        return "Weak"

chapter_analytics["performance_category"] = (chapter_analytics["accuracy_rate"].apply(classify_chapter))

# SORT

chapter_analytics = chapter_analytics.sort_values(["subject", "accuracy_rate"], ascending=[True, False])


# Adding rank column
chapter_analytics["chapter_rank"] = (chapter_analytics["accuracy_rate"].rank(ascending=False, method="dense").astype(int))


# SAVE

chapter_analytics.to_csv("chapter_analytics.csv", index=False)

print("\nchapter_analytics.csv created successfully.\n")

print(chapter_analytics.head())

print("\nShape:")
print(chapter_analytics.shape)



# Validation Checks

ca = pd.read_csv("chapter_analytics.csv")
print(ca.shape)
print(ca["accuracy_rate"].describe())

# Check Performance Categories
print(ca["performance_category"].value_counts())

# Weakest Chapters
print(ca.sort_values("accuracy_rate").head(10))

# Strongest Chapters
print(ca.sort_values("accuracy_rate", ascending=False).head(10))

# Subject-Level Validation
print(ca.groupby("subject")["accuracy_rate"].mean())

