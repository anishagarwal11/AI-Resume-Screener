# AI Resume Screening System

## Problem
Manual resume screening is time-consuming and opaque. Candidates rarely understand why they are rejected, and recruiters spend limited time per resume.

## Solution
A hybrid AI system that:
- Scores resume–job fit using a deterministic ML model
- Explains the score using an LLM in clear, human language

## Architecture
1. Resume PDF ingestion
2. Text cleaning and normalization
3. Feature engineering (skills, experience, education)
4. ML scoring (Logistic Regression + scaling + calibration)
5. LLM-based explanation layer (read-only)

## Why this design
- Machine Learning ensures interpretability and determinism
- LLMs are used strictly for explanation, not decision-making
- Probability calibration prevents overconfident predictions

## Features extracted
- Skill match count
- Keyword overlap ratio
- Years of experience
- Education presence
- Resume length

## Modeling choices
- Logistic Regression baseline
- Feature scaling using StandardScaler
- Probability calibration using CalibratedClassifierCV

## Limitations
- Small synthetic training dataset
- Resume parsing depends on PDF quality
- In production, the model should be trained on recruiter-labeled data

## How to run
```bash
python -m src.features.run_feature_pipeline
python src/model/train_model.py
python src/model/predict.py
python -m src.llm.run_explainer


## API Usage (FastAPI)

The system can be exposed as an HTTP API for real-world usage.

### Endpoint
POST `/analyze`

### Inputs
- Resume PDF
- Job description text

### Output
- Structured feature values
- Fit score (probability)
- Natural language explanation

## Deployment

### Run locally
```bash
uvicorn src.api.main:app --reload
