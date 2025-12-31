import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)          # normalize whitespace
    text = re.sub(r'[^a-z0-9\s]', '', text)   # remove special characters
    return text.strip()


if __name__ == "__main__":
    sample_text = """
    Software Engineer — Python, ML
    Email: test@email.com
    Experience: 3+ years!!!
    """
    print(clean_text(sample_text))