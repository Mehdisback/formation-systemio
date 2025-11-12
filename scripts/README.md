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

## 🔮 Futurs scripts prévus

### `check_images.py` (TODO)
Vérifier que toutes les images référencées existent et ont un alt text.

### `optimize_images.py` (TODO)
Compresser automatiquement les images PNG/JPG avec TinyPNG API.

### `validate_frontmatter.py` (TODO)
Vérifier que tous les guides ont une meta description dans le frontmatter YAML.

### `generate_stats.py` (TODO)
Générer statistiques projet :
- Nombre total de mots
- Nombre de guides
- Durée totale formation
- Score SEO estimé

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
