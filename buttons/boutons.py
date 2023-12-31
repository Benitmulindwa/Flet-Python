import flet as ft


def main(page: ft.Page):
    page.window_width = 490
    page.window_height = 844

    def affiche(e):
        txt = ft.Text("Hello guys!")
        page.add(txt)
        page.update()

    # Créer un bouton avec du texte
    basic_button = ft.ElevatedButton("Cliquez-moi !", on_click=affiche)
    page.add(basic_button)


ft.app(target=main)
