import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_frameless = True
    page.window_always_on_top = True
    # to make page transparent
    # page.views[0].bgcolor = ft.colors.TRANSPARENT
    print(page.views)
    t = ft.Text("Hi", weight=ft.FontWeight.W_900, size=400)
    page.add(t)


ft.app(target=main)
