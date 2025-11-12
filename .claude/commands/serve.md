# `/serve`

Démarre le serveur de développement MkDocs avec live reload.

```
/serve [port]
```

## Ce que fait cette commande
1. Lance `mkdocs serve` sur le port spécifié (8000 par défaut)
2. Active le live reload automatique
3. Affiche l'URL locale pour accéder au site
4. Surveille les changements dans `docs/` et `mkdocs.yml`

## Arguments
- `port` (optionnel) : Port à utiliser (défaut: 8000)

## Exemples
```
/serve                   # Lance sur http://127.0.0.1:8000
/serve 8080              # Lance sur http://127.0.0.1:8080
```

## Conseils
- Laissez le serveur tourner pendant l'édition de contenu
- Les changements sont visibles immédiatement dans le navigateur
- Vérifiez la console pour les erreurs de build
- Testez toujours localement avant de commiter

## Workflow typique
1. `/serve` pour démarrer le serveur
2. Ouvrir http://127.0.0.1:8000 dans le navigateur
3. Éditer les fichiers `.md` dans `docs/`
4. Vérifier les changements en temps réel
5. Ctrl+C pour arrêter le serveur
