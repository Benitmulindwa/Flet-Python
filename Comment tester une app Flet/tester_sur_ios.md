Ce guide explique comment tester une application Flet sur un appareil iOS, comme un iPhone ou un iPad. Voici les étapes à suivre pour tester votre application Flet sur iOS :

Installez l'application Flet sur votre appareil iOS. Vous utiliserez cette application pour voir comment fonctionne votre projet Flet sur votre iPhone ou iPad. Vous pouvez la télécharger depuis l'App Store.

Assurez-vous que votre appareil iOS et votre ordinateur sont connectés au même réseau Wi-Fi ou au même réseau local. Cela garantira la communication entre les deux.

Sur votre ordinateur, vous devez avoir Python 3.7 ou une version ultérieure installée. Si ce n'est pas le cas, vous devrez l'installer.

Créez un nouvel environnement virtuel (virtual environment). Si vous utilisez macOS, Linux ou Windows, vous pouvez utiliser les commandes suivantes pour créer un environnement virtuel :

Pour macOS et Linux :

bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
Pour Windows :

Copy code
python.exe -m venv .venv
.venv\Scripts\activate.bat
Mettez à jour la bibliothèque Flet en exécutant la commande suivante :

css
Copy code
pip install flet --upgrade
Vérifiez que Flet a été installé avec succès et que la CLI de Flet est disponible dans votre chemin d'accès (PATH) en exécutant la commande suivante :

css
Copy code
flet --version
Créez un nouveau projet Flet en exécutant la commande suivante :

perl
Copy code
flet create my-app
cd my-app
Exécutez la commande suivante pour démarrer le serveur de développement Flet avec votre application :

arduino
Copy code
flet run --ios
Un code QR avec l'URL de votre projet encodée sera affiché dans le terminal.

Ouvrez l'application "Caméra" sur votre appareil iOS, pointez la caméra vers le code QR et cliquez sur le lien "Ouvrir dans Flet".

Une boîte de dialogue demandant l'autorisation d'accéder à votre réseau local s'affichera. Cliquez sur "Autoriser" et vous devriez voir votre application Flet s'exécuter sur votre appareil iOS.

Essayez de mettre à jour le fichier main.py. Par exemple, remplacez un message de salutation dans un contrôle Text. L'application sera instantanément actualisée sur votre appareil iOS.

Pour revenir à l'onglet "Accueil", vous pouvez soit :

Appuyer longuement n'importe où sur l'écran avec trois doigts.
Secouer votre appareil iOS.
Vous pouvez également ajouter manuellement un nouveau projet en cliquant sur le bouton "+" et en saisissant son URL.

Test rapide : Il existe un projet Flet appelé "Counter" hébergé sur Internet que vous pouvez ajouter à l'application Flet pour vous assurer que tout fonctionne. L'URL du projet est la suivante : https://flet-counter-test-ios.fly.dev

Consultez l'onglet "Galerie" de l'application Flet pour découvrir quelques exemples de projets Flet intéressants. Vous pouvez également explorer les exemples Flet pour voir davantage d'exemples.

En suivant ces étapes, vous pourrez tester et développer des applications Flet sur votre appareil iOS.
