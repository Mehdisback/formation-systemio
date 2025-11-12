# `/deploy`

Déploie la documentation sur GitHub Pages.

```
/deploy [--force]
```

## Ce que fait cette commande
1. Build la documentation
2. Crée/met à jour la branche `gh-pages`
3. Push les fichiers statiques vers GitHub Pages
4. Affiche l'URL du site déployé

## Arguments
- `--force` (optionnel) : Force le déploiement (écrase l'historique gh-pages)

## Exemples
```
/deploy                  # Déploiement standard
/deploy --force          # Déploiement forcé (utile en cas de conflit)
```

## Prérequis
- ✅ Dépôt Git configuré avec remote origin
- ✅ GitHub Pages activé dans les settings du repo
- ✅ Permissions push sur le dépôt
- ✅ Tous les changements locaux commités

## Workflow recommandé
1. `/serve` - Tester localement
2. `/build` - Vérifier le build
3. Commit des changements
4. `/deploy` - Déployer sur GitHub Pages
5. Attendre 1-2 minutes pour la mise à jour
6. Vérifier le site en production

## Notes importantes
⚠️ **Cette commande nécessite confirmation** car elle pousse vers GitHub

Le déploiement automatique via GitHub Actions est recommandé pour la production. Cette commande est utile pour :
- Tests de déploiement
- Déploiements urgents
- Déploiements hors workflow CI/CD

## En cas d'erreur
- **Permission denied** : Vérifier les droits Git
- **gh-pages conflict** : Utiliser `--force`
- **Build failed** : Corriger avec `/build` d'abord
