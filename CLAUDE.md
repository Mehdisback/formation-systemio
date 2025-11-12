# CLAUDE.md — MkDocs Material Documentation Project

**Stack**: MkDocs Material · Python · GitHub Pages · Markdown

## ✅ Commandes rapides
- `/serve` - Démarrer le serveur de développement avec live reload
- `/build` - Builder la documentation
- `/deploy` - Déployer sur GitHub Pages (nécessite confirmation)
- `/add-guide` - Créer un nouveau guide de formation
- `/validate-docs` - Valider l'intégrité de la documentation
- `/check-links` - Vérifier tous les liens internes et externes

## 🗂️ Structure du projet
| Répertoire/Fichier | Description | Notes importantes |
| --- | --- | --- |
| `docs/` | Contenu de la documentation | Tous les fichiers `.md` |
| `docs/stylesheets/` | Styles CSS personnalisés | Branding et thème |
| `mkdocs.yml` | Configuration MkDocs | Navigation, thème, plugins |
| `.github/workflows/` | CI/CD GitHub Actions | Déploiement automatique |
| `site/` | Build généré (ignoré Git) | Créé par `mkdocs build` |
| `.claude/` | Configuration Claude Code | Commandes et agents |

## 🔧 Stack technique
- **MkDocs Material** : Générateur de documentation statique
- **Python 3.x** : Runtime requis pour MkDocs
- **GitHub Pages** : Hébergement de la documentation
- **GitHub Actions** : CI/CD pour déploiement automatique
- **Markdown** : Format de rédaction
- **Material Extensions** : Admonitions, emojis, tabs, etc.

## 🎨 Configuration MkDocs
### Theme et couleurs
- **Theme** : Material for MkDocs
- **Langue** : Français (`fr`)
- **Palette primaire** : Indigo (#3949AB)
- **Palette accent** : Deep Purple (#7E57C2)

### Plugins actifs
- `search` : Recherche en français
- `minify` : Optimisation HTML/CSS/JS

### Extensions Markdown
- **Admonitions** : Callouts (tip, warning, info, danger, success)
- **CodeHilite** : Coloration syntaxique
- **Tasklists** : Checklists interactives
- **Emoji** : Support emojis Material
- **Tabs** : Onglets de contenu
- **Tables** : Tableaux avancés

## 📝 Conventions de rédaction

### Fichiers
- Nomenclature : `XX-NOM-EN-MAJUSCULES.md`
- Numérotation : 01, 02, 03... (deux chiffres)
- Langue : **Français uniquement**

### Structure d'un guide
```markdown
# 🎯 [Numéro] - [Titre]

⏱️ **Durée estimée** : X minutes
📊 **Niveau** : Débutant/Intermédiaire/Avancé

## 🎯 Objectifs
- [ ] Objectif 1
- [ ] Objectif 2

## 📝 Contenu
### Section 1
Contenu...

!!! tip "Conseil"
    Votre conseil ici

## ✅ Checklist de validation
- [ ] Action 1
- [ ] Action 2

## 🔗 Navigation
- ⬅️ [Guide précédent](XX-GUIDE.md)
- ➡️ [Guide suivant](XX-GUIDE.md)
```

### Admonitions recommandées
- `!!! success` - Félicitations, réussites
- `!!! tip` - Conseils pratiques, astuces
- `!!! warning` - Attention, points importants
- `!!! danger` - Erreurs critiques à éviter
- `!!! info` - Informations complémentaires

### Style de contenu
- ✍️ **Public** : Non-technique (coaching professionnel)
- 🗣️ **Ton** : Professionnel, bienveillant, encourageant
- 📖 **Langage** : Simple, clair, sans jargon technique
- 🎯 **Focus** : Actions concrètes et guidées

## 🚀 Workflows

### Édition de contenu
```bash
/serve                          # Lancer serveur local
# Éditer les fichiers .md dans docs/
# Vérifier les changements dans le navigateur (http://127.0.0.1:8000)
/validate-docs                  # Valider avant commit
git add . && git commit -m "..."
git push                        # Déploiement auto via GitHub Actions
```

### Création d'un nouveau guide
```bash
/add-guide 11 "Titre du guide"  # Créer nouveau guide avec template
# Rédiger le contenu
@content-reviewer analyze       # Review du contenu français
/serve                          # Prévisualiser
/validate-docs                  # Valider
git commit && git push
```

### Audit de qualité complet
```bash
/validate-docs --full           # Validation complète
/check-links                    # Vérifier tous les liens
@content-reviewer review-all    # Review du contenu
@accessibility-checker audit    # Audit accessibilité
```

### Modification de styles
```bash
# Éditer docs/stylesheets/extra.css
@accessibility-checker check-contrast  # Vérifier contrastes
/serve                          # Tester visuellement
/build                          # Build de validation
git commit && git push
```

## 🧪 Validation avant commit

### Checklist manuelle
- [ ] Testé localement avec `/serve`
- [ ] Liens internes fonctionnels
- [ ] Captures d'écran à jour
- [ ] Français correct (grammaire, orthographe)
- [ ] Admonitions bien formatées
- [ ] Navigation précédent/suivant correcte
- [ ] Responsive testé (mobile, tablet, desktop)

### Validation automatique
```bash
/build                    # Build doit passer sans erreur
/validate-docs            # Vérifier syntaxe et structure
/check-links              # Vérifier liens internes
```

## 🎯 Agents spécialisés

### @content-reviewer
**Quand** : Après rédaction ou modification de contenu
**Vérifie** :
- Grammaire et orthographe française
- Clarté pour public non-technique
- Ton adapté au coaching
- Cohérence terminologique
- Utilisation appropriée des admonitions

**Usage** :
```
@content-reviewer analyze docs/05-FORMULAIRES.md
@content-reviewer review-all
```

### @accessibility-checker
**Quand** : Avant déploiement majeur ou après modif CSS
**Vérifie** :
- Conformité WCAG 2.1 AA
- Contraste des couleurs (≥ 4.5:1)
- Navigation au clavier
- Alternatives textuelles images
- Responsive design
- Hiérarchie des titres

**Usage** :
```
@accessibility-checker audit docs/
@accessibility-checker check-contrast
@accessibility-checker full-report
```

## 🔄 Déploiement

### Automatique (recommandé)
1. Push vers `main` branch
2. GitHub Actions déclenché automatiquement
3. Build et déploiement sur GitHub Pages
4. Site mis à jour en ~2 minutes

**Workflow** : `.github/workflows/ci.yml`

### Manuel (dépannage)
```bash
/deploy                   # Nécessite confirmation
# ou
mkdocs gh-deploy --force
```

⚠️ **Note** : Déploiement manuel uniquement pour corrections urgentes. Privilégier le workflow automatique.

## ♻️ Discipline de tokens

### Optimisations activées
- **Auto-compact** : Activé à 95% du contexte
- **Références ciblées** : Fichiers spécifiques dans settings.json
- **Commandes** : Workflows répétitifs automatisés
- **Agents** : Analyses approfondies uniquement

### Bonnes pratiques
- Utiliser `/serve` au lieu de multiples `/build`
- Combiner validations : `/validate-docs && /check-links`
- Agents pour reviews, pas pour simple lecture
- Commandes slash pour workflows standards

## 📊 Métriques de qualité

### Contenu
- ✅ Français grammaticalement correct (100%)
- ✅ Vocabulaire adapté au public (0 jargon non expliqué)
- ✅ Cohérence terminologique
- ✅ Ton professionnel et bienveillant

### Technique
- ✅ Build MkDocs sans erreur ni warning
- ✅ Tous les liens internes valides
- ✅ Liens externes vérifiés hebdomadairement
- ✅ Validation Markdown stricte

### Accessibilité
- ✅ WCAG 2.1 Niveau AA
- ✅ Contraste ≥ 4.5:1 (AA) ou ≥ 7:1 (AAA)
- ✅ Navigation clavier complète
- ✅ Responsive 320px → 2560px
- ✅ Lighthouse Accessibility ≥ 90

## 🔧 Dépendances

### Installation
```bash
pip install mkdocs-material
pip install mkdocs-minify-plugin
```

### Versions recommandées
- Python : ≥ 3.8
- MkDocs : ≥ 1.5.0
- MkDocs Material : ≥ 9.0.0

## 🆘 Dépannage

### Build échoue
1. Vérifier syntaxe Markdown : `/validate-docs`
2. Vérifier mkdocs.yml (indentation YAML)
3. Vérifier dépendances : `pip list | grep mkdocs`

### Liens cassés
1. `/check-links` pour identifier
2. Corriger dans fichiers .md
3. Revalider avec `/check-links`

### Styles CSS ne s'appliquent pas
1. Vérifier chemin dans mkdocs.yml
2. Vider cache navigateur (Ctrl+Shift+R)
3. Rebuild avec `/build --clean`

### Déploiement GitHub Pages échoue
1. Vérifier permissions GitHub Actions
2. Vérifier branche gh-pages existe
3. Vérifier GitHub Pages activé dans settings
4. Consulter logs Actions dans GitHub

## 📚 Documentation externe

- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
- [Guide Markdown](https://squidfunk.github.io/mkdocs-material/reference/)
- [Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)
- [GitHub Pages](https://docs.github.com/en/pages)
- [WCAG 2.1](https://www.w3.org/WAI/WCAG21/quickref/)

## 🎓 Public cible

**Utilisateur final** : Professionnel du coaching (non-technique)
**Cas d'usage** : Formation autonome gestion landing page Systeme.io
**Objectif** : Autonomie complète sur la gestion de contenu

## 📝 Notes importantes

- ⚠️ **Langue** : Français obligatoire (public francophone)
- 🎨 **Branding** : Coaching au Féminin + A-Tek Universe
- 📱 **Mobile-first** : Audience majoritairement mobile
- ♿ **Accessibilité** : Conformité légale RGAA/WCAG
- 🚫 **Pas de code** : Documentation pure, pas d'application

## ✅ Checklist projet en bonne santé

- [ ] `/serve` démarre sans erreur
- [ ] `/build` passe sans warning
- [ ] `/validate-docs` 100% OK
- [ ] `/check-links` 0 lien cassé
- [ ] @content-reviewer score ≥ 95%
- [ ] @accessibility-checker WCAG AA
- [ ] CI/CD GitHub Actions fonctionnel
- [ ] Site GitHub Pages accessible
- [ ] Lighthouse Performance ≥ 90
- [ ] Lighthouse Accessibility ≥ 90
