# Introduction au développement d'applications avec Flet en Python

Ce guide vous aidera à démarrer avec le développement d'applications Flet en utilisant Python. Flet est un framework Python pour créer des interfaces utilisateur interactives. Vous n'avez pas besoin d'être un expert en développement front-end, mais une connaissance de base de Python et de la programmation orientée objet est recommandée.

## Installation du module Flet

Flet nécessite Python 3.7 ou une version ultérieure. Pour commencer à utiliser Flet, vous devez d'abord installer le module Flet à l'aide de pip :

```bash
pip install flet
```

# Contrôles

Les interfaces utilisateur des applications Flet sont construites à partir de contrôles (widgets). Les contrôles sont des objets Python qui représentent des éléments de l'interface utilisateur(text, bouton, champ de saisi,...). Vous pouvez créer des contrôles en utilisant des constructeurs avec des paramètres correspondant à leurs propriétés.

### Exemple:

```python
t = ft.Text(value="Hello, world!", color="green")
```

## Propriétés des contrôles : 

Vous pouvez modifier les propriétés des contrôles pour les personnaliser. Par exemple, vous pouvez définir la couleur du texte d'un contrôle **Text** en utilisant la propriété color. 
Pour rendre un contrôle visible, ajoutez-le à la liste des contrôles de la page (**page.add()**) et appelez **page.update()** pour envoyer les modifications à l'interface utilisateur.
### Exemple:

```python
page.add(t)  #cette ligne de code permet d'afficher 'Hello, world!' en vert sur l'ecran
```
[Ici](controls.py) il y a le fichier d'exemple. 

## Contrôles de conteneur :

Certains contrôles, comme **Row** et **Column**, agissent comme des conteneurs pour d'autres contrôles. Vous pouvez organiser les contrôles à l'intérieur de ces conteneurs pour créer des mises en page plus complexes.

Nous pouvons aligner un champ de text et un text sur une meme ligne(row), en faisant:

```python
import flet as ft

def main(page: ft.Page):
    txtfield = ft.TextField(hint_text = "Ajoutez une nouvelle tache", height=30, width=200)
    txt = ft.Text(value = "Ajouter")
    page.add( ft.Row([ txtfield, txt ]))
ft.app(target = main)
```
Dans ce precedent code, le contrôle *row* permet d'aligner, les autres contrôles(txtfield et txt) horizontalement. Le contrôle *column* quand à lui permet d'organiser d'autres contrôles verticalement.

# Les boutons:

En Flet, les boutons sont des éléments d'interface utilisateur interactifs couramment utilisés pour déclencher des actions lorsque l'utilisateur les clique.

## ElevetedButton

```python
import flet as ft

def main(page: ft.Page):
    # Créer un bouton avec du texte
    basic_button = ft.ElevatedButton("Cliquez-moi !")
    page.add(basic_button)
ft.app(target=main)
```
## IconButton

Le bouton d'icône(**IconButton**) en Flet vous permet d'afficher une icône au lieu de du texte.
Vous pouvez l'utiliser pour des actions spécifiques qui sont mieux représentées par des icônes.
La classe ft.IconButton est utilisée pour créer des boutons d'icône.

```python
import flet as ft

# Créer un bouton d'icône avec une icône spécifiée
icon_button = ft.IconButton(ft.icons.ADD)
page.add(icon_button)
```
## Gestion des evenements en Flet:

En programmation, un événement est un signal qu'un composant génère pour indiquer qu'une action spécifique s'est produite(l'appui d'un bouton). Les événements sont couramment utilisés pour gérer les interactions utilisateur, les entrées de données, les réponses aux actions de l'utilisateur et bien plus encore.

Les gestionnaires d'événements sont des fonctions qui seront exécutées lorsque le bouton est cliqué.
Vous pouvez spécifier un gestionnaire d'événements en utilisant l'argument __on_click__ lors de la création du bouton.

```python

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

```
