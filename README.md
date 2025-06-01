# 🤖 SmartSDLC – AI-enhanced Software Development Life Cycle

SmartSDLC is a Streamlit-based AI tool that turns plain English software requirements into:
- 📜 User Stories
- 💻 Python Implementation Code
- 🧪 Unit Tests using `unittest`

Built for developers, product managers, and hackathon teams to **accelerate early-stage software planning and prototyping**, this tool uses open-source Hugging Face models to generate high-quality code without relying on paid APIs like OpenAI.

---

## 🚀 Features

✅ Input software requirements in plain English  
✅ Get structured User Stories automatically  
✅ Instantly generate Python code & test cases  
✅ Powered by Hugging Face (`flan-t5-base`)  
✅ No OpenAI or external cloud dependency  
✅ Intuitive UI with [Streamlit](https://streamlit.io)

---

## 🧠 How It Works

1. ✍️ You enter your requirement (e.g., "Allow users to register and log in").
2. 🧠 The AI model generates:
    - A user story
    - Python code (e.g., with `Flask`)
    - Corresponding `unittest` test cases
3. ⚙️ Streamlit shows the result in three separate sections.

---

## 🛠️ Setup Instructions

### 🔧 Prerequisites
- Python 3.7+
- Hugging Face account + API token (free)

### 📦 Installation

```bash
# Clone the repo
git clone https://github.com/Rishika14104/SmartSDLC
cd SmartSDLC

# Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# output:

![Image](https://github.com/user-attachments/assets/95de8370-b2f6-41ef-95d3-75b02bd505d5)

![Image](https://github.com/user-attachments/assets/9f9406cd-8e7e-436f-82c1-0c033ebb23ee)

