
""" Flet Responsive Portfolio - Website"""

# modules
from math import pi
import os
from datetime import date
import flet as ft

from page_classes import (DynamicText, DynamicContainer)
from assets.texts.page_texts import *

# сonstants
VERTICAL = 3 * pi / 2
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LITE_GREEN = "#186318"
LITE_GREEN_OVER = "#00e600"
DARK_GREEN = "#004D00"
DARK_GREEN_CON = "#000000"
STORG_GREEN = "#42ff49"

FORES_GREEN = "#186318"
ELECTRIC_LIME = "#00e600"
DARK_FOREST = "#004D00"
STARLESS_NIGHT = "#000000"
LIGHT_MOSS = "#42ff49"

main_photo_path = os.path.join("img", "snake.png")

# functions
def _change_container_color(e):
    if e.control.bgcolor == FORES_GREEN:
        e.control.bgcolor = DARK_FOREST
        e.control.update()
    else:
        e.control.bgcolor = FORES_GREEN
        e.control.update()


def _change_text_color(e):
    if e.control.content.color == LITE_GREEN_OVER:
        e.control.content.color = STORG_GREEN
        e.control.update()
    else:
        e.control.content.color = LITE_GREEN_OVER
        e.control.update()


def _menu_bar_item(label: str, with_border=True, url=None):
    item = ft.Container(
        bgcolor="#186318",
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Text(value=label, rotate=VERTICAL, size=12),
        on_hover=_change_container_color,
        url=url,
    )

    if with_border:
        item.border = ft.border.only(bottom=ft.border.BorderSide(1, "#1c361c"))

    return ft.Row(expand=True, controls=[item])


def _menu_bar(page):
    return ft.Container(
        
        ft.Column(
            [
                _menu_bar_item("about_me", url="#"),
                _menu_bar_item("contacts", url="#"),
                _menu_bar_item("services", url="#", with_border=False),
            ],
            spacing=0,
        ),
        bgcolor=ft.Colors.YELLOW,
        col={"sm": 0, "md": 4, "xl": 2},
        height=page.height,
        
    )


def _create_skill_item(value):
    return ft.Container(
        ft.Text(
            value=value,
            color="white",
            size=14,
            weight=ft.FontWeight.W_300,
        ),
    )



def _create_work_item(value):
    return ft.Container(
        ft.Text(
            value=value,
            color=LITE_GREEN_OVER,
        ),
        on_hover=_change_text_color,
    )

LText = DynamicText()
LContainer = DynamicContainer()
RText = DynamicText()
RContainer = DynamicContainer()

def _main_window_left(page):
    return ft.Container(
        ft.Column(
            [
                ft.Stack(
                    [
                        LContainer.create_container(
                            ft.Column(
                                [
                                    ft.Container(
                                        LText.create_text(
                                            value="Hi, I'm",
                                            text_align="left",
                                            color="white",
                                            size=30,
                                        ),
                                        
                                    ),
                                    ft.Container(
                                        LText.create_text(
                                            value="Andy Lin",
                                            font_family="Poland",
                                            text_align="left",
                                            color="white",
                                            size=78,
                                        ),
                                        padding=ft.padding.only(top=30),
                                    ),
                                    ft.Container(
                                        LText.create_text(
                                            value="Python Developer | Problem Solver | Tech Enthusiast",
                                            text_align="left",
                                            color="white",
                                            size=20,
                                        ),
                                    ),
                                    ft.Container(
                                        LText.create_text(
                                            value=main_page_title_3,
                                            text_align="left",
                                            color="white",
                                            size=18,
                                            weight=ft.FontWeight.W_700,
                                        ),
                                    ),
                                    ft.Container(
                                        LText.create_text(
                                            value=main_page_title_4,
                                            text_align="left",
                                            color="white",
                                            size=16,
                                        ),
                                    ),
                                    ft.ElevatedButton(
                                        text="reach_to_me",
                                        # on_click=_reach_to_me_handler,
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
                                expand=False,
                                alignment=ft.MainAxisAlignment.CENTER,
                                
                            ),
                            
                            bgcolor="#0a0a0a",
                            padding=ft.padding.only(left=20, right=30),
                            alignment=ft.alignment.center,
                            expand=True,
                        ),
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        ),
        bgcolor=ft.Colors.YELLOW,
        col={"xs": 38, "sm": 38, "md": 17, "xl": 18},
        height=page.height,
)

def _main_window_right(page, photo):
    return ft.Container(
        ft.Column(
            [
                ft.Stack(
                    [
                        RContainer.create_container(
                            ft.Column(
                                [   
                                    ft.Container(
                                        ft.Row(
                                            [
                                                RContainer.create_container(
                                                    ft.Image(
                                                        src=photo,
                                                        height=160,
                                                        fit=ft.ImageFit.CONTAIN,
                                                    ),
                                                ),
                                                RContainer.create_container(
                                                    ft.Column(
                                                        [
                                                            ft.Text(
                                                                value="My Skill Set:",
                                                                # text_align="right",
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
                                                    padding=ft.padding.only(left=20),
                                                ),
                                            ],
                                        ),
                                    ),
                                    ft.Column(
                                        [
                                            ft.Container(
                                                ft.Text(
                                                    value="My latest works",
                                                    color="white",
                                                    size=18,
                                                    weight=ft.FontWeight.W_700,
                                                ),
                                                alignment=ft.alignment.top_center,
                                                margin=ft.margin.only(top=40),
                                            ),
                                            ft.Container(
                                                ft.Column(
                                                    [
                                                        _create_work_item("> Development of an add-on to the 1C configuration: Retail"),
                                                        _create_work_item("> Telegram bot with CRM for beauty salon (aiogram + PostgreSQL)"),
                                                        _create_work_item("> Commentary analysis on marketplaces - coursework (Python + ML)"),
                                                        _create_work_item("> Online store for wholesale of electronic cigarettes (Django + PosgreSQL)"),
                                                        _create_work_item("> Portfolio Website (Flet)"),
                                                        ft.Container(
                                                            ft.Text(
                                                                value="[view all]",
                                                                color=LITE_GREEN_OVER,
                                                            ),
                                                            expand=True,
                                                            alignment=ft.alignment.bottom_center,
                                                            on_hover=_change_text_color,
                                                        ),
                                                    ],
                                                    spacing=10,
                                                ),
                                                expand=True,
                                                alignment=ft.alignment.top_left,
                                                margin=ft.margin.only(top=7),
                                                bgcolor="#132612",
                                                
                                                border=ft.Border(
                                                    left=ft.BorderSide(width=2, color=LITE_GREEN_OVER),
                                                ),
                                                padding=ft.padding.symmetric(horizontal=20, vertical=20),
                                            ),
                                        ]
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            bgcolor=FORES_GREEN,
                            padding=ft.padding.only(left=30, right=20),
                            alignment=ft.alignment.center,
                            expand=True,
                        ),
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        ),
        bgcolor=ft.Colors.GREEN,
        col={"xs": 38, "sm": 38, "md": 17, "xl": 18},
        height=page.height,
        margin=ft.margin.all(0),
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
    

    def page_resize(e):
        page_width = page.width
        texts = LText.text_list
        l_containers = LContainer.container_list
        r_containers = RContainer.container_list

        if page_width <= 420:
            texts[1].size = page_width/8
        elif page_width <= 767 > 420:
            texts[1].size = page_width/10
        elif page_width <= 1100 and page_width > 767:
            texts[1].size = page_width/19
        else:
            texts[1].size = page_width/20
            
            print(texts[2].size)
            print(texts[1].size)

        l_containers[0].padding = ft.padding.only(left=texts[1].size/2.2, right=texts[1].size/2.2)
        l_containers[0].content.width = texts[1].size*7
        r_containers[0].width = l_containers[0].content.width*0.3
        r_containers[1].width = l_containers[0].content.width*0.7-10

        r_containers[2].padding = ft.padding.only(left=texts[1].size/2.2, right=texts[1].size/2.2)
        r_containers[2].content.width = texts[1].size*7

        texts[2].size = texts[1].size/3.8

        if page_width <= 767:
            menu_bar.visible = False
        else:
            menu_bar.visible = True

        print(page_width)
        page.update()
        
        
    page.on_resized = page_resize

    menu_bar = _menu_bar(page)
    main_window_left = _main_window_left(page)
    main_window_right = _main_window_right(page, main_photo_path)

    page.scroll = "auto"
    page.add(
        ft.Column(
            [
                ft.ResponsiveRow(
                    [
                        menu_bar,
                        main_window_left,
                        main_window_right,
                    ],
                    spacing=0,
                    run_spacing=0,
                    columns=38,
                ),
            ], 
            spacing=0,   
              
        ),
    )

    page_resize(None)

    

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets/")