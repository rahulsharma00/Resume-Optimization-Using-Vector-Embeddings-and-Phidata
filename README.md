# Resume-Optimization-Using-Vector-Embeddings-and-Phidata
Resumate is a Python-based tool that helps tailor resumes to specific job descriptions by identifying missing keywords and suggesting improvements using OpenAI's GPT model. It extracts text from a resume PDF, analyzes keyword relevance, and provides recommendations for enhancement.

### Features
✅ Extracts resume text from a PDF file.  <br />
✅ Compares resume content with a given job description.  <br />
✅ Identifies missing keywords using TF-IDF vectorization.  <br />
✅ Uses OpenAI GPT to suggest improvements and generate a tailored resume.  <br />
✅ Plans to integrate vector embeddings for more accurate semantic matching.  <br />

### Planned Enhancements
🚀 Replace TF-IDF with OpenAI's text embeddings for better semantic matching.<br />
🚀 Support for multiple resume formats (DOCX, TXT).<br />
🚀 UI using streamlit/gradio<br />

Here’s a clean installation guide for your GitHub project!  

---
---
## 📥 **Installation Instructions**

Follow these steps to clone the repo and set up the environment!

---

✅ **Step 1: Clone the Repository**

```bash
git clone https://github.com/rahulsharma00/Resume-Optimization-Using-Vector-Embeddings-and-Phidata.git
cd Resume-Optimization-Using-Vector-Embeddings-and-Phidata
```

---

✅ **Step 2: Create a Virtual Environment**

```bash
python -m venv env
source env/bin/activate  # Linux & MacOS
# OR
env\Scripts\activate     # Windows
```

---

✅ **Step 3: Install Dependencies**

```bash
pip install -r requirements.txt
```

---

✅ **Step 4: Set Up OpenAI API Key**

1. Create a `.env` file in the root directory:  

```
OPENAI_API_KEY=your_openai_api_key_here
```

2. Alternatively, you can set the environment variable in your terminal:

```bash
export OPENAI_API_KEY=your_openai_api_key_here  # MacOS/Linux
set OPENAI_API_KEY=your_openai_api_key_here     # Windows
```

---

✅ **Step 5: Run the Project**

```bash
python main.py
```

---
