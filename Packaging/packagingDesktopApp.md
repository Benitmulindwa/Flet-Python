# Packaging d'une application de Bureau

Flet Python app et toutes ses dépendances peuvent être regroupées dans un exécutable, et l'utilisateur peut l'exécuter sur son ordinateur sans avoir besoin d'installer un interpréteur Python ou des modules.

Flet utilise l'API **PyInstaller** pour empaqueter l'application Flet Python et toutes ses dépendances dans un seul package pour ```Windows, macOS et Linux```. Pour créer un package Windows, PyInstaller doit être exécuté sur Windows ; pour construire une application Linux, elle doit être exécutée sur Linux ; et pour construire une application macOS, elle doit être exécutée sur macOS.

### Commencez par installer PyInstaller :

```bash
pip install pyinstaller
```

Accédez au répertoire où se trouve votre fichier **.py** et construisez votre application avec la commande suivante :

```bash
flet pack votre_programme.py
```

Votre application **Flet** regroupée devrait maintenant être disponible dans le dossier **"dist"**. Essayez d'exécuter le programme pour voir s'il fonctionne.

### Sur macOS :

```bash
open dist/votre_programme.app
```

### Sur Windows :

``` bash
dist\votre_programme.exe
```

### Sur Linux :

```bash
dist/votre_programme
```

Maintenant, vous pouvez simplement compresser le contenu du dossier "dist" et le distribuer à vos utilisateurs !

Par défaut, cet exécutable a le même nom que le script Python. Vous pouvez le changer avec l'argument **--name** :

```bash
flet pack votre_programme.py --name nom_du_bundle
```
## Personnalisation de l'icône du package

L'icône par défaut du bundle est une disquette, ce qui peut être déroutant pour les développeurs plus jeunes qui ont manqué l'époque où les disquettes étaient utilisées pour stocker des données informatiques.

Vous pouvez remplacer l'icône par la vôtre en ajoutant l'argument **--icon** :

```bash
flet pack votre_programme.py --icon <votre-image.png>
```
PyInstaller convertira le PNG fourni dans un format spécifique à la plateforme (*.ico* pour Windows et *.icns* pour macOS), mais vous devez installer le module Pillow pour cela :

```bash
pip install pillow
```
## Packaging des ressources

Votre application Flet peut inclure des ressources. Si les ressources de l'application sont dans le dossier **"assets"** à côté de **votre_programme.py**, elles peuvent être ajoutées au package de l'application avec l'argument ```--add-data```, sur macOS/Linux :

```bash
flet pack votre_programme.py --add-data "assets:assets"
```
Sur Windows, **"assets;assets"** doit être délimité par ; :

```bash
flet pack votre_programme.py --add-data "assets;assets"
```
