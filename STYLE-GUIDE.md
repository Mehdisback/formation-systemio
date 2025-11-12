# 🎨 Guide de Style - Documentation Formation Systeme.io

Ce document recense **tous les éléments de style disponibles** dans la documentation pour garantir une cohérence visuelle et éditoriale.

---

## 📊 Palette de couleurs

### Couleurs principales (CSS Variables)

| Variable CSS | Valeur | Usage |
|--------------|--------|-------|
| `--atek-primary` | #3949AB (Indigo) | Couleur principale, liens, titres actifs |
| `--atek-primary-dark` | #283593 (Indigo foncé) | Dégradés, en-têtes |
| `--atek-accent` | #7E57C2 (Violet) | Accent, hover, mise en avant |
| `--atek-success` | #4CAF50 (Vert) | Validations, succès |
| `--atek-warning` | #FF9800 (Orange) | Avertissements, points d'attention |
| `--atek-info` | #2196F3 (Bleu) | Informations complémentaires |

### Couleurs neutres

| Variable | Valeur | Usage |
|----------|--------|-------|
| `--atek-gray-50` | #FAFAFA | Fonds très clairs |
| `--atek-gray-100` | #F5F5F5 | Fonds de code inline |
| `--atek-gray-200` | #EEEEEE | Bordures, séparateurs |
| `--atek-gray-800` | #424242 | Texte secondaire |
| `--atek-gray-900` | #212121 | Texte principal, footer |

---

## 🎯 Admonitions (Boîtes d'alerte)

### Types disponibles

#### ✅ Success - Félicitations, réussites
```markdown
!!! success "Titre de la réussite"
    Contenu de félicitations ou validation d'étape.
```

**Usage :** Début de guide (bienvenue), fin de section (bravo), validation d'objectifs.

**Style CSS :** Bordure verte (#4CAF50), fond léger vert

---

#### 💡 Tip - Conseils pratiques
```markdown
!!! tip "Conseil pratique"
    Astuce ou bonne pratique pour faciliter le travail.
```

**Usage :** Astuces, raccourcis, optimisations, bonnes pratiques.

**Style CSS :** Bordure verte (#4CAF50), fond léger vert

---

#### ⚠️ Warning - Attention, points importants
```markdown
!!! warning "Attention"
    Point important à ne pas négliger.
```

**Usage :** Mises en garde, précautions, points critiques non bloquants.

**Style CSS :** Bordure orange (#FF9800), fond léger orange

---

#### 🚨 Danger - Erreurs critiques à éviter
```markdown
!!! danger "Erreur critique"
    Action dangereuse ou erreur grave à éviter absolument.
```

**Usage :** Sécurité, erreurs destructrices, actions irréversibles.

**Style CSS :** Bordure rouge (#F44336), fond léger rouge

---

#### ℹ️ Info - Informations complémentaires
```markdown
!!! info "Information"
    Information complémentaire ou contexte supplémentaire.
```

**Usage :** Contexte, définitions, explications techniques simplifiées.

**Style CSS :** Bordure bleue (#2196F3), fond léger bleu

---

## 📝 Extensions Markdown activées

### Emojis
**Extension :** `pymdownx.emoji`

```markdown
:material-check: :material-close: :material-star:
```

**Liste complète :** [Material Icons](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/)

**Recommandation :** Utiliser les emojis Unicode natifs dans les titres pour compatibilité mobile.

---

### Checklists interactives
**Extension :** `pymdownx.tasklist`

```markdown
- [ ] Tâche non cochée
- [x] Tâche cochée
```

**Style CSS personnalisé :**
- Checkbox accent couleur primaire (#3949AB)
- Taille : 1.25rem
- Texte barré quand coché

**Usage recommandé :**
- Objectifs en début de guide
- Checklist de validation en fin de guide

---

### Onglets de contenu
**Extension :** `pymdownx.tabbed`

```markdown
=== "Onglet 1"
    Contenu du premier onglet

=== "Onglet 2"
    Contenu du second onglet
```

**Usage :** Alternatives (débutant/avancé), différents parcours utilisateur.

---

### Tableaux
**Extension :** `tables`

```markdown
| Colonne 1 | Colonne 2 | Colonne 3 |
|-----------|-----------|-----------|
| Valeur A  | Valeur B  | Valeur C  |
```

**Style CSS personnalisé :**
- En-tête : Dégradé indigo (#3949AB → #283593), texte blanc
- Lignes : Bordure grise, hover fond clair (#FAFAFA)
- Box-shadow : 0 2px 8px rgba(0,0,0,0.08)
- Border-radius : 0.5rem

---

### Blocs de code avec coloration syntaxique
**Extension :** `pymdownx.highlight`, `pymdownx.superfences`

````markdown
```python
def exemple():
    return "Hello World"
```
````

**Fonctionnalités :**
- Numérotation des lignes
- Bouton copier automatique
- Support multi-langages

---

### Attributs HTML
**Extension :** `attr_list`

```markdown
[Bouton CTA](https://example.com){ .md-button .md-button--primary }
```

**Classes disponibles :**
- `.md-button` : Bouton standard
- `.md-button--primary` : Bouton principal avec dégradé

**Style CSS :**
- Dégradé indigo → violet
- Box-shadow avec effet hover
- Transition transform + shadow

---

### Raccourcis clavier
**Extension :** `pymdownx.keys`

```markdown
++ctrl+s++
++cmd+d++
```

**Rendu :** Touches de clavier stylisées

---

### Formatage avancé
**Extensions :** `pymdownx.mark`, `pymdownx.caret`, `pymdownx.tilde`

```markdown
==Texte surligné==
^^Texte en exposant^^
~~Texte barré~~
```

---

## 🎨 Classes CSS personnalisées disponibles

### Badges
```html
<span class="badge badge--new">Nouveau</span>
<span class="badge badge--important">Important</span>
<span class="badge badge--pro">Pro</span>
```

**Styles :**
- `badge--new` : Vert (#4CAF50), texte blanc
- `badge--important` : Orange (#FF9800), texte blanc
- `badge--pro` : Dégradé indigo → violet, texte blanc

---

### Cards (Cartes)
```html
<div class="card">
  <div class="card-title">Titre de la carte</div>
  <p>Contenu de la carte</p>
</div>
```

**Style :**
- Fond blanc, bordure grise
- Border-radius : 0.75rem
- Box-shadow : 0 4px 12px rgba(0,0,0,0.08)
- Hover : Translation Y + shadow plus forte

---

### Bannière de bienvenue
```html
<div class="welcome-banner">
  <h2>Bienvenue dans la formation</h2>
  <p>Description...</p>
</div>
```

**Style :**
- Dégradé indigo → violet
- Texte blanc, padding généreux
- Box-shadow prononcée

---

### Timeline (Processus étape par étape)
```html
<div class="timeline">
  <div class="timeline-item">
    <h3>Étape 1</h3>
    <p>Description de l'étape</p>
  </div>
  <div class="timeline-item">
    <h3>Étape 2</h3>
    <p>Description de l'étape</p>
  </div>
</div>
```

**Style :**
- Ligne verticale avec dégradé indigo → violet
- Points de progression circulaires
- Espacement vertical optimal

---

### Signature A-Tek
```html
<a href="https://a-tek-universe.fr" class="atek-signature">A-Tek Universe</a>
```

**Style :**
- Dégradé indigo → violet, texte blanc
- Icône éclair (⚡) avant le texte
- Box-shadow + effet hover

---

## 📐 Structure recommandée d'un guide

### Entête obligatoire
```markdown
# 🎯 [Numéro] - [Titre avec emoji pertinent]

⏱️ **Durée estimée** : X minutes
📊 **Niveau** : Débutant/Intermédiaire/Avancé

## 🎯 Objectifs

À la fin de ce guide, vous saurez :

- [ ] Objectif 1 (action concrète)
- [ ] Objectif 2 (action concrète)
- [ ] Objectif 3 (action concrète)
```

---

### Corps du guide
```markdown
---

## 📝 [Section principale]

### Sous-section 1

Contenu clair, paragraphes courts (max 3-4 lignes).

!!! tip "Conseil"
    Astuce pratique pour faciliter la tâche.

### Sous-section 2

!!! warning "Attention"
    Point important à ne pas négliger.

---

## 📝 [Section principale 2]

...
```

---

### Checklist de validation
```markdown
---

## ✅ Checklist de validation

Avant de passer au guide suivant, vérifiez que vous avez bien :

- [ ] Action 1 complétée
- [ ] Action 2 vérifiée
- [ ] Action 3 testée
- [ ] Toutes les étapes comprises
```

---

### Navigation de fin
```markdown
---

## 🔗 Navigation

- ⬅️ **Précédent** : [Guide XX - Titre](XX-TITRE.md)
- ➡️ **Suivant** : [Guide XX - Titre](XX-TITRE.md)
- 🏠 **Accueil** : [Retour à l'accueil](index.md)
```

---

## 📏 Conventions éditoriales

### Ton et style
- **Public cible :** Professionnel du coaching (non-technique)
- **Ton :** Professionnel, bienveillant, encourageant
- **Langage :** Simple, clair, **sans jargon technique** non expliqué
- **Phrases :** Courtes, actives, directes
- **Paragraphes :** Max 3-4 lignes pour faciliter la lecture

### Utilisation des emojis
- **Titres principaux (h1) :** 1 emoji pertinent
- **Sections (h2) :** 1 emoji si pertinent
- **Sous-sections (h3) :** Facultatif
- **Inline :** Modéré, uniquement pour illustrer

### Nomenclature des fichiers
```
XX-NOM-EN-MAJUSCULES.md
```
- `XX` : Numéro à deux chiffres (01, 02, 03...)
- `NOM` : Titre en majuscules, tirets
- Extension : `.md`

**Exemples :**
- `01-GUIDE-DEMARRAGE-RAPIDE.md`
- `05-FORMULAIRES-DONNEES.md`

---

## 🎯 Utilisation des admonitions par contexte

| Contexte | Admonition recommandée |
|----------|------------------------|
| Bienvenue en début de guide | `!!! success` |
| Conseil pratique | `!!! tip` |
| Point d'attention important | `!!! warning` |
| Sécurité, erreur grave | `!!! danger` |
| Contexte, explication | `!!! info` |
| Fin de guide, félicitations | `!!! success` |

---

## 🔤 Typographie et formatage

### Gras (`**texte**`)
- Termes clés à retenir
- Noms de boutons, menus, sections de l'interface
- Chiffres importants

**Exemples :**
- Cliquez sur **"Enregistrer"**
- Section **Dashboard**
- **60% des visiteurs** sont sur mobile

### Italique (`*texte*`)
- Citations
- Termes étrangers
- Emphase légère

### Code inline (`` `code` ``)
- Noms de fichiers
- URLs
- Commandes
- Raccourcis clavier dans tableaux

**Exemples :**
- `index.md`
- `https://systeme.io`
- `Ctrl + S`

### Listes
- **Non ordonnées :** Points généraux, options, avantages
- **Ordonnées :** Étapes séquentielles, processus
- **Checklists :** Objectifs, validation, actions à réaliser

---

## 📱 Responsive et accessibilité

### Accessibilité WCAG 2.1 AA
- **Contraste :** Minimum 4.5:1 (texte normal), 7:1 idéal
- **Navigation clavier :** Tous les éléments interactifs accessibles au clavier
- **Alternatives textuelles :** Images décoratives avec alt vide, images informatives avec alt descriptif
- **Hiérarchie des titres :** Respect strict (h1 → h2 → h3, pas de saut)

### Mobile-first
- **Test mobile obligatoire** avant publication
- **Tableaux :** Scroll horizontal automatique
- **Images :** Responsive automatique
- **Texte :** Taille minimale 16px

---

## 🔍 SEO et métadonnées

### Titres de page
- Format : `# 🎯 [Numéro] - [Titre descriptif]`
- Max 60 caractères pour SEO
- Mots-clés pertinents

### Structure des titres
```markdown
# Titre principal (h1) - Un seul par page
## Section principale (h2)
### Sous-section (h3)
#### Détail (h4) - Usage modéré
```

### Liens internes
- **Toujours utiliser des chemins relatifs** pour les liens entre guides
- Format : `[Texte du lien](XX-NOM-FICHIER.md)`

**Exemple :**
```markdown
[Guide 02 - Modification du contenu](02-MODIFICATION-CONTENU.md)
```

---

## ✅ Checklist de validation avant publication

### Contenu
- [ ] Français grammaticalement correct
- [ ] Ton adapté au public (bienveillant, professionnel)
- [ ] Pas de jargon non expliqué
- [ ] Emojis utilisés avec modération
- [ ] Checklist d'objectifs en début
- [ ] Checklist de validation en fin
- [ ] Navigation précédent/suivant présente

### Technique
- [ ] Nomenclature fichier respectée (XX-NOM.md)
- [ ] Titres hiérarchisés correctement (h1 → h2 → h3)
- [ ] Liens internes fonctionnels
- [ ] Admonitions bien formatées
- [ ] Tableaux bien structurés
- [ ] Code blocks avec langage spécifié

### Accessibilité
- [ ] Contraste couleurs ≥ 4.5:1
- [ ] Images avec alt text
- [ ] Navigation clavier possible
- [ ] Testé en vue mobile
- [ ] Responsive vérifié

### SEO
- [ ] Titre h1 unique et descriptif
- [ ] Structure hiérarchique respectée
- [ ] Liens internes cohérents
- [ ] Métadonnées pertinentes

---

## 📚 Ressources de référence

- **MkDocs Material :** [https://squidfunk.github.io/mkdocs-material/](https://squidfunk.github.io/mkdocs-material/)
- **Icons Material :** [https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/)
- **Admonitions :** [https://squidfunk.github.io/mkdocs-material/reference/admonitions/](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)
- **WCAG 2.1 :** [https://www.w3.org/WAI/WCAG21/quickref/](https://www.w3.org/WAI/WCAG21/quickref/)

---

**Ce guide de style est la référence absolue pour maintenir la cohérence de la documentation. Respectez-le scrupuleusement pour garantir une expérience utilisateur optimale.** ✨
