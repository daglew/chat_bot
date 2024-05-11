from openai import OpenAI, RateLimitError


class ChatBotBackend:
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = self.initialize_client()

    def initialize_client(self):
        return OpenAI(api_key=self.api_key)

    def custom_chat(self, prompt: str):
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
        except RateLimitError:
            response = None
        return response

