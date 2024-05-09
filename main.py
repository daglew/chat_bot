from backend.main import ChatBotBackend
from frontend.main import ChatBotFrontend


class ApplicationChatBot:

    @staticmethod
    def run_application(prompt: str, title: str):
        backend = ChatBotBackend()
        custom_chat = backend.custom_chat(prompt=prompt)
        frontend = ChatBotFrontend(title=title)
        demo = frontend.open_demo(function=custom_chat)
        demo.launch()


a = ApplicationChatBot().run_application(prompt="Hello", title="xd")


