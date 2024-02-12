from flet import *
import flet as ft



def main(page: Page):

    def on_pan_update(e: DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.delta_y)
        e.control.left = max(0, e.control.left + e.delta_x)
        e.control.update()

    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"


    page.bgcolor = "#c5b5b5"

    gd = ft.GestureDetector(
        mouse_cursor=MouseCursor.MOVE,
        drag_interval=10,
        on_vertical_drag_update=on_pan_update,
        left=100,
        top=100,
        content=ft.Container(
            width=150,
            height=150,
            border_radius=100,
            shadow=[
                ft.BoxShadow(
                    offset=ft.Offset(20, 20),
                    blur_radius=60,
                    color="#a79999",
                    blur_style=ft.ShadowBlurStyle.NORMAL,
                ),
                ft.BoxShadow(
                    offset=ft.Offset(-20, -20),
                    blur_radius=60,
                    color="#e2d0d0",
                    blur_style=ft.ShadowBlurStyle.NORMAL,
                ),
            ],
        ),
    )

    page.add(Stack([gd]))
    page.update()


if __name__ == "__main__":
    app(target=main)


# un texte avec du code en python
