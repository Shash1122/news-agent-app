import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

from smolagents import CodeAgent, WebSearchTool
from smolagents import OpenAIServerModel
from smolagents import tool

load_dotenv()


@tool
def news_fetch_tool(topic: str) -> str:
    """
    This tool takes the topic as input and fetches the latest news related to the provided topic.

    Args:
        topic: The news topic to fetch.

    Returns:
        A formatted string containing the top 5 news articles.
    """
    api_key = os.getenv("NEWS_API_KEY")

    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "articles" not in data or not data["articles"]:
            return f"No news found for topic: {topic}"
        articles = [f"📰 {a['title']}\n{a.get('description', 'No description provided.')}" for a in data["articles"]]
        return "\n\n".join(articles)

    except Exception as e:
        return f"Error fetching news: {e}"


# --- 3. Initialize the Agent ---
print("Initializing AI Agent...")
model=OpenAIServerModel(model_id='gemini-2.5-flash',
                        api_base="https://generativelanguage.googleapis.com/v1beta/openai/",
                        api_key=os.getenv("GOOGLE_API_KEY")
)
agent=CodeAgent(tools=[news_fetch_tool, WebSearchTool()], model=model)

print("Agent Initialized Successfully!")

# --- 4. Create the Flask App ---
app = Flask(__name__)

@app.route("/")
def index():
    """Serve the main HTML file."""
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """Handle the chat request from the frontend."""
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    print(f"Received message: {user_message}")
    # Run the agent to get a response
    system_instruction = (
    "You are a News agent. Provide users with news based on their query. "
    "Format your answers clearly using Markdown."
)
    agent_response = agent.run(f"{system_instruction}User prompt:{user_message}")
    print(f"Agent response: {agent_response}")

    # Return the response as JSON
    return jsonify({"response": agent_response})

if __name__ == "__main__":
    app.run(debug=True)