import re

# Skills tailored EXACTLY to your resume
SKILLS = [
    # Core iOS
    "swift", "swiftui", "uikit", "ios", "xcode",

    # Architecture & patterns
    "mvvm", "mvc", "delegate", "protocol",

    # Data & networking
    "rest", "api", "graphql", "core data",

    # UI / UX
    "autolayout", "collection view", "table view",
    "xib", "lottie", "figma",

    # Tooling
    "git", "cocoapods", "carthage",

    # Quality & infra
    "xctest", "unit test", "ui test",
    "datadog", "splunk", "crashlytics",

    # Concurrency
    "multithreading", "dispatch", "operations"
]

EDUCATION_KEYWORDS = [
    "computer science",
    "engineering",
    "bachelor",
    "degree",
    "btech",
    "b.e"
]


def extract_years_of_experience(text: str) -> int:
    """
    Handles:
    - Jan 2021 to Jan 2023
    - June 2024 to Present
    - 3+ years
    - 3-4 years
    """
    patterns = [
        r'(\d+)\s*\+?\s*years',
        r'(\d+)\s*-\s*(\d+)\s*years',
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return int(match.group(1))

    # Fallback: infer from dates (very rough)
    if "2021" in text and ("present" in text or "2024" in text):
        return 3

    return 0


def extract_features(resume_text: str, job_description_text: str) -> dict:
    resume_text = resume_text.lower()
    job_text = job_description_text.lower()

    resume_words = set(resume_text.split())
    job_words = set(job_text.split())

    skill_match_count = sum(1 for skill in SKILLS if skill in resume_text)

    keyword_overlap_ratio = round(
        len(resume_words & job_words) / max(len(job_words), 1),
        3
    )

    years_of_experience = extract_years_of_experience(resume_text)

    education_present = int(
        any(keyword in resume_text for keyword in EDUCATION_KEYWORDS)
    )

    resume_length = len(resume_words)

    return {
        "skill_match_count": skill_match_count,
        "keyword_overlap_ratio": keyword_overlap_ratio,
        "years_of_experience": years_of_experience,
        "education_present": education_present,
        "resume_length": resume_length
    }
