from flet import *
from time import sleep


def main(page: Page):
    page.theme_mode = "light"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    # page.on_resize = lambda e: print(page.width)

    def on_login_event(e):
        pass

    #
    def on_hover_event(e, BGCOLOR: str, CONTENTCOLOR: str):
        if e.data == "true":
            e.control.bgcolor = BGCOLOR
            e.control.scale = 1.04
            e.control.border = border.all(color=BGCOLOR)
            e.control.content.controls[0].content.color = CONTENTCOLOR
            e.control.content.controls[1].color = CONTENTCOLOR
        else:
            e.control.bgcolor = "transparent"
            e.control.scale = 1.0
            e.control.border = (
                border.all(color="black")
                if BGCOLOR == "#acd8a7"
                else border.all(color="transparent")
            )
            e.control.content.controls[0].content.color = "black"
            e.control.content.controls[1].color = "black"

        e.control.update()

    # When the window is closed
    def on_close_event(e):
        # login container is updated
        login_container.content = Row(
            [
                Container(
                    Icon(icons.PERSON_2_OUTLINED, color="black"),
                    margin=margin.only(left=15),
                ),
                Text("Login", size=16, weight=FontWeight.BOLD),
            ],
            spacing=0,
        )
        login_container.height = 30
        login_container.width = 100

        # alignment=alignment.center,
        login_container.border = border.all(width=1.2, color="black")
        login_container.border_radius = 10

        login_container.on_hover = lambda e: on_hover_event(e, "#acd8a7", "#276221")
        login_container.on_click = animate_container
        login_container.left = 320
        login_container.update()

        # The main container is moved to its initial position
        login_container.top = page.height // 2
        login_container.left = page.width // 2
        page.update()

    def animate_container(e):
        # Change the main container's position
        login_container.top = 150
        login_container.left = page.width // 2 - 100
        page.update()
        sleep(0.5)  # A delay of 500ms before the container reaches the top and opens up
        login_container.width = 350
        login_container.height = 270
        login_container.border_radius = 20
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
                    border_radius=10,
                    margin=margin.only(left=15, top=15),
                    alignment=alignment.center,
                    data="clase",
                    on_click=on_close_event,
                    on_hover=lambda e: on_hover_event(e, "#ffcbd1", "#c30010"),
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
                        offset=transform.Offset(1, 0),
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
                # Submit button
                Container(
                    Row(
                        [
                            Container(
                                Text("Continue", size=16, weight=FontWeight.BOLD),
                                padding=padding.only(right=0),
                                alignment=alignment.center_right,
                            ),
                            Icon(icons.LOGIN_OUTLINED, color="black"),
                        ],
                        spacing=0,
                    ),
                    # expand=True,
                    height=30,
                    width=110,
                    border_radius=10,
                    border=border.all(width=1.2, color="transparent"),
                    # alignment=alignment.center,
                    margin=margin.only(left=220),
                    padding=padding.only(left=7),
                    on_click=on_login_event,
                    on_hover=lambda e: on_hover_event(e, "#cce7c9", "#276221"),
                ),
            ],
            horizontal_alignment=CrossAxisAlignment.START,
        )
        login_container.update()
        sleep(0.5)
        login_container.content.controls[2].content.offset = transform.Offset(0, 0)
        login_container.content.controls[2].content.update()
        login_container.update()
        # page.update()

    # Main container
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
        # expand=True,
        width=100,
        height=30,
        left=page.width // 2,
        top=page.height // 2,
        bgcolor="transparent",
        animate_position=500,
        border_radius=10,
        alignment=alignment.center,
        border=border.all(width=1.2, color="black"),
        on_hover=lambda e: on_hover_event(e, "#acd8a7", "#276221"),
        on_click=animate_container,
    )
    page.add(
        Stack(
            [login_container],
            alignment=alignment.center,
            height=page.width,
        ),
    )
    page.update()


app(target=main)
