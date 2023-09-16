import flet as ft


# Fonction principale de l'application
def main(page: ft.Page):
    # Définit le titre de la page
    page.title = "Flet app"

    # Définit la couleur de l'arrière-plan de la page
    page.bgcolor = "white"

    # Crée un champ de texte vide avec une largeur de 200 pixels et une hauteur de 30 pixels
    champ = ft.TextField(value="", width=200, height=30)

    # Crée un élément de texte avec le contenu "Add a new task" et une couleur de texte noire
    text = ft.Text("Afficher un text", color="black")

    # Ajoute les contrôles (champ de texte et texte) à la page pour qu'ils puissent s'afficher à l'écran
    page.add(
        champ,
        text,
    )


# Lance l'application Flet avec la fonction principale comme point d'entrée
ft.app(target=main)
