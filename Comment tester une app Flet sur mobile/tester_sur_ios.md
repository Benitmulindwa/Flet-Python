# Comment tester votre application Flet sur iOS :

1. **Installez l'application [Flet](https://apps.apple.com/app/flet/id1624979699)** sur votre appareil iOS. Vous utiliserez cette application pour voir comment fonctionne votre projet Flet sur votre iPhone ou iPad. Vous pouvez la télécharger depuis l'[App Store](https://apps.apple.com/app/flet/id1624979699).

*Assurez-vous que votre appareil iOS et votre ordinateur sont connectés au même réseau Wi-Fi ou au même réseau local. Cela garantira la communication entre les deux.*

2. **Sur votre ordinateur, vous devez avoir *Python 3.7* ou une version ultérieure installée.** Si ce n'est pas le cas, vous devrez l'installer.

```bash
pip install flet --upgrade
```
Créez un nouveau projet Flet en exécutant la commande suivante :

```bash
flet create my-app
cd my-app
```
3. **Exécutez la commande suivante pour démarrer le serveur de développement Flet avec votre application:**

```bah
flet run --ios
```

*Un code QR avec l'URL de votre projet encodée sera affiché dans le terminal.*

4. **Scannez ce code QR  avec votre appareil iOS, et le lien s'ouvrira dans Flet.**

*Si une boîte de dialogue demandant l'autorisation d'accéder à votre réseau local s'affiche. Cliquez sur "Autoriser" et vous devriez voir votre application Flet s'exécuter sur votre appareil iOS.*

Pour revenir à l'onglet "Accueil", vous pouvez soit :

- Appuyer longuement n'importe où sur l'écran avec trois doigts.
Secouer votre appareil iOS.
- Vous pouvez également ajouter manuellement un nouveau projet en cliquant sur le bouton "+" et en saisissant son URL.

Consultez l'onglet "Galerie" de l'application Flet pour découvrir quelques exemples de projets Flet intéressants. Vous pouvez également explorer les exemples Flet pour voir davantage d'exemples.
