# Corrections - Plugins MkDocs

## ❌ Erreur commune : mkdocs-sitemap n'existe pas

### 🔍 Le problème
```bash
pip install mkdocs-sitemap
# ERROR: No matching distribution found for mkdocs-sitemap
```

### ✅ La solution

**Le sitemap est INTÉGRÉ dans MkDocs core !**

Aucun package séparé n'est nécessaire. Le fichier `sitemap.xml` est généré automatiquement lors du build si vous avez configuré :

```yaml
# mkdocs.yml
site_url: https://votre-domaine.com
```

**Dans votre cas :**
- ✅ Déjà configuré : `site_url: https://mehdisback.github.io/formation-systemeio/`
- ✅ Sitemap disponible à : `https://mehdisback.github.io/formation-systemio/sitemap.xml`
- ✅ Aucune action requise

---

## ✅ Plugin Git Revision Date (recommandé)

### Installation correcte

```bash
pip install mkdocs-git-revision-date-localized-plugin
```

### Configuration activée dans mkdocs.yml

```yaml
plugins:
  - search:
      # ... config recherche
  - minify:
      # ... config minify
  - git-revision-date-localized:
      enable_creation_date: true
      type: date
      locale: fr
      fallback_to_build_date: true
```

### Ce que ça fait

Affiche automatiquement sur chaque page :
- **Date de dernière modification** (via Git)
- **Date de création** (premier commit)
- **Format** : Format français (ex: "12 novembre 2025")
- **Fallback** : Utilise la date de build si pas de Git

### Exemple de rendu

En bas de chaque page, vous verrez :
```
Dernière mise à jour : 12 novembre 2025
Créé le : 10 novembre 2025
```

---

## 📦 Commandes d'installation complètes

### Installation minimale (déjà installés normalement)
```bash
pip install mkdocs-material
pip install mkdocs-minify-plugin
```

### Installation avec plugin Git dates (recommandé)
```bash
pip install mkdocs-material
pip install mkdocs-minify-plugin
pip install mkdocs-git-revision-date-localized-plugin
```

### Installation complète avec export PDF (optionnel)
```bash
pip install mkdocs-material
pip install mkdocs-minify-plugin
pip install mkdocs-git-revision-date-localized-plugin
pip install mkdocs-with-pdf
```

---

## 🔧 Vérification de l'installation

### Vérifier les plugins installés
```bash
pip list | grep mkdocs
```

Vous devriez voir :
```
mkdocs                              1.5.x
mkdocs-material                     9.x.x
mkdocs-minify-plugin                0.7.x
mkdocs-git-revision-date-localized-plugin  1.2.x
```

### Tester le build
```bash
mkdocs build --strict
```

Si le plugin git-revision-date n'est pas installé, vous verrez :
```
Error: Plugin 'git-revision-date-localized' not found
```

Solution : Installer le plugin ou commenter la section dans mkdocs.yml

---

## 🚀 Build et déploiement

### Développement local
```bash
mkdocs serve
# Ouvrir http://127.0.0.1:8000
```

### Build production
```bash
mkdocs build
# Génère le dossier site/ avec sitemap.xml
```

### Déploiement GitHub Pages
```bash
mkdocs gh-deploy
# Ou push vers main (CI/CD automatique)
```

---

## 📊 Plugins disponibles (récapitulatif)

| Plugin | Package | Statut | Notes |
|--------|---------|--------|-------|
| **Sitemap** | *(intégré)* | ✅ Actif | Généré automatiquement |
| **Search** | *(intégré)* | ✅ Actif | Recherche française |
| **Minify** | `mkdocs-minify-plugin` | ✅ Actif | Compression HTML/CSS/JS |
| **Git Dates** | `mkdocs-git-revision-date-localized-plugin` | ✅ **Maintenant actif** | Dates de modification |
| **PDF Export** | `mkdocs-with-pdf` | ⏳ Optionnel | Pour export PDF |
| **Blog** | *(intégré Material 9.2+)* | ⏳ Non configuré | Fonctionnalité blog |

---

## ⚠️ Erreurs courantes et solutions

### Erreur : "Plugin not found"
```
Error: Plugin 'git-revision-date-localized' not found
```

**Solution :**
```bash
pip install mkdocs-git-revision-date-localized-plugin
```

### Erreur : "No module named 'git'"
```
ModuleNotFoundError: No module named 'git'
```

**Solution :**
```bash
pip install GitPython
```

### Erreur : Sitemap vide
**Cause :** `site_url` manquant ou mal configuré

**Solution :** Vérifier dans mkdocs.yml :
```yaml
site_url: https://votre-domaine.com  # OBLIGATOIRE pour sitemap
```

### Warning : "Repository not found"
**Cause :** Le plugin git-revision-date cherche un dépôt Git

**Solution :**
- Soit : Initialiser Git (`git init`)
- Soit : Désactiver le plugin
- Soit : Utiliser `fallback_to_build_date: true` (déjà configuré)

---

## 📚 Documentation officielle

- **MkDocs** : https://www.mkdocs.org/
- **Material for MkDocs** : https://squidfunk.github.io/mkdocs-material/
- **Git Revision Date Plugin** : https://github.com/timvink/mkdocs-git-revision-date-localized-plugin
- **Minify Plugin** : https://github.com/byrnereese/mkdocs-minify-plugin

---

## ✅ Checklist de validation

- [ ] `site_url` configuré dans mkdocs.yml
- [ ] Plugins nécessaires installés via pip
- [ ] `mkdocs build` passe sans erreur
- [ ] `site/sitemap.xml` généré
- [ ] Dates de modification visibles sur les pages
- [ ] Recherche française fonctionnelle
- [ ] CSS/JS minifiés dans le build

---

**Date de ce document :** 2025-11-12
**Version MkDocs testée :** ≥ 1.5.0
**Version Material testée :** ≥ 9.0.0
