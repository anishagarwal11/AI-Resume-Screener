from src.parsing.resume_parser import extract_text_from_pdf
from src.parsing.text_cleaner import clean_text
from src.features.feature_extractor import extract_features

with open("data/raw/job_description.txt") as f:
    job_text = clean_text(f.read())

resume_text = extract_text_from_pdf("data/raw/resume.pdf")

features = extract_features(resume_text, job_text)
print(features)


