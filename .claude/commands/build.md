# `/build`

Build la documentation MkDocs en site statique HTML.

```
/build [--clean]
```

## Ce que fait cette commande
1. Génère le site statique dans le dossier `site/`
2. Compile tous les fichiers Markdown en HTML
3. Applique les styles et extensions configurées
4. Minifie les assets (HTML, CSS, JS)
5. Vérifie l'intégrité de la navigation

## Arguments
- `--clean` (optionnel) : Nettoie le dossier `site/` avant le build

## Exemples
```
/build                   # Build standard
/build --clean           # Build avec nettoyage préalable
```

## Ce qui est vérifié
- ✅ Syntaxe Markdown valide
- ✅ Navigation cohérente avec mkdocs.yml
- ✅ Extensions Markdown fonctionnelles
- ✅ Admonitions correctement formatées
- ✅ Liens internes valides

## Conseils
- Lancez un build avant chaque commit
- Vérifiez les warnings dans la console
- Le dossier `site/` est ignoré par Git
- Utilisez `/serve` pour prévisualiser avant de build

## En cas d'erreur
- **Erreur de navigation** : Vérifier `mkdocs.yml`
- **Markdown invalide** : Vérifier la syntaxe dans le fichier mentionné
- **Extension manquante** : Installer avec `pip install <extension>`
