from backend.main import ChatBotBackend
from frontend.main import ChatBotFrontend


class ApplicationChatBot:

    @staticmethod
    def run_application(prompt: str, title: str, api_key: str):
        backend = ChatBotBackend(api_key=api_key)
        custom_chat = backend.custom_chat(prompt=prompt)
        frontend = ChatBotFrontend(title=title)
        demo = frontend.open_demo(function=custom_chat)
        demo.launch(share=True)

if __name__ == "__main__":
    while True:
        api_key = str(input("Please set your own api key: "))
        a = ApplicationChatBot().run_application(prompt="Hello", title="xd", api_key=api_key)


