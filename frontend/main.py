import gradio


class ChatBotFrontend:
    def __init__(self, title: str):
        self.title = title

    def open_demo(self, function):
        return gradio.Interface(fn=function, inputs="text", outputs="text", title=self.title)

