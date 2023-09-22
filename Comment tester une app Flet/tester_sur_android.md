Ce guide explique comment tester une application Flet sur un appareil Android. Voici les étapes à suivre pour tester votre application Flet sur Android :

1. **Installez l'application Flet sur votre appareil Android**. Vous utiliserez cette application pour voir comment fonctionne votre projet Flet sur votre appareil Android. Vous pouvez la télécharger depuis Google Play.

2. **Assurez-vous que votre appareil Android et votre ordinateur sont connectés au même réseau Wi-Fi ou au même réseau local**. Cela garantira la communication entre les deux.

3. **Sur votre ordinateur**, vous devez avoir Python 3.7 ou une version ultérieure installée. Si ce n'est pas le cas, vous devrez l'installer.

4. **Créez un nouvel environnement virtuel (virtual environment)**. Si vous utilisez macOS, Linux ou Windows, vous pouvez utiliser les commandes suivantes pour créer un environnement virtuel :

   - Pour macOS et Linux :
     ```
     python3 -m venv .venv
     source .venv/bin/activate
     ```

   - Pour Windows :
     ```
     python.exe -m venv .venv
     .venv\Scripts\activate.bat
     ```

5. **Mettez à jour la bibliothèque Flet** en exécutant la commande suivante :
   ```
   pip install flet --upgrade
   ```

6. **Vérifiez que Flet a été installé avec succès et que la CLI de Flet est disponible dans votre chemin d'accès (PATH)** en exécutant la commande suivante :
   ```
   flet --version
   ```

7. **Créez un nouveau projet Flet** en exécutant la commande suivante :
   ```
   flet create my-app
   cd my-app
   ```

8. **Exécutez la commande suivante pour démarrer le serveur de développement Flet avec votre application** :
   ```
   flet run --android
   ```

9. **Un code QR avec l'URL de votre projet encodée sera affiché dans le terminal**. 

10. **Ouvrez l'application "Caméra" sur votre appareil Android**, pointez la caméra vers le code QR et cliquez sur l'URL pour l'ouvrir dans l'application Flet.

11. **Essayez de mettre à jour le fichier main.py**. Par exemple, remplacez un message de salutation dans un contrôle Text. L'application sera instantanément actualisée sur votre appareil Android.

12. Pour revenir à l'onglet "Accueil", vous pouvez soit :
    - Appuyer longuement n'importe où sur l'écran avec trois doigts.
    - Secouer votre appareil Android.

13. Vous pouvez également **ajouter manuellement un nouveau projet** en cliquant sur le bouton "+" et en saisissant son URL.

14. **Test rapide** : Il existe un projet Flet appelé "Counter" hébergé sur Internet que vous pouvez ajouter à l'application Flet pour vous assurer que tout fonctionne. L'URL du projet est la suivante : https://flet-counter-test-ios.fly.dev

15. Consultez l'onglet "Galerie" de l'application Flet pour découvrir quelques exemples de projets Flet intéressants. Vous pouvez également explorer les exemples Flet pour voir davantage d'exemples.

En suivant ces étapes, vous pourrez tester et développer des applications Flet sur votre appareil Android.
