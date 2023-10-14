Vous pouvez publier une application Flet en tant que site web statique autonome (SPA) exécuté entièrement dans le navigateur avec Pyodide.

Flet statique vs côté serveur
Avantages de Flet statique :
Aucune latence entre les événements générés par l'utilisateur et les mises à jour de la page.
Hébergement économique, ne nécessitant pas de code côté serveur.
Meilleure évolutivité, car l'application Flet statique s'exécute entièrement dans le navigateur.
Inconvénients de Flet statique :
Temps de chargement plus lent en raison du téléchargement du moteur Python (Pyodide), des packages intégrés et du programme utilisateur.
Compatibilité Python limitée, certaines applications natives ne peuvent pas s'exécuter avec Pyodide.
Performances inférieures, Pyodide étant actuellement 3 à 5 fois plus lent que Python natif pour certaines tâches intensives.
Async ou non async ?
Les applications Flet, qu'elles soient asynchrones ou non, peuvent être publiées en tant que site web statique. Cependant, pour les applications asynchrones (utilisant asyncio), assurez-vous qu'elles sont bien définies comme telles.

Publier une application en tant que site web statique
Utilisez la commande suivante pour publier une application Flet en tant que site web statique :

bash
Copy code
flet publish <votre-app-flet.py>
Le site web statique est publié dans le répertoire ./dist.

Arguments optionnels de la commande :
--pre : autorise micropip à installer des packages Python pré-versionnés.
-a ASSETS_DIR, --assets ASSETS_DIR : chemin vers un répertoire d'assets.
--app-title APP_TITLE : titre de l'application.
--app-description APP_DESCRIPTION : description de l'application.
--base-url BASE_URL : URL de base pour l'application.
--web-renderer {canvaskit,html} : moteur web à utiliser.
--route-url-strategy {path,hash} : stratégie d'URL.
Test du site web
Vous pouvez tester un site web Flet publié en utilisant le module http.server intégré de Python :

bash
Copy code
python -m http.server --directory dist
Ouvrez ensuite http://localhost:8000 dans votre navigateur pour vérifier le site publié.

Chargement de packages
Vous pouvez charger des packages personnalisés depuis PyPI lors du démarrage de l'application en les répertoriant dans le fichier requirements.txt. Celui-ci doit être créé dans le même répertoire que <votre-app-flet.py>.

Stratégie d'URL
Les applications Flet prennent en charge deux modes de configuration du routage basé sur les URL :

Path (par défaut) : les chemins sont lus et écrits sans hachage.
Hash : les chemins sont lus et écrits dans le fragment de hachage.
Utilisez l'option --route-url-strategy pour spécifier la stratégie d'URL lors de la publication :

bash
Copy code
flet publish <votre-app-flet.py> --route-url-strategy hash
Moteur Web
Vous pouvez changer le moteur web par défaut "canvaskit" à "html" avec l'option --web-renderer :

```bash
flet publish <votre-app-flet.py> --web-renderer html
```
### Émojis en couleur

Pour activer les émojis en couleur, utilisez l'option ```--use-color-emoji``` :

```bash
flet publish <votre-app-flet.py> --use-color-emoji
```

### Hébergement du site dans un sous-répertoire

Pour héberger plusieurs applications Flet sur un seul domaine, chacune dans son propre sous-répertoire, publiez l'application avec l'option ```--base-url``` :

```bash

flet publish <votre-app-flet.py> --base-url <sous-repertoire>
```

## Déploiement du site

Déployez votre site statique sur n'importe quel hébergement gratuit tel que **GitHub Pages**, **Cloudflare Pages** ou **Vercel**.

Pour Cloudflare Pages, suivez les [étapes](https://dash.cloudflare.com/sign-up/pages) pour connecter votre dépôt Git ou télécharger directement vos actifs.

Dépannage
Lorsque l'application Flet s'exécute dans un navigateur, toutes ses instructions print() sont affichées dans l'onglet "Console" des outils de développement du navigateur. Utilisez print() ou le module logging pour
