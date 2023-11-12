import json
from openai import OpenAI

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

config = load_config()
client = OpenAI(api_key=config["openai_api_key"])

def get_chatgpt_response(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{"role": "user", "content": message}]
    )
    # Access the content attribute of the message
    return response.choices[0].message.content.strip()