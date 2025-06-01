import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_models():
    # Use t5-small for summarization (lightweight)
    summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")
    # Code generation model (still codet5-base, relatively small)
    text2code = pipeline("text2text-generation", model="Salesforce/codet5-base")
    return summarizer, text2code

summarizer, text2code = load_models()

st.title("SmartSDLC - AI-enhanced Software Development Life Cycle")

menu = ["Requirement Analysis", "Code Generation", "Code Review", "Test Case Generation"]
choice = st.sidebar.selectbox("Select Stage", menu)

if choice == "Requirement Analysis":
    st.header("Requirement Analysis & Summarization")
    req_text = st.text_area("Paste your software requirements here:")
    if st.button("Summarize Requirements"):
        if req_text.strip():
            summary = summarizer(req_text, max_length=50, min_length=20, do_sample=False)[0]['summary_text']
            st.success("Summary:")
            st.write(summary)
        else:
            st.warning("Please input requirements text.")

elif choice == "Code Generation":
    st.header("Generate Code from Requirements")
    req_text = st.text_area("Describe the functionality you want to implement:")
    if st.button("Generate Code"):
        if req_text.strip():
            generated = text2code(req_text, max_length=150)[0]['generated_text']
            st.code(generated, language="python")
        else:
            st.warning("Please input a description.")

elif choice == "Code Review":
    st.header("Automated Code Review")
    code = st.text_area("Paste your code here for review:")
    if st.button("Review Code"):
        if code.strip():
            issues = []
            if len(code.splitlines()) > 50:
                issues.append("Code is very long; consider modularizing.")
            if "TODO" in code:
                issues.append("Found TODO comments; consider completing before release.")
            if not issues:
                st.success("No obvious issues found.")
            else:
                st.warning("Review Comments:")
                for issue in issues:
                    st.write(f"- {issue}")
        else:
            st.warning("Please paste code to review.")

elif choice == "Test Case Generation":
    st.header("Generate Test Cases from Requirements")
    req_text = st.text_area("Paste the functionality or requirements:")
    if st.button("Generate Test Cases"):
        if req_text.strip():
            test_cases = [
                "Test valid input scenarios.",
                "Test invalid input handling.",
                "Test boundary conditions.",
                "Test error handling."
            ]
            st.write("Suggested Test Cases:")
            for tc in test_cases:
                st.write(f"- {tc}")
        else:
            st.warning("Please input requirements.")
