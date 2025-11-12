# 🔧 Scripts - Formation Systeme.io

Scripts utilitaires pour la maintenance et la validation de la documentation.

---

## 📜 Liste des scripts

### `check_links.py` - Vérification des liens

Vérifie tous les liens (internes et externes) dans la documentation Markdown.

#### Installation des dépendances

```bash
# Optionnel : pour vérification liens externes
pip install requests
```

#### Usage

```bash
# Vérifier uniquement liens internes (rapide)
python scripts/check_links.py

# Vérifier aussi les liens externes (plus lent, ~2-3 min)
python scripts/check_links.py --external
```

#### Sortie exemple

```
🔍 Vérification des liens dans 12 fichiers...

📄 index.md
  ✓ Ligne 33: 01-GUIDE-DEMARRAGE-RAPIDE.md
  ✓ Ligne 71: 02-MODIFICATION-CONTENU.md
  ⊘ Ligne 165: https://a-tek-universe.fr (externe, non vérifié)

📄 01-GUIDE-DEMARRAGE-RAPIDE.md
  ✓ Ligne 342: 02-MODIFICATION-CONTENU.md
  ✓ Ligne 343: index.md

...

============================================================

📊 RÉSUMÉ

Total de liens vérifiés: 197
✓ Liens valides: 197

🎉 Tous les liens sont valides !
```

#### En cas de liens cassés

```
❌ Liens cassés: 2

🔴 DÉTAILS DES LIENS CASSÉS:

  📄 05-FORMULAIRES-DONNEES.md:42
     🔗 06-SEO.md
     ⚠️  Fichier introuvable: /path/to/docs/06-SEO.md

  📄 08-MAINTENANCE-BONNES-PRATIQUES.md:15
     🔗 https://example.com/broken
     ⚠️  HTTP 404
```

#### Intégration CI/CD

Ajouter dans `.github/workflows/ci.yml` :

```yaml
- name: Check links
  run: |
    python scripts/check_links.py
  continue-on-error: false  # Fail si liens cassés
```

#### Options avancées

Le script peut être étendu pour :
- Vérifier les ancres (#section) dans les fichiers
- Générer un rapport HTML
- Exclure certains domaines externes
- Configurer timeout personnalisé

---

### `optimize_images.py` - Optimisation d'images

Compresse et optimise les images pour le web.

#### Installation des dépendances

```bash
pip install Pillow
```

#### Usage

```bash
# Optimiser toutes les images dans docs/assets
python scripts/optimize_images.py

# Avec conversion WebP
python scripts/optimize_images.py --webp

# Personnaliser la qualité
python scripts/optimize_images.py --quality 85 --max-size 100

# Générer versions responsive
python scripts/optimize_images.py --responsive
```

#### Fonctionnalités

- Compression PNG/JPG avec réduction de taille
- Conversion vers WebP (optionnel)
- Génération de versions responsive (320px, 640px, 1024px, 1920px)
- Rapport d'optimisation avec gains en KB

---

### `validate_frontmatter.py` - Validation des métadonnées

Vérifie le frontmatter YAML des fichiers Markdown.

#### Installation des dépendances

```bash
pip install PyYAML
```

#### Usage

```bash
# Validation normale (warnings pour frontmatter manquant)
python scripts/validate_frontmatter.py

# Mode strict (erreur si pas de frontmatter)
python scripts/validate_frontmatter.py --strict

# Vérifier un répertoire spécifique
python scripts/validate_frontmatter.py --dir docs/
```

#### Validations effectuées

- Syntaxe YAML correcte
- Présence des champs requis (title)
- Champs recommandés (description)
- Longueur de description SEO (50-160 caractères)

---

### `generate_stats.py` - Statistiques de documentation

Génère des statistiques complètes sur la documentation.

#### Usage

```bash
# Afficher les statistiques
python scripts/generate_stats.py

# Exporter en JSON
python scripts/generate_stats.py --export stats.json

# Analyser un répertoire spécifique
python scripts/generate_stats.py --dir docs/
```

#### Statistiques générées

- Nombre total de pages et de mots
- Temps de lecture estimé (à 200 mots/minute)
- Éléments de contenu (code blocks, images, liens, admonitions)
- Couverture des assets (images, screenshots)
- Top 5 des pages les plus longues
- Moyennes par page

---

### `check_spelling.py` - Vérification orthographique

Vérifie l'orthographe française avec dictionnaire personnalisé.

#### Installation des dépendances

```bash
pip install pyspellchecker
```

#### Usage

```bash
# Vérifier toute la documentation
python scripts/check_spelling.py

# Vérifier un fichier spécifique
python scripts/check_spelling.py --file docs/01-GUIDE-DEMARRAGE-RAPIDE.md

# Ajouter un mot au dictionnaire personnalisé
python scripts/check_spelling.py --add-word "Systeme.io"
```

#### Fonctionnalités

- Dictionnaire français intégré
- Dictionnaire personnalisé pour termes techniques
- Suggestions de corrections
- Rapport des erreurs fréquentes
- Exclut automatiquement code, URLs, balises HTML

---

## 💡 Contribuer

Pour ajouter un nouveau script :

1. Créer le fichier dans `scripts/`
2. Ajouter shebang : `#!/usr/bin/env python3`
3. Rendre exécutable : `chmod +x scripts/nom_script.py`
4. Documenter usage dans ce README
5. Tester localement
6. Commit avec message descriptif

---

## 🆘 Dépannage

### Erreur : `No module named 'requests'`

Installer avec :
```bash
pip install requests
```

### Erreur : Permission denied

Rendre le script exécutable :
```bash
chmod +x scripts/check_links.py
```

### Script ne détecte pas les fichiers

Vérifier que vous exécutez depuis la racine du projet :
```bash
cd /path/to/formation-systemio
python scripts/check_links.py
```

---

## 📚 Ressources

- [Python argparse](https://docs.python.org/3/library/argparse.html)
- [Requests library](https://requests.readthedocs.io/)
- [GitHub Actions](https://docs.github.com/en/actions)
