import os
import requests

API_KEY = os.environ.get("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")

def get_response(message):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "You are a helpful chatbot."},
            {"role": "user", "content": message}
        ]
    }

    if not API_KEY:
        return "Error: GROQ_API_KEY is not set. Set it as an environment variable before running the app."

    try:
        response = requests.post(url, json=data, headers=headers, timeout=15)
    except requests.exceptions.RequestException as e:
        return f"Error: could not reach Groq API ({e})"

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.text}"
