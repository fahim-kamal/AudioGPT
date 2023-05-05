import requests, os
from dotenv import load_dotenv

load_dotenv()

CHAT_GPT_ENDPOINT = "https://api.openai.com/v1/chat/completions"

OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")


def askChatGPT(text: str) -> str:
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": text}]
    }

    headers = {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + OPEN_AI_API_KEY
    }

    req = requests.post(CHAT_GPT_ENDPOINT, headers=headers, json=data)
    req = req.json()
    req = req['choices'][0]['message']['content']

    return req

    
