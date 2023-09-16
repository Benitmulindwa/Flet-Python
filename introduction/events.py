import flet as ft


def main(page: ft.Page):
    page.window_width = 390
    page.window_height = 844

    def add_clicked(e):
        task = ft.Checkbox(label=new_task.value)
        # On ajoute une nouvelle tache si le champ de saisi n'est pas vide
        if new_task.value != "":
            page.add(task)
            new_task.value = ""
            new_task.focus()
            new_task.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=250)
    page.add(ft.Row([new_task, ft.ElevatedButton("Ajoute", on_click=add_clicked)]))


ft.app(target=main)
