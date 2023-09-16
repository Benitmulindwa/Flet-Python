import flet as ft


def main(page: ft.Page):
    page.title = "Compteur"
    page.window_width = 390
    page.window_height = 844

    txt_number = ft.Text(value="0", text_align="center", width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, icon_color="red", on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, icon_color="blue", on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(target=main)
