import requests
from decouple import config

CHAT_GPT_ENDPOINT = "https://api.openai.com/v1/chat/completions"

OPEN_AI_API_KEY = config('OPEN_AI_API_KEY')


data = {
  "model": "gpt-3.5-turbo",
  "messages": [{"role": "user", "content": "This is a test!"}]
}


headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + OPEN_AI_API_KEY
}

req = requests.post(CHAT_GPT_ENDPOINT, headers=headers, json=data)
print(req.json())
