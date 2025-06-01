import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="SmartSDLC", layout="wide")
st.title("🤖 SmartSDLC - AI-enhanced Software Development Life Cycle")

# Text input
requirement = st.text_area("📝 Enter your software requirement (in plain English):", height=200)

# Prompt template
def generate_code_and_tests(requirement_text):
    system_prompt = (
        "You are an expert software engineer and technical writer. "
        "Given a software requirement, you will produce the following:\n\n"
        "1. A clear user story in the format: 'As a [role], I want to [goal] so that [benefit].'\n"
        "2. Python code that implements the feature.\n"
        "3. Unit test code using unittest.\n\n"
        "Return the output in the following format:\n"
        "### User Story\n<user_story>\n\n### Code\n<code>\n\n### Unit Test\n<unit_test_code>"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": requirement_text}
        ],
        temperature=0.5,
        max_tokens=1000
    )

    return response['choices'][0]['message']['content']

# Generate button
if st.button("🚀 Generate Code & Tests"):
    if not requirement.strip():
        st.warning("Please enter a requirement first.")
    else:
        with st.spinner("Generating with GPT-4..."):
            output = generate_code_and_tests(requirement)

        # Display sections
        if "### User Story" in output:
            parts = output.split("###")
            for part in parts:
                if "User Story" in part:
                    st.subheader("🧩 User Story")
                    st.code(part.replace("User Story", "").strip(), language="markdown")
                elif "Code" in part:
                    st.subheader("💻 Python Code")
                    st.code(part.replace("Code", "").strip(), language="python")
                elif "Unit Test" in part:
                    st.subheader("🧪 Unit Test")
                    st.code(part.replace("Unit Test", "").strip(), language="python")
        else:
            st.error("Unexpected response format. Please try again or check your prompt.")
