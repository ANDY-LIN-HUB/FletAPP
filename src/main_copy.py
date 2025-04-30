
""" Flet Responsive Portfolio - Website"""

# modules
from math import pi
import os
from datetime import date
import flet as ft
from flet import (
    Page, Column, Row, padding, margin, ResponsiveRow, border, Container, Text, 
    LinearGradient, transform, Rotate, ElevatedButton, Image, Stack
)
from assets.texts.page_texts import *

VERTICAL = 3 * pi / 2
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LITE_GREEN = "#186318"
LITE_GREEN_OVER = "#00e600"
DARK_GREEN = "#004D00"
DARK_GREEN_CON = "#000000"
STORG_GREEN = "#42ff49"

def _change_container_color(e):
    if e.control.bgcolor == LITE_GREEN:
        e.control.bgcolor = DARK_GREEN
        e.control.update()
    else:
        e.control.bgcolor = LITE_GREEN
        e.control.update()

def _change_text_color(e):
    if e.control.content.color == LITE_GREEN_OVER:
        e.control.content.color = STORG_GREEN
        e.control.update()
    else:
        e.control.content.color = LITE_GREEN_OVER
        e.control.update()


def _reach_to_me_handler():
    pass

def _open_work():
    pass


def _create_nav_item(label: str, with_border=True, url=None):
    item = Container(
        bgcolor="#186318",
        expand=True,
        alignment=ft.alignment.center,
        content=Text(value=label, rotate=VERTICAL, size=14),
        on_hover=_change_container_color,
        url=url,
    )

    if with_border:
        item.border = ft.border.only(bottom=ft.border.BorderSide(1, "#1c361c"))

    return Row(expand=True, controls=[item])


def _create_work_item(value):
    return Container(
        
        on_hover=_change_text_color,
        content=Text(
            value=value,
            color=LITE_GREEN_OVER,
        )
    )


def _create_skill_item(value):
    return Text(
        value=value,
        color="white",
        size=14,
        weight=ft.FontWeight.W_300,
    )



def main(page: ft.Page):
    page.spacing = 0
    page.padding = 0

    page.fonts = {
        "Poland": "https://raw.githubusercontent.com/ANDY-LIN-HUB/free-fonts/main/Poland_%D1%81an_into/PolandCanIntoBigWritingsOutline.otf",
        "Tektur": "https://raw.githubusercontent.com/ANDY-LIN-HUB/free-fonts/main/Tektur/Tektur-VariableFont.ttf",
    }

    page.title = "Flet Portfolio"
    page.theme = ft.Theme(font_family="Tektur")

    main_photo_path = os.path.join("img", "snake.png")

    _nav = Column(
        width=76,
        spacing=0,
        controls=[
            _create_nav_item("about_me", url="#"),
            _create_nav_item("contacts", url="#"),
            _create_nav_item("services", url="#", with_border=False),
        ],
    )

    _main_left = Column(
        expand=True,
        controls=[
            Stack(
                expand=True,
                controls=[
                    
                    Container(
                        bgcolor="#0a0a0a",
                        expand=True,
                        padding=ft.padding.only(left=60),
                        alignment=ft.alignment.center_left,
                        content=Column(
                            expand=False,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                Text(
                                    value="Hi, I'm",
                                    text_align="left",
                                    color="white",
                                    size=30,
                                ),
                                Container(
                                    padding=ft.padding.only(top=30),  
                                    content=Text(
                                        value="Andy Lin",
                                        font_family="Poland",
                                        text_align="left",
                                        color="white",
                                        size=78,
                                    ),
                                ),
                                Text(
                                    value="Python Developer | Problem Solver | Tech Enthusiast",
                                    text_align="left",
                                    color="white",
                                    size=20,
                                ),
                                Text(
                                    value=main_page_title_3,
                                    text_align="left",
                                    color="white",
                                    size=18,
                                    weight=ft.FontWeight.W_700,
                                ),
                                Text(
                                    value=main_page_title_4,
                                    text_align="left",
                                    color="white",
                                    size=16,
                                ),
                                ElevatedButton(
                                    text="reach_to_me",
                                    on_click=_reach_to_me_handler,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=0),
                                        overlay_color=DARK_GREEN, 
                                        color=ft.colors.WHITE,
                                        bgcolor=LITE_GREEN,
                                        text_style=ft.TextStyle(size=16),
                                    ),
                                    width=180,
                                ),
                            ],
                        ),
                    ),
                    Container(
                        content=Text(value=date.today().strftime("%d.%m.%Y"), color="white", opacity=0.5),
                        alignment=ft.alignment.top_center,
                        margin=ft.margin.only(top=20)
                    ),
                ],
            ),  
        ],
    )

    _main_right = Column(
        expand=True,
        controls=[
            Container(
                bgcolor="#186318",
                padding=ft.padding.only(top=0),
                expand=True,
                alignment=ft.alignment.top_right,
                content=Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        Row(
                            alignment=ft.MainAxisAlignment.END,
                            
                            controls=[
                                Container(
                                    padding=padding.only(left=60),
                                    alignment=ft.alignment.top_right,
                                    content=Image(
                                        src=main_photo_path,
                                        height=250,
                                        fit=ft.ImageFit.CONTAIN,
                                    ),
                                ),
                                Container(
                                    expand=True,
                                    margin=margin.only(right=60, left=30),
                                    content=Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.START,
                                        controls=[
                                            Text(
                                                value="My Skill Set:",
                                                text_align="right",
                                                color="white",
                                                size=18,
                                                weight=ft.FontWeight.W_700,
                                            ),
                                            _create_skill_item("- Develop backend systems (FastAPI, Django)"),
                                            _create_skill_item("- Work with databases (MySQL, SQLite, PostgreSQL)"),
                                            _create_skill_item("- Develop bots (Aiogram, Flet)"),
                                            _create_skill_item("- Integrate AI & ML tools"),
                                            
                                        ],
                                    ),
                                ),
                                
                            ],
                        ),
                        Column(
                            controls=[
                                Container(
                                    content=Text(
                                        value="My latest works",
                                        color="white",
                                        size=18,
                                        weight=ft.FontWeight.W_700,
                                    ),
                                    alignment=ft.alignment.top_center,
                                    margin=margin.only(top=40),
                                    
                                ),
                                Container(
                                    expand=True,
                                    alignment=ft.alignment.top_left,
                                    margin=ft.margin.only(top=7, right=60, left=60),
                                    bgcolor="#132612",
                                    height=230,
                                    border=ft.Border(
                                        left=ft.BorderSide(width=2, color=LITE_GREEN_OVER),
                                    ),
                                    padding=ft.padding.symmetric(horizontal=20, vertical=20),
                                    content=Column(
                                        spacing=10,
                                        controls=[
                                            _create_work_item("> Development of an add-on to the 1C configuration: Retail"),
                                            _create_work_item("> Telegram bot with CRM for beauty salon (aiogram + PostgreSQL)"),
                                            _create_work_item("> Commentary analysis on marketplaces - coursework (Python + ML)"),
                                            _create_work_item("> Online store for wholesale of electronic cigarettes (Django + PosgreSQL)"),
                                            _create_work_item("> Portfolio Website (Flet)"),
                                            Container(
                                                expand=True,
                                                alignment=ft.alignment.bottom_center,
                                                on_hover=_change_text_color,
                                                content=Text(
                                                    value="[view all]",
                                                    color=LITE_GREEN_OVER,
                                                    ),
                                            )
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        ],
    )

    _main_window = Row(expand=True, spacing=0)
    _main_window.controls.append(_main_left)
    _main_window.controls.append(_main_right)
    

    _main_layout = Row(expand=True, spacing=0)
    _main_layout.controls.append(_nav)
    _main_layout.controls.append(_main_window)

    def resize(e):
        pw = page.width
        if pw <= 1270 and pw > 800:
            print("ok_1")
        if pw <= 800 and pw > 400:
            text = _main_left.controls[0].controls[0].content.controls[1].content
            text.size = 30
            print("ok_2")

        page.update()

    

    page.add(_main_layout)
    page.on_resized = resize
    page.update()
    resize(None)

            
if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets/")