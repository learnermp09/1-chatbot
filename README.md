# 🤖 ThinkChain - An AI Chatbot

ThinkChain is an AI-powered conversational assistant built using **LangChain**, **Groq**, and **Streamlit**. The application enables users to interact with a large language model through a simple and intuitive web interface.

## 🚀 Live Demo

**Streamlit App:** [https://thinkchain.streamlit.app/]

## 📌 Features

- Interactive AI chatbot interface
- Powered by Groq's high-performance LLM inference
- Built using LangChain's chain architecture
- Simple and responsive Streamlit UI
- Optional LangSmith tracing support for observability and debugging
- Secure API key management using Streamlit Secrets

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Groq API
- LangSmith (Optional)

## 📂 Project Structure

```text
AgentForge/
│
├── chatbot.py          # Main Streamlit application
├── requirements.txt    # Project dependencies
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-github-username>/1-chatbot.git
cd 1-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file locally:

```env
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
```

> Note: Never commit your `.env` file to GitHub.

### 5. Run the application

```bash
streamlit run chatbot.py
```

## 🔐 Deployment

The application is deployed on Streamlit Community Cloud.

For production deployment:

- API keys are stored securely using Streamlit Secrets.
- No credentials are exposed in the repository.
- GitHub Push Protection is enabled to prevent accidental secret leaks.

## 🧠 How It Works

1. User enters a question through the Streamlit interface.
2. LangChain formats the prompt.
3. The prompt is sent to the Groq-hosted Qwen model.
4. The model generates a response.
5. The response is displayed back to the user.

## 📸 Application Preview

<img width="1858" height="782" alt="image" src="https://github.com/user-attachments/assets/cbe2ebf3-b5c3-42ad-bd8f-d8ccdcbf9c70" />


## 🎯 Future Enhancements

- Chat history support
- Multi-turn conversations
- Retrieval-Augmented Generation (RAG)
- Document Q&A
- Tool-using AI Agents
- Memory-enabled conversations

## 👨‍💻 Author

**Mrityunjay Pathak**

- GitHub: https://github.com/learnermp09
- LinkedIn: [https://www.linkedin.com/in/mrityunjay-pathak-74151aa/]

## 📜 License

This project is licensed under the MIT License.
