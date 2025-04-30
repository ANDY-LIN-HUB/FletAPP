import flet as ft


class DynamicText:
    def __init__(self):
        self.text_list = []

    def create_text(self, value, **kwargs):
        text = ft.Text(value=value, **kwargs)
        self.text_list.append(text)
        return text


class DynamicContainer:
    def __init__(self):
        self.container_list = []

    def create_container(self, content=None, **kwargs):
        container = ft.Container(content=content, **kwargs)
        self.container_list.append(container)
        return container