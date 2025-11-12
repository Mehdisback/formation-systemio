# 💬 Configuration Giscus (Commentaires)

Ce guide explique comment activer les commentaires GitHub Discussions via Giscus sur votre documentation.

## 🎯 Qu'est-ce que Giscus ?

Giscus est un système de commentaires basé sur GitHub Discussions qui permet aux visiteurs de laisser des commentaires directement sur vos pages de documentation.

## ✅ Prérequis

- [ ] Le repository doit être **public**
- [ ] GitHub Discussions doit être activé
- [ ] L'application Giscus doit être installée

## 📝 Étapes de configuration

### 1. Activer GitHub Discussions

1. Allez sur votre repository GitHub : `https://github.com/Mehdisback/formation-systemio`
2. Cliquez sur **Settings** (Paramètres)
3. Descendez jusqu'à la section **Features**
4. Cochez la case **Discussions**
5. Cliquez sur **Set up discussions**

### 2. Installer l'application Giscus

1. Visitez [https://giscus.app](https://giscus.app)
2. Faites défiler jusqu'à la section **Configuration**
3. Renseignez :
   - **Repository** : `Mehdisback/formation-systemio`
   - **Page ↔️ Discussions Mapping** : `pathname`
   - **Discussion Category** : Choisissez `General` (ou créez une catégorie dédiée)
4. L'outil génèrera automatiquement :
   - Un `data-repo-id`
   - Un `data-category-id`

### 3. Copier les identifiants

Copiez les valeurs fournies par Giscus :

```yaml
# Exemple de valeurs (les vôtres seront différentes)
repo_id: "R_kgDOK1234567"
category_id: "DIC_kwDOK1234567890"
```

### 4. Mettre à jour mkdocs.yml

Ouvrez `mkdocs.yml` et remplacez dans la section `extra.giscus` :

```yaml
giscus:
  repo_id: "REMPLACER_PAR_VOTRE_REPO_ID"
  category_id: "REMPLACER_PAR_VOTRE_CATEGORY_ID"
```

Par vos vraies valeurs :

```yaml
giscus:
  repo_id: "R_kgDOK1234567"
  category_id: "DIC_kwDOK1234567890"
```

### 5. Activer les commentaires sur une page

Pour activer les commentaires sur une page spécifique, ajoutez en **début de fichier** markdown :

```markdown
---
comments: true
---

# Titre de votre page

Votre contenu...
```

## 🎨 Personnalisation

### Choisir les pages avec commentaires

Par défaut, les commentaires sont désactivés. Activez-les uniquement sur :

- ✅ Les guides de formation (pour questions techniques)
- ✅ La FAQ (pour discussions communautaires)
- ❌ La page d'accueil (généralement non pertinent)
- ❌ Le glossaire (pas de discussion nécessaire)

### Exemple d'activation sur un guide

**Fichier : `docs/01-GUIDE-DEMARRAGE-RAPIDE.md`**

```markdown
---
comments: true
---

# 🎯 01 - Guide de démarrage rapide

⏱️ **Durée estimée** : 15 minutes
...
```

## 🧪 Test

1. Lancez le serveur de développement :
   ```bash
   mkdocs serve
   ```

2. Ouvrez une page avec `comments: true`

3. Vérifiez que la section "💬 Commentaires et questions" apparaît en bas de page

4. Testez en laissant un commentaire (nécessite un compte GitHub)

## 🔧 Dépannage

### Les commentaires n'apparaissent pas

- ✅ Vérifiez que GitHub Discussions est bien activé
- ✅ Vérifiez que `comments: true` est présent dans le frontmatter
- ✅ Vérifiez que les IDs sont corrects dans `mkdocs.yml`
- ✅ Videz le cache du navigateur (Ctrl+Shift+R)

### Erreur "Discussion category not found"

- Le `category_id` est incorrect
- Retournez sur https://giscus.app et régénérez les IDs

### Les commentaires apparaissent en anglais

Vérifiez que `data-lang="fr"` est bien défini dans `overrides/partials/comments.html`

## 📚 Ressources

- [Documentation Giscus](https://giscus.app)
- [GitHub Discussions Guide](https://docs.github.com/en/discussions)
- [Material for MkDocs - Comments](https://squidfunk.github.io/mkdocs-material/setup/adding-a-comment-system/)

## ✅ Checklist finale

- [ ] GitHub Discussions activé sur le repository
- [ ] IDs Giscus copiés et collés dans `mkdocs.yml`
- [ ] `comments: true` ajouté sur les pages souhaitées
- [ ] Test local réussi
- [ ] Build et déploiement effectués
- [ ] Commentaires visibles sur GitHub Pages
