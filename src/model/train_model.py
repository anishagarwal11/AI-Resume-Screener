import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.calibration import CalibratedClassifierCV
import joblib

df = pd.read_csv("data/processed/training_data.csv")

X = df.drop("label", axis=1)
y = df["label"]

base_model = Pipeline([
    ("scaler", StandardScaler()),
    ("lr", LogisticRegression())
])

calibrated_model = CalibratedClassifierCV(
    base_model,
    method="sigmoid",
    cv=3
)

calibrated_model.fit(X, y)

joblib.dump(calibrated_model, "src/model/resume_model.pkl")
print("Model retrained with calibration")
