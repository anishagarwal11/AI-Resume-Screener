try:
    from src.parsing.resume_parser import extract_text_from_pdf
    print("✓ Imported resume_parser")
except Exception as e:
    print(f"✗ Error importing resume_parser: {e}")
    extract_text_from_pdf = None

try:
    from src.parsing.text_cleaner import clean_text
    print("✓ Imported text_cleaner")
except Exception as e:
    print(f"✗ Error importing text_cleaner: {e}")
    clean_text = None

try:
    from src.features.run_feature_pipeline import features
    print("✓ Imported features")
except Exception as e:
    print(f"✗ Error importing features: {e}")
    features = {}

try:
    from src.model.predict import score
    print("✓ Imported score")
except Exception as e:
    print(f"✗ Error importing score: {e}")
    score = 0

try:
    from src.llm.explainer import explain_fit
    print("✓ Imported explain_fit")
except Exception as e:
    print(f"✗ Error importing explain_fit: {e}")
    explain_fit = None


if __name__ == "__main__":
    job_text = ""
    resume_text = ""
    
    try:
        with open("data/raw/job_description.txt") as f:
            job_text = clean_text(f.read()) if clean_text else f.read()
        print("✓ Loaded job description")
    except Exception as e:
        print(f"✗ Error loading job description: {e}")

    try:
        if extract_text_from_pdf:
            resume_text = extract_text_from_pdf("data/raw/resume.pdf")
            print("✓ Extracted resume text")
        else:
            print("✗ extract_text_from_pdf not available")
    except Exception as e:
        print(f"✗ Error extracting resume: {e}")

    try:
        if explain_fit and resume_text and job_text:
            explanation = explain_fit(
                resume_text=resume_text,
                job_text=job_text,
                features=features,
                fit_score=round(score, 2)
            )
            if explanation:
                print("\n" + str(explanation))
            else:
                print("✗ No explanation generated")
        else:
            print("✗ Cannot generate explanation - missing dependencies")
    except Exception as e:
        print(f"✗ Error generating explanation: {e}")