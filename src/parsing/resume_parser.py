import pdfplumber
from src.parsing.text_cleaner import clean_text

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Try to extract text with layout preserved
            page_text = page.extract_text(layout=True)
            if page_text:
                text += page_text + "\n"
    return clean_text(text)


if __name__ == "__main__":
    pdf_path = "data/raw/resume.pdf"
    text = extract_text_from_pdf(pdf_path)
    print(text)
   # print(f"\nTotal characters extracted: {len(text)}")