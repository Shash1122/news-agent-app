# News Agent App

A Flask-based AI news agent that fetches the latest news using **NewsAPI** and integrates with **SmolAgents** for AI-powered responses. Docker-ready for easy deployment.

---

## Features

- Fetches the latest news articles based on user queries.
- Uses `SmolAgents` with the `OpenAIServerModel` (`gemini-2.5-flash`).
- Easy-to-use Flask web interface.
- Dockerized for quick setup and deployment.

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Shash1122/news-agent-app.git
cd news-agent-app

### 2. Setup environment variables

Create a .env file
and add
OPENAI_API_KEY=your_google_api_key_here(gemini api key)
NEWS_API_KEY=your_news_api_key_here

### 3. Setup Virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

### 4. Install dependencies
pip install -r requirements.txt

### 5. Start the app
python app.py
