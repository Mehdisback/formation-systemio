# Export PDF - Générer version PDF de la documentation

Exporte l'intégralité de la documentation en un fichier PDF unique pour lecture hors ligne.

## Utilisation

```bash
/export-pdf
```

## Ce que fait cette commande

1. Vérifie si le plugin mkdocs-pdf-export-plugin est installé
2. L'installe si nécessaire via pip
3. Configure temporairement mkdocs.yml pour l'export PDF
4. Build la documentation avec génération du PDF
5. Génère un PDF unique avec couverture, table des matières et tous les guides
6. Sauvegarde dans `site/pdf/formation-systemio.pdf`

## Instructions d'implémentation

### Étape 1 : Vérifier et installer le plugin

```bash
# Vérifier si déjà installé
pip list | grep mkdocs-pdf-export-plugin

# Si pas installé
pip install mkdocs-pdf-export-plugin
```

### Étape 2 : Ajouter configuration dans mkdocs.yml

Ajouter dans la section `plugins:` :

```yaml
plugins:
  - search:
      lang: fr
  - minify:
      minify_html: true
      minify_js: true
      minify_css: true
  - pdf-export:
      combined: true
      combined_output_path: pdf/formation-systemio.pdf
      media_type: print
      enabled_if_env: ENABLE_PDF_EXPORT
      author: 'A-Tek Universe'
      copyright: '2025 Coaching au Féminin - L\'Essentiel en Soi'
```

### Étape 3 : Builder avec PDF

```bash
# Activer l'export PDF via variable d'environnement
ENABLE_PDF_EXPORT=1 mkdocs build

# Vérifier le résultat
ls -lh site/pdf/formation-systemio.pdf
```

### Étape 4 : Alternative - WeasyPrint pour PDF de qualité supérieure

Pour un meilleur contrôle du PDF, utiliser WeasyPrint :

```bash
# Installer WeasyPrint
pip install mkdocs-with-pdf weasyprint

# Utiliser dans mkdocs.yml
plugins:
  - with-pdf:
      author: 'A-Tek Universe'
      copyright: '2025 Coaching au Féminin'
      cover_title: 'Formation Systeme.io'
      cover_subtitle: 'L\'Essentiel en Soi - Guide Complet'
      cover_logo: 'assets/logo.png'
      output_path: 'pdf/formation-systemio.pdf'
      enabled_if_env: ENABLE_PDF_EXPORT

      # Style personnalisé
      custom_template_path: templates

      # Options de rendu
      render_js: true
      headless_chrome_path: '/usr/bin/google-chrome'

      # Table des matières
      toc_title: 'Table des matières'
      toc_level: 3

      # Ordre des pages
      ordered_chapter_level: 2
```

## Bénéfices

✅ **Accès hors ligne** : Lecture sans connexion internet
✅ **Ressource professionnelle** : PDF téléchargeable à partager
✅ **Impression optimisée** : Format A4 avec numéros de page
✅ **Archive complète** : Capture l'état de la documentation à un instant T
✅ **Portable** : Compatible tous appareils (mobile, tablette, PC)

## Fichiers créés

```
site/
└── pdf/
    └── formation-systemio.pdf  (document unique, ~5-10 MB)
```

## Notes importantes

⚠️ **Build time** : Générer un PDF peut prendre 30-60 secondes selon la taille de la doc
⚠️ **Dépendances système** : WeasyPrint nécessite des libs système (cairo, pango)
⚠️ **Images** : Toutes les images doivent exister pour un PDF complet
⚠️ **Liens externes** : Les URLs seront affichées en texte dans le PDF

## Dépannage

### Erreur : "ModuleNotFoundError: No module named 'pdf'"

```bash
pip install --upgrade mkdocs-pdf-export-plugin
```

### Erreur : "cairo" ou "pango" not found (pour WeasyPrint)

**Ubuntu/Debian** :
```bash
sudo apt-get install python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0
```

**macOS** :
```bash
brew install cairo pango gdk-pixbuf libffi
```

### PDF vide ou incomplet

1. Vérifier que toutes les images existent
2. Vérifier la configuration dans mkdocs.yml
3. Builder en mode verbose : `mkdocs build -v`

### Performance lente

Pour PDF rapide sans rendu JS :
```yaml
plugins:
  - pdf-export:
      render_js: false
      theme_handler_path: null
```

## Exemple d'utilisation complète

```bash
# Installation complète
pip install mkdocs-with-pdf weasyprint

# Activer dans mkdocs.yml (voir étape 4)

# Build avec PDF
ENABLE_PDF_EXPORT=1 mkdocs build

# Vérifier le résultat
echo "✅ PDF généré : site/pdf/formation-systemio.pdf"
ls -lh site/pdf/formation-systemio.pdf

# Ouvrir le PDF (Linux)
xdg-open site/pdf/formation-systemio.pdf

# Ouvrir le PDF (macOS)
open site/pdf/formation-systemio.pdf
```

## Automatisation CI/CD

Pour générer le PDF automatiquement lors du déploiement, ajouter dans `.github/workflows/ci.yml` :

```yaml
- name: Install PDF dependencies
  run: |
    pip install mkdocs-with-pdf weasyprint
    sudo apt-get update
    sudo apt-get install -y libpango-1.0-0 libpangoft2-1.0-0

- name: Build with PDF
  run: ENABLE_PDF_EXPORT=1 mkdocs build

- name: Upload PDF artifact
  uses: actions/upload-artifact@v3
  with:
    name: documentation-pdf
    path: site/pdf/formation-systemio.pdf
```

---

**Prêt à générer votre PDF ?** 📄✨
