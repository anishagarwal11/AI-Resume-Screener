import joblib
import pandas as pd
from src.features.run_feature_pipeline import features

model = joblib.load("src/model/resume_model.pkl")

X = pd.DataFrame([features])
score = model.predict_proba(X)[0][1]

print(f"Fit Score: {round(score, 2)}")
