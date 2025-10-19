# News Agent App

A Flask-based AI news agent that fetches the latest news using **NewsAPI** and integrates with **SmolAgents** for AI-powered responses. Docker-ready for easy deployment.

---

## Features

- Fetches the latest news articles based on user queries.
- Uses `SmolAgents` with the `OpenAIServerModel` (`gemini-2.5-flash`).
- Easy-to-use Flask web interface.

---

## How to Run

1. **Clone the repository**

```bash
git clone [https://github.com/Shash1122/news-agent-app.git](https://github.com/Shash1122/news-agent-app.git)
cd news-agent-app
```
---
2. **Set up environment variables**
Create a .env file in the project's root directory and add your API keys:

```bash
OPENAI_API_KEY="your_google_api_key_here" # Gemini API Key
NEWS_API_KEY="your_news_api_key_here"
```
3. **Set up a virtual environment**
Create and activate a new virtual environment:
```bash
# Create the environment
python -m venv venv

# Activate on Linux/Mac
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```
4. **Install dependencies**
Install all the required packages using the requirements.txt file:

```bash
pip install -r requirements.txt
```
5. **Start the app**
Run the Flask application:

```bash
python app.py
```
