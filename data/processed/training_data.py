import pandas as pd

data = [
    # skill_match, overlap, exp, edu, length, label
    [28, 0.55, 4, 1, 380, 1],
    [24, 0.45, 3, 1, 350, 1],
    [20, 0.35, 3, 1, 330, 1],
    [15, 0.25, 2, 1, 300, 0],
    [10, 0.15, 1, 0, 260, 0],
    [5,  0.05, 0, 0, 200, 0],
]

columns = [
    "skill_match_count",
    "keyword_overlap_ratio",
    "years_of_experience",
    "education_present",
    "resume_length",
    "label"
]

df = pd.DataFrame(data, columns=columns)
df.to_csv("data/processed/training_data.csv", index=False)
print(df)
