import os
from openai import OpenAI

def explain_fit(resume_text, job_text, features, fit_score):
    """Generate explanation for resume fit score using OpenAI"""
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return "Error: OPENAI_API_KEY environment variable not set"
        
        client = OpenAI(api_key=api_key)
        
        prompt = f"""
You are a recruiter.

Resume text:
{resume_text[:1500]}

Job description:
{job_text[:1500]}

Structured features:
{features}

Model fit score: {fit_score}

Explain:
1. Why the score is high or low
2. What skills or experience are missing
3. Concrete suggestions to improve the resume

Rules:
- Do not change the score
- Do not invent experience
- Be concise and practical
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating explanation: {str(e)}"
    
# Test the module loads
if __name__ == "__main__":
    print("✓ explainer.py loaded successfully")
    print(f"✓ explain_fit function exists: {callable(explain_fit)}")