import openai

class ChatBot:
    def __init__(self):
        openai.api_key = "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"

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
    response = chatbot.get_response("Write a joke about ghosts.")
    print(response)