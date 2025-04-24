import streamlit as st
import fitz  # PyMuPDF
import datetime

required_skills = ['python', 'sql', 'machine learning', 'django', 'aws', 'html', 'css', 'javascript']

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def analyze_resume(text):
    found = []
    for skill in required_skills:
        if skill.lower() in text.lower():
            found.append(skill)
    missing = list(set(required_skills) - set(found))
    return found, missing

st.set_page_config(page_title="CloudResumeIQ", page_icon=":mag:", layout="centered")
st.title("AI-Powered Resume Analyzer")

st.write("Upload your resume (PDF only) and get a quick skill analysis.")

uploaded_file = st.file_uploader("Choose your resume file", type="pdf")

if uploaded_file is not None:
    with st.spinner("Analyzing your resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        found, missing = analyze_resume(resume_text)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        st.success("Analysis complete!")
        st.subheader("Result Summary")
        st.markdown(f"**Uploaded at:** {timestamp}")
        st.markdown(f"**Skills Found:** `{', '.join(found)}`")
        st.markdown(f"**Skills Missing:** `{', '.join(missing) if missing else 'None — Great resume!'}`")

        st.subheader("Extracted Resume Text")
        with st.expander("Click to view full resume text"):
            st.text(resume_text)
