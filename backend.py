import openai
import os
from dotenv import load_dotenv

load_dotenv()

class ChatBot:
    def __init__(self):
        openai.api_key = os.environ.get("OPENAI_API_KEY")

    def get_response(self, user_input):
        response = openai.completions.create(
            model="text-davinci-003",
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5
        ).choices[0].text
        return response

if __name__ == '__main__':
    chatbot = ChatBot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)