import requests
import json

def generate_response(user_prompt):
    """
    Generates a response from the AI model using the OpenRouter API.
    """

    API_URL = "https://openrouter.ai/api/v1/chat/completions"
    API_KEY = "<>"

    HEADERS = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    PAYLOAD = {
        "model": "qwen/qwen2.5-vl-72b-instruct:free",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": f'{user_prompt}'},
                ],
            }
        ],
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, data=json.dumps(PAYLOAD))
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
