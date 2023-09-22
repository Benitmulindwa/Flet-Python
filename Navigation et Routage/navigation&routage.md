# Navigation et Routage en flet

La navigation et le routage sont des fonctionnalités essentielles des applications à page unique (SPA). La navigation et le routage permettent d'organiser l'interface utilisateur de l'application en pages virtuelles (vues) et de "naviguer" entre elles, tout en reflétant l'état actuel de l'application dans l'URL.

### Voici un résumé des concepts et des étapes clés associées à la navigation et au routage dans Flet :

Route de page : Une route de page est une partie de l'URL de l'application après le symbole #. Par exemple, /store, /authors/1/books/2 sont des routes de page.

Route par défaut : Si l'utilisateur ne définit pas de route dans l'URL de l'application, la route par défaut est /. Toutes les routes commencent par /.

Obtention de la route de l'application : Vous pouvez obtenir la route actuelle de l'application en lisant la propriété page.route. Par exemple :

```python

import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(f"Route initiale : {page.route}"))

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
```
En modifiant la partie de l'URL après # en /test et en appuyant sur Entrée, vous verrez "Route initiale : /test".

Gestion des changements de route : Vous pouvez gérer les changements de route en définissant un gestionnaire d'événements page.on_route_change. Par exemple :

```python
import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(f"Route initiale : {page.route}"))

    def route_change(e: ft.RouteChangeEvent):
        page.add(ft.Text(f"Nouvelle route : {e.route}"))

    page.on_route_change = route_change
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
```
Maintenant, essayez de mettre à jour le hachage de l'URL quelques fois et utilisez les boutons Précédent/Suivant du navigateur ! Vous devriez voir un nouveau message ajouté à la page à chaque fois que la route change.

Changement de route programmable : Vous pouvez changer la route programmable en mettant à jour la propriété page.route. Par exemple :

```python

import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(f"Route initiale : {page.route}"))

    def route_change(e: ft.RouteChangeEvent):
        page.add(ft.Text(f"Nouvelle route : {e.route}"))

    def go_store(e):
        page.route = "/store"
        page.update()

    page.on_route_change = route_change
    page.add(ft.ElevatedButton("Aller au magasin", on_click=go_store))

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
```
Cliquez sur le bouton "Aller au magasin", et vous verrez que l'URL de l'application est modifiée et qu'un nouvel élément est ajouté à l'historique du navigateur. Vous pouvez utiliser le bouton "Retour" du navigateur pour naviguer vers une route précédente.

Vues de page : Flet's Page n'est plus simplement une seule page, mais un conteneur pour des vues empilées les unes sur les autres, comme un sandwich. Chaque vue représente une étape de l'historique de la navigation.

Création de vues lors du changement de route : Pour créer une navigation fiable, il doit y avoir un seul endroit dans le programme qui construit une liste de vues en fonction de la route actuelle. Cela garantit que l'historique de navigation (représenté par la liste de vues) dépend de la route actuelle. Ce lieu est le gestionnaire d'événements page.on_route_change.

Voici un exemple complet qui vous permet de naviguer entre deux pages :

```python

import flet as ft

def main(page: ft.Page):
    page.title = "Exemple de routes"

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Application Flet"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Visiter le magasin", on_click=lambda _: page.go("/store")),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Magasin"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Retour à l'accueil", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
```
Essayez de naviguer entre les pages en utilisant les boutons "Visiter le magasin" et "Retour à l'accueil", les boutons Précédent/Suivant du navigateur, en modifiant manuellement la route dans l'URL, cela fonctionne quelle que soit la méthode !

Modèles de route : Flet offre une classe utilitaire appelée TemplateRoute, basée sur la bibliothèque repath, qui permet de faire correspondre des routes de type ExpressJS et de les analyser, par exemple /account/:account_id/orders/:order_id.

Vous pouvez utiliser TemplateRoute pour faire correspondre des routes et analyser les paramètres de manière propre. Par exemple :

```python
troute = TemplateRoute(page.route)

if troute.match("/books/:id"):
    print("Vue du livre ID :", troute.id)
elif troute.match("/account/:account_id/orders/:order_id"):
    print("Compte :", troute.account_id, "Commande :", troute.order_id)
else:
    print("Route inconnue")
```
Cela permet de gérer différentes routes en fonction de leur structure.

Stratégie d'URL pour le web : Les applications web Flet prennent en charge deux méthodes de configuration de la gestion des URL :

Path (chemin) : Les chemins sont lus et écrits sans dièse (#). Par exemple, fletapp.dev/path/to/view.
Hash (hachage) : Les chemins sont lus et écrits dans la partie fragment d'URL. Par exemple, ***fletapp.dev/#/path/to/view.***

Vous pouvez changer la stratégie d'URL en utilisant le paramètre route_url_strategy de la méthode flet.app(). Par exemple :

```python
ft.app(target=main, route_url_strategy="hash")
```
Cela vous permet de choisir si vous souhaitez utiliser des URL avec ou sans hachage pour la gestion des routes dans votre application web Flet.

La gestion des routes et de la navigation est essentielle pour créer des applications web interactives et à pages multiples. Avec Flet, vous pouvez facilement mettre en place des fonctionnalités de routage pour vos applications web et mobiles, en permettant aux utilisateurs de naviguer entre différentes vues et de conserver un historique de navigation cohérent.
