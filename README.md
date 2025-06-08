# SmartSDLC – AI-enhanced Software Development Life Cycle

✅ This is a Streamlit-based web application designed to assist software developers across various stages of the Software Development Life Cycle (SDLC) using a generative AI model.

## 🔍 Features

- **Requirement Analysis**  
  Summarize lengthy software requirement documents into clear, concise summaries.

- **Code Generation**  
  Automatically generate Python code snippets from functional requirements.

- **Code Review**  
  Review existing code for potential bugs, improvements, or best practices.

- **Test Case Generation**  
  Generate appropriate software test cases based on given requirements or functionality.

## 🧠 Model Used

This app uses the IBM Granite 3.3B Instruct model from Hugging Face:

ibm-granite/granite-3.3-2b-instruct


## 🧰 Tech Stack

- Python 🐍
- Streamlit 📊
- Hugging Face Transformers 🤗
- PyTorch 🔥
- Pyngrok 🌐 (for tunneling in Google Colab)
- Google Colab (for hosting & testing)

## 🚀 How to Run in Google Colab

1. **Install dependencies:**

!pip install streamlit transformers torch pyngrok accelerate sentencepiece

2. *Save your Streamlit code as Smart_app.py:**

%%writefile Smart_app.py

%%writefile "Smart_app.py"
import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("ibm-granite/granite-3.3-2b-instruct")
    model = AutoModelForCausalLM.from_pretrained("ibm-granite/granite-3.3-2b-instruct")
    instruct_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)
    return instruct_pipeline

model = load_model()

st.title("SmartSDLC - AI-enhanced Software Development Life Cycle")
st.write("✅ This app is running from Google Colab using Streamlit + ngrok!")

menu = ["Requirement Analysis", "Code Generation", "Code Review", "Test Case Generation"]
choice = st.sidebar.selectbox("Select Stage", menu)

def generate_response(prompt, max_tokens=200):
    output = model(prompt, max_new_tokens=max_tokens, do_sample=False)[0]['generated_text']
    return output.replace(prompt, "").strip()

if choice == "Requirement Analysis":
    st.header("Requirement Analysis & Summarization")
    req_text = st.text_area("Paste your software requirements here:")
    if st.button("Summarize Requirements"):
        if req_text.strip():
            prompt = f"Summarize the following software requirement:\n\n{req_text}\n\nSummary:"
            summary = generate_response(prompt, max_tokens=100)
            st.success("Summary:")
            st.write(summary)
        else:
            st.warning("Please input requirements text.")

elif choice == "Code Generation":
    st.header("Generate Code from Requirements")
    req_text = st.text_area("Describe the functionality you want to implement:")
    if st.button("Generate Code"):
        if req_text.strip():
            prompt = f"Generate Python code for the following functionality:\n\n{req_text}\n\nPython code:"
            code = generate_response(prompt, max_tokens=150)
            st.code(code, language="python")
        else:
            st.warning("Please input a description.")

elif choice == "Code Review":
   st.header("Automated Code Review")
   code = st.text_area("Paste your code here for review:")
   if st.button("Review Code"):
        if code.strip():
            prompt = f"Review the following Python code and list any issues or improvements:\n\n{code}\n\nReview:"
            review = generate_response(prompt, max_tokens=150)
            st.warning("Review Comments:")
            st.write(review)
        else:
            st.warning("Please paste code to review.")

elif choice == "Test Case Generation":
    st.header("Generate Test Cases from Requirements")
    req_text = st.text_area("Paste the functionality or requirements:")
    if st.button("Generate Test Cases"):
        if req_text.strip():
            prompt = f"Based on the following requirements, generate a list of software test cases:\n\n{req_text}\n\nTest Cases:"
            cases = generate_response(prompt, max_tokens=150)
            st.write("Suggested Test Cases:")
            st.write(cases)
        else:
            st.warning("Please input requirements.")

3. **Run the app with ngrok:**

from pyngrok import ngrok
import os

Run Streamlit app in background
os.system("streamlit run Smart_app.py --server.port 8501 &")

Wait a bit for the app to start
import time
time.sleep(5)

Open ngrok tunnel to the Streamlit app
public_url = ngrok.connect(8501)
print("🚀 Your SmartSDLC app is live at:", public_url)

4. **Click the public URL shown in the output to use the app.**

📁 Project Structure

├── Smart_app.py          # Streamlit app source code
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation

💡 Example Prompts

➤ Requirement Analysis

As an e-commerce platform user, I want to be able to add products to a shopping cart so that I can purchase multiple items at once. The cart should display all selected items, their quantities, prices, and a total price. Users should be able to update quantities, remove items, and proceed to a secure checkout process that supports multiple payment options. The system should validate product availability before confirming the order.

➤ Code Generation

Create a Python function that takes a list of numbers and returns a new list containing only the even numbers from the original list.

➤ Code Review

def calculate_area(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area

print(calculate_area(5))

➤ Test Case Generation

The system should allow users to register by providing a unique email and password. Upon successful registration, the user should receive a confirmation email. The system must validate the email format and ensure the password is at least 8 characters long.

# OUTPUT :










