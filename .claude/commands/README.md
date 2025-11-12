# Commandes MkDocs Documentation

Commandes slash optimisées pour la gestion de documentation MkDocs Material.

## 🎯 Commandes disponibles

### Développement
- `/serve` - Lance le serveur de développement avec live reload
- `/build` - Build la documentation en site statique

### Déploiement
- `/deploy` - Déploie sur GitHub Pages (nécessite confirmation)

### Gestion de contenu
- `/add-guide` - Crée un nouveau guide avec template
- `/validate-docs` - Valide l'intégrité de la documentation
- `/check-links` - Vérifie tous les liens (internes et externes)

## 🔄 Workflow typique

### Édition de contenu
```
/serve                          # Démarre le serveur local
# Éditer les fichiers .md
# Vérifier dans le navigateur
/validate-docs                  # Valider avant commit
```

### Ajout d'un guide
```
/add-guide 11 "Titre du guide"  # Créer nouveau guide
/serve                          # Prévisualiser
/validate-docs                  # Valider
```

### Préparation déploiement
```
/build                          # Build local
/validate-docs --full           # Validation complète
/check-links                    # Vérifier les liens
# Commit des changements
/deploy                         # Déployer (si nécessaire)
```

## 📊 Fréquence recommandée

| Commande | Quand l'utiliser |
|----------|------------------|
| `/serve` | À chaque session d'édition |
| `/build` | Avant chaque commit |
| `/validate-docs` | Avant chaque commit |
| `/check-links` | Hebdomadaire ou après ajout de liens |
| `/deploy` | Uniquement si déploiement manuel nécessaire |
| `/add-guide` | Lors de l'ajout de nouveau contenu |

## 💡 Conseils d'utilisation

### Performance
- Laissez `/serve` tourner pendant l'édition (live reload)
- Utilisez `/validate-docs` sans `--full` pour les checks rapides
- `/check-links --external-only` est plus rapide que la vérification complète

### Qualité
- Toujours `/validate-docs` avant commit
- `/check-links` régulièrement (liens externes peuvent changer)
- `/build` pour détecter erreurs de compilation

### CI/CD
- Le déploiement automatique via GitHub Actions est recommandé
- `/deploy` manuel uniquement pour corrections urgentes
- Vérifications intégrées dans le workflow CI

## 🔧 Personnalisation

Pour ajouter une nouvelle commande :
1. Créer `nouvelle-commande.md` dans ce dossier
2. Suivre le format des commandes existantes
3. Tester avec `/nouvelle-commande`
4. Documenter ici

## 📚 Documentation

Chaque fichier de commande contient :
- Description détaillée
- Syntaxe et arguments
- Exemples d'utilisation
- Conseils et bonnes pratiques
- Gestion des erreurs
