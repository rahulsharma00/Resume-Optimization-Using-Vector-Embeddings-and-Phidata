from openai import OpenAI

from dotenv import load_dotenv
import os
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer

# Load environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from the environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

if openai_api_key is None:
    raise ValueError("OpenAI API key not found in environment variables!")

# Set the OpenAI API key

def get_resume_suggestions(resume_text, job_description, missing_keywords):
    # Set up OpenAI API request
    completion = client.chat.completions.create(model="gpt-4",  # Use "gpt-4" or "gpt-3.5-turbo"
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": f"""
I am tailoring my resume for the role of a Data Analyst. Here is the job description: B. Tech. / B.E. / MCA
1-2 years of relevant experience
Strong Python coding skills
Hands-on experience in writing RESTful APIs using python
Experience in SQL and data management
Exposure to application deployment in cloud environment
Good understanding of LLM models, Vector databases, and frameworks like LangChain/LlamaIndex
Strong problem-solving skills and the ability to work in a fast-paced environment
Excellent teamwork & communication skills
This role will be full-time and completely remot
{job_description}

And here is my current resume text:
{resume_text}

The following keywords are missing but are relevant to the job:
{', '.join(missing_keywords)}

Please suggest how to naturally and professionally incorporate these keywords into my resume.
Rewrite or enhance sections as needed to better align with the job description while maintaining an authentic representation of my skills and experiences. 
Provide specific bullet points, rephrased statements, or new content where necessary. Please keep my existing projects as well in the final output.

Once you've suggested the changes, use them to create a fully updated version of my resume tailored to the job description. 
Ensure the new resume is well-structured, highlights my most relevant skills and experiences, and maximizes my chances of getting noticed by recruiters.
"""
        }
    ])

    return completion.choices[0].message.content

def main():
    # Path to the resume PDF file
    resume_pdf_path = "/Users/rahulsharma/Desktop/Resumate/Data/Rahul's_Resume.pdf"

    # Job description text
    job_description = """
    [Insert the job description here]
    """

    # Read the resume PDF
    reader = PdfReader(resume_pdf_path)
    resume_text = ""
    for page in reader.pages:
        resume_text += page.extract_text()

    # Extract keywords and find missing ones
    vectorizer = TfidfVectorizer(stop_words='english', max_features=20)
    X = vectorizer.fit_transform([resume_text])
    keywords = vectorizer.get_feature_names_out()
    scores = X.toarray().flatten()

    keyword_scores = list(zip(keywords, scores))
    keyword_scores.sort(key=lambda x: x[1], reverse=True)

    job_vectorizer = TfidfVectorizer(stop_words='english')
    job_X = job_vectorizer.fit_transform([job_description])
    job_keywords = job_vectorizer.get_feature_names_out()

    missing_keywords = set(job_keywords) - set(keywords)

    # Get resume suggestions from OpenAI
    suggestions = get_resume_suggestions(resume_text, job_description, missing_keywords)

    print("Suggestions to Tailor Your Resume:")
    print(suggestions)

if __name__ == "__main__":
    main()