import flet as ft
from flet import *
from time import sleep


def main(page: ft.Page):

    page.theme_mode = "light"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    def on_hover_event(e):
        if e.data == "true":
            e.control.bgcolor = "#acd8a7"
            e.control.border = border.all(color="#acd8a7")
            e.control.content.controls[0].content.color = "#276221"
            e.control.content.controls[1].color = "#276221"
        else:
            e.control.bgcolor = "transparent"
            e.control.border = border.all(color="black")
            e.control.content.controls[0].content.color = "black"
            e.control.content.controls[1].color = "black"

        e.control.update()

    def animate_container(e):
        login_container.top = 150
        login_container.left = 320
        page.update()
        sleep(0.5)
        login_container.width = 350
        login_container.height = 270
        login_container.on_hover = None
        login_container.on_click = None
        login_container.border = border.all(color="#c8c8c8")
        login_container.content = Column(
            [
                Container(
                    Row(
                        [
                            Container(
                                Icon(icons.CLOSE, color="black", size=18),
                                alignment=alignment.center,
                                margin=margin.only(left=15, top=1),
                            ),
                            Text("Close", size=16, weight=FontWeight.W_600),
                        ],
                        spacing=0,
                    ),
                    width=100,
                    height=30,
                    bgcolor="transparent",
                    border_radius=30,
                    margin=margin.only(left=0, top=15),
                    alignment=alignment.center,
                ),
                Container(
                    Text("Email:", weight=FontWeight.W_500), margin=margin.only(left=15)
                ),
                Container(
                    TextField(
                        border=None,
                        height=30,
                        bgcolor="#f0f0f0",
                        content_padding=8,
                        border_color="transparent",
                        focused_border_color="transparent",
                    ),
                    margin=margin.only(left=15, right=15),
                ),
                Container(
                    Text("Password:", weight=FontWeight.W_500),
                    margin=margin.only(left=15),
                ),
                Container(
                    TextField(
                        password=True,
                        height=30,
                        bgcolor="#f0f0f0",
                        content_padding=8,
                        border_color="transparent",
                        focused_border_color="transparent",
                    ),
                    margin=margin.only(left=15, right=15),
                ),
            ],
            # alignment=MainAxisAlignment.START,
            horizontal_alignment=CrossAxisAlignment.START,
        )
        login_container.update()
        page.update()

    login_container = Container(
        Row(
            [
                Container(
                    Icon(icons.PERSON_2_OUTLINED, color="black"),
                    margin=margin.only(left=15),
                ),
                Text("Login", size=16, weight=FontWeight.BOLD),
            ],
            spacing=0,
        ),
        expand=True,
        width=100,
        height=30,
        left=page.width // 2,
        top=page.height // 2,
        bgcolor="transparent",
        animate_position=500,
        border_radius=30,
        alignment=alignment.center,
        border=border.all(width=1.2, color="black"),
        on_hover=on_hover_event,
        on_click=animate_container,
    )
    page.add(
        Stack([login_container], alignment=alignment.center, height=page.width),
    )


ft.app(target=main)
