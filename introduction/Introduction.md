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
Here is a file [example](controls.py)

## Contrôles de conteneur :

Certains contrôles, comme **Row** et **Column**, agissent comme des conteneurs pour d'autres contrôles. Vous pouvez organiser les contrôles à l'intérieur de ces conteneurs pour créer des mises en page plus complexes.
