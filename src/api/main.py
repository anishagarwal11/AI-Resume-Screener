from fastapi import FastAPI, UploadFile, File, Form
import shutil
import os

from src.parsing.resume_parser import extract_text_from_pdf
from src.parsing.text_cleaner import clean_text
from src.features.feature_extractor import extract_features
from src.model.predict import score
from src.llm.explainer import explain_fit

app = FastAPI(title="AI Resume Screener")

TEMP_RESUME_PATH = "data/raw/temp_resume.pdf"


@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    # Save uploaded resume
    with open(TEMP_RESUME_PATH, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    resume_text = extract_text_from_pdf(TEMP_RESUME_PATH)
    job_text = clean_text(job_description)

    features = extract_features(resume_text, job_text)

    explanation = explain_fit(
        resume_text=resume_text,
        job_text=job_text,
        features=features,
        fit_score=round(score, 2)
    )

    return {
        "features": features,
        "fit_score": round(score, 2),
        "explanation": explanation
    }
