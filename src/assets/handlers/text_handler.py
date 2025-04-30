import flet as ft
from flet import Control, MouseCursor

class HoverLink(ft.Control):
    def __init__(self, text, url):
        super().__init__()
        self.text = text
        self.url = url
        self.color = ft.colors.BLUE

    def build(self):
        self.label = ft.Text(
            value=self.text,
            color=self.color,
            size=16
        )

        return ft.MouseCursor(
            on_enter=self.on_hover_enter,
            on_exit=self.on_hover_exit,
            child=ft.GestureDetector(
                on_tap=self.open_link,
                child=self.label,
            )
        )

    def on_hover_enter(self, e):
        self.label.color = "#004D00"  # Цвет при наведении
        self.update()

    def on_hover_exit(self, e):
        self.label.color = ft.colors.BLUE  # Обычный цвет
        self.update()

    def open_link(self, e):
        import webbrowser
        webbrowser.open(self.url)
