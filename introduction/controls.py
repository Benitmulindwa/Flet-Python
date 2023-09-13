import flet as ft

def main(page:ft.Page):

    page.title='Flet app' # Le titre de l'application

    page.bgcolor='white' # La couleur du arrière-plan

    # Cree un champ de texte
    champ = ft.TextField(value="", width=200, height=30 )

    # cree un text
    text = ft.Text("Add a new task", color='black')

    # Tous les 'controles' sont ajoutés à la page, pourque celles-ci puisses s'afficher à l'ecran
    page.add(
        champ,
        text, 
        )

ft.app(target=main)