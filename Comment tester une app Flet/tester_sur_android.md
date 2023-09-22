# Comment tester son application Flet sur Android

1. **Installez l'application Flet sur votre appareil Android**. Vous utiliserez cette application pour voir comment fonctionne votre projet Flet sur votre appareil Android. Vous pouvez la télécharger depuis [Google Play](https://play.google.com/store/apps/details?id=com.appveyor.flet&pli=1).

2. **Assurez-vous que votre appareil Android et votre ordinateur sont connectés au même réseau Wi-Fi ou au même réseau local**. Cela garantira la communication entre les deux.

3. **Sur votre ordinateur**, vous devez avoir *Python 3.7* ou une version ultérieure installée. Si ce n'est pas le cas, vous devrez l'installer.

4. **Créez un nouveau projet Flet** en exécutant la commande suivante :

   ```bash
   flet create my-app
   
   cd my-app
   ```

5. **Exécutez la commande suivante pour démarrer le serveur de développement Flet avec votre application** :
   ```
   flet run --android
   ```

6. **Un code QR avec l'URL de votre projet encodée sera affiché dans le terminal**. 

7. **Scannez le code QR avec votre appareil Android**, pointez la caméra vers le code QR et cliquez sur l'URL pour l'ouvrir dans l'application Flet.

8. **Essayez de mettre à jour le fichier main.py**. Par exemple, remplacez un message de salutation dans un contrôle Text. L'application sera instantanément actualisée sur votre appareil Android.

9. Pour revenir à l'onglet "Accueil", vous pouvez soit :
    - Appuyer longuement n'importe où sur l'écran avec trois doigts.
    - Secouer votre appareil Android.

10. Vous pouvez également **ajouter manuellement un nouveau projet** en cliquant sur le bouton "+" et en saisissant son URL.

11. Consultez l'onglet "Galerie" de l'application Flet pour découvrir quelques exemples de projets Flet intéressants. Vous pouvez également explorer les exemples Flet pour voir davantage d'exemples.

En suivant ces étapes, vous pourrez tester et développer des applications Flet sur votre appareil Android.
