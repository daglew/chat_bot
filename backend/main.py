from openai import OpenAI


class ChatBotBackend:
    def __init__(self):
        self.client = self.initialize_client()

    def initialize_client(self):
        return OpenAI(api_key="api key")

    def custom_chat(self, prompt: str):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response


if __name__ == "__main__":
    while True:
        a = ChatBotBackend()
        b = a.custom_chat(prompt="Hello")
