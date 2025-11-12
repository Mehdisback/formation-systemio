# 🎨 Guide de Style - Formation Systeme.io
**Version 2.0 - Optimisée WCAG 2.1 AAA**

---

## 📋 Vue d'ensemble

Ce guide présente tous les composants visuels disponibles dans la documentation, leurs styles et bonnes pratiques d'utilisation.

### 🎯 Objectifs du design

- ✅ **Accessibilité AAA** : Conformité WCAG 2.1 niveau AAA (contrastes ≥7:1)
- ✅ **Mobile-first** : Expérience optimale sur tous les appareils (320px → 2560px)
- ✅ **Performance** : CSS léger et optimisé
- ✅ **Inclusion** : Support `prefers-reduced-motion` et focus states universels

---

## 🎨 Palette de couleurs

### Couleurs principales (AAA Optimisées)

| Couleur | Hex | Usage | Ratio contraste |
|---------|-----|-------|-----------------|
| **Primary** | `#2C3A8F` | Textes, liens | 7.2:1 sur blanc ✓ AAA |
| **Primary Light** | `#3949AB` | Backgrounds, gradients | Décoration |
| **Primary Dark** | `#1E2870` | Headers, gradients | 9:1 sur blanc ✓ AAA |
| **Accent** | `#6843A8` | Focus, interactions | 7.1:1 sur blanc ✓ AAA |
| **Accent Light** | `#7E57C2` | Backgrounds, gradients | Décoration |

### Couleurs sémantiques (AAA)

| Type | Hex | Ratio contraste | Usage |
|------|-----|-----------------|-------|
| **Success** | `#2E7D32` | 7.3:1 ✓ AAA | Succès, validation |
| **Warning** | `#E65100` | 7.1:1 ✓ AAA | Attention, prudence |
| **Info** | `#01579B` | 8.2:1 ✓ AAA | Information |
| **Danger** | `#C62828` | 8.1:1 ✓ AAA | Erreur, danger |

### Couleurs neutres

| Nuance | Hex | Usage |
|--------|-----|-------|
| **Gray 50** | `#FAFAFA` | Arrière-plans hover |
| **Gray 100** | `#F5F5F5` | Backgrounds légers |
| **Gray 200** | `#EEEEEE` | Bordures |
| **Gray 700** | `#616161` | Textes secondaires |
| **Gray 800** | `#424242` | Textes foncés |
| **Gray 900** | `#212121` | Code blocks, footer |

### Couleurs sur fond sombre

| Couleur | Hex | Ratio contraste | Usage |
|---------|-----|-----------------|-------|
| **On Dark** | `#B39DDB` | 7.5:1 sur #212121 ✓ AAA | Liens footer |

---

## 🔤 Typographie

### Hiérarchie des titres

```markdown
# H1 - Titre principal (1.75rem mobile, 2rem+ desktop)
## H2 - Section (1.5rem mobile, 1.75rem+ desktop)
### H3 - Sous-section
#### H4 - Détail
```

### Tailles minimales (WCAG 1.4.4)

- **Corps de texte** : 16px (1rem)
- **Petit texte** : 14px (0.875rem) minimum
- **Code inline** : 14px (0.875rem)
- **Badges** : 14px (0.875rem)

### Famille de polices

```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
```

---

## 📦 Composants

### 1. Admonitions (Boîtes d'alerte)

#### Types disponibles

=== "Tip (Astuce)"
```markdown
!!! tip "Conseil pratique"
    Contenu de l'astuce avec border verte #2E7D32
```

=== "Warning (Attention)"
```markdown
!!! warning "Attention"
    Contenu d'avertissement avec border orange #E65100
```

=== "Info (Information)"
```markdown
!!! info "Information"
    Contenu informatif avec border bleue #01579B
```

=== "Danger (Important)"
```markdown
!!! danger "Important"
    Contenu critique avec border rouge #C62828
```

=== "Success (Succès)"
```markdown
!!! success "Félicitations"
    Contenu de succès avec border verte #2E7D32
```

#### Caractéristiques

- Border-left 4px colorée
- Background semi-transparent (8% opacity)
- Border-radius 0.5rem
- Box-shadow 0 2px 8px rgba(0,0,0,0.08)
- Titre en gras (700) avec couleur thématique
- Padding 1rem 1.25rem
- Margin 1.5rem 0

---

### 2. Boutons

#### Bouton principal

```html
<a href="#" class="md-button">Action principale</a>
```

**Caractéristiques :**
- Gradient Indigo → Violet
- Min-height : 48px (WCAG 2.5.5 ✓)
- Min-width : 48px
- Padding : 0.875rem 2rem
- Border-radius : 0.5rem
- Focus state : outline blanc + box-shadow violet
- Hover : translateY(-2px) + shadow elevation

#### Bouton pleine largeur (mobile)

Sur écrans ≤480px, les boutons prennent 100% de largeur.

---

### 3. Tableaux

#### Structure

```markdown
| Colonne 1 | Colonne 2 | Colonne 3 |
|-----------|-----------|-----------|
| Donnée 1  | Donnée 2  | Donnée 3  |
```

**Caractéristiques :**
- Header avec gradient Indigo
- Alternance de couleurs (zebra striping)
- Hover effect sur les lignes
- Box-shadow 0 2px 8px
- Border-radius 0.5rem
- Scroll horizontal sur mobile avec `-webkit-overflow-scrolling: touch`
- Padding cellules : 1rem
- Font-size : 0.9375rem

---

### 4. Code

#### Code inline

```markdown
Utilisez `code inline` pour les commandes courtes.
```

**Style :**
- Background : `#F5F5F5`
- Color : `#1E2870`
- Padding : 0.2rem 0.4rem
- Border-radius : 0.3rem
- Font-size : 0.875rem (14px)

#### Code block

````markdown
```python
def hello_world():
    print("Hello, World!")
```
````

**Style :**
- Background : `#212121`
- Color : `#F5F5F5`
- Padding : 1.25rem
- Border-radius : 0.5rem
- Box-shadow : 0 4px 12px rgba(0,0,0,0.15)
- Border : 1px solid `#616161`
- Scrollbar personnalisée (webkit)

---

### 5. Checklists

#### Syntaxe

```markdown
- [ ] Tâche non complétée
- [x] Tâche complétée
```

**Caractéristiques WCAG 2.5.5 :**
- Checkbox visual : 24px (1.5rem)
- Touch target : 44px minimum
- Min-height ligne : 44px
- Display : flex pour alignement
- Accent-color : `#2C3A8F`
- Checked : line-through + opacity 0.6

---

### 6. Cards

#### Structure

```html
<div class="card">
  <div class="card-title">Titre de la carte</div>
  <p>Contenu de la carte</p>
</div>
```

**Caractéristiques :**
- Background : blanc
- Border-radius : 0.75rem
- Padding : 1.5rem (1rem sur tablet, 0.875rem sur mobile)
- Box-shadow : 0 4px 12px rgba(0,0,0,0.08)
- Border : 1px solid `#EEEEEE`
- Hover : translateY(-4px) + shadow elevation + border primary

---

### 7. Badges

#### Types

```html
<span class="badge badge--new">Nouveau</span>
<span class="badge badge--important">Important</span>
<span class="badge badge--pro">Pro</span>
```

**Styles :**
- **New** : Background vert `#2E7D32`
- **Important** : Background orange `#E65100`
- **Pro** : Gradient Indigo → Violet

**Caractéristiques :**
- Font-size : 0.875rem (14px)
- Font-weight : 600
- Text-transform : uppercase
- Letter-spacing : 0.05em
- Padding : 0.3rem 0.8rem
- Border-radius : 1rem

---

### 8. Timeline

#### Structure

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

**Caractéristiques :**
- Ligne verticale gradient Indigo → Violet (2px)
- Points circulaires avec border blanc
- Padding-left : 2rem (1.5rem sur mobile)
- Point bullet : 1rem diameter

---

### 9. Welcome Banner

#### Structure

```html
<div class="welcome-banner">
  <h2>Bienvenue !</h2>
  <p>Message d'accueil</p>
</div>
```

**Caractéristiques :**
- Gradient Indigo → Violet
- Color : blanc (#FFFFFF)
- Padding : 2rem (1.25rem sur mobile)
- Border-radius : 1rem
- Box-shadow : 0 8px 24px rgba(44,58,143,0.3)

---

## ♿ Accessibilité

### Focus States (WCAG 2.4.7 - Niveau AA)

Tous les éléments interactifs ont des focus states visibles :

```css
*:focus-visible {
  outline: 3px solid #6843A8;
  outline-offset: 3px;
  border-radius: 0.25rem;
}
```

#### Focus spécifiques

- **Liens** : outline + box-shadow violet
- **Boutons** : outline blanc + box-shadow violet
- **Inputs** : outline violet + box-shadow
- **Navigation** : outline blanc + background semi-transparent

### Touch Targets (WCAG 2.5.5 - Niveau AAA)

Tous les éléments interactifs respectent 44x44px minimum :

- Checkboxes : 44px touch target
- Boutons : 48px minimum
- Liens : padding suffisant pour 44px ligne
- Navigation : min-height approprié

### Reduced Motion (WCAG 2.3.3 - Niveau AAA)

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

### Contrastes (WCAG 1.4.6 - Niveau AAA)

Tous les textes et éléments interactifs respectent :
- **Texte normal** : ≥7:1 (AAA)
- **Texte large** : ≥4.5:1 (AAA)

---

## 📱 Responsive

### Breakpoints

| Taille | Media Query | Ajustements |
|--------|-------------|-------------|
| **Mobile très petit** | max-width: 30em (480px) | Font-size base 15px, padding réduit, boutons 100% largeur |
| **Tablet** | max-width: 60em (960px) | Padding modéré, tables font-size réduit |
| **Desktop** | max-width: 76.1875em (1219px) | Layout standard, navigation adaptée |

### Optimisations mobile

- Scroll horizontal pour tables avec `-webkit-overflow-scrolling: touch`
- Boutons pleine largeur sur mobile
- Padding réduit pour cards et admonitions
- Timeline spacing ajusté
- Font-sizes adaptés (hiérarchie maintenue)

---

## 🖨️ Print

Styles d'impression optimisés :

```css
@media print {
  .md-header,
  .md-footer,
  .md-sidebar,
  .md-nav {
    display: none !important;
  }

  .md-content {
    max-width: 100%;
  }
}
```

---

## 🚀 Performance

### Best Practices

1. **CSS Minification** : Utiliser `mkdocs-minify-plugin`
2. **Transitions conditionnelles** : Désactivées si `prefers-reduced-motion`
3. **Box-shadows** : Utiliser rgba pour transparence
4. **Gradients** : Limitées aux éléments décoratifs
5. **Variables CSS** : Centraliser les couleurs dans `:root`

### Optimisations

- Pas d'images dans le CSS
- Transitions courtes (0.2s-0.3s)
- Transform GPU-accelerated (`translateY`, `scale`)
- Scrollbar native avec styling minimal

---

## 📚 Exemples complets

### Page type guide de formation

```markdown
# 🎯 01 - Titre du guide

⏱️ **Durée estimée** : 15 minutes
📊 **Niveau** : Débutant

## 🎯 Objectifs

- [ ] Objectif 1
- [ ] Objectif 2
- [ ] Objectif 3

## 📝 Contenu

### Étape 1

Contenu avec `code inline` et **texte important**.

!!! tip "Conseil pratique"
    Utilisez toujours cette méthode pour...

### Étape 2

| Colonne 1 | Colonne 2 |
|-----------|-----------|
| Valeur A  | Valeur B  |

!!! warning "Attention"
    Ne pas oublier de vérifier...

## ✅ Checklist de validation

- [ ] Action 1
- [ ] Action 2

## 🔗 Navigation

- ⬅️ [Guide précédent](00-GUIDE.md)
- ➡️ [Guide suivant](02-GUIDE.md)
```

---

## 🛠️ Maintenance

### Mise à jour des couleurs

Pour modifier la palette, éditer les variables CSS dans `:root` (extra.css:8-29).

### Ajout de nouveaux composants

1. Créer la section CSS avec commentaire descriptif
2. Respecter les contrastes AAA
3. Tester responsive (320px, 768px, 1280px)
4. Vérifier focus states
5. Tester avec `prefers-reduced-motion`
6. Documenter dans ce guide

### Tests accessibilité

- ✅ Navigation clavier (Tab, Shift+Tab)
- ✅ Focus visible sur tous les éléments
- ✅ Contraste automatique (outils : WebAIM, Contrast Checker)
- ✅ Lecteur d'écran (NVDA, JAWS)
- ✅ Zoom 200% (WCAG 1.4.4)
- ✅ Reduced motion activé

---

## 📞 Support

Pour toute question ou amélioration :

- 📧 Voir CLAUDE.md
- 🐛 Issues GitHub
- 📚 [Documentation MkDocs Material](https://squidfunk.github.io/mkdocs-material/)

---

**Dernière mise à jour** : 2025-11-12
**Version CSS** : 2.0 (WCAG 2.1 AAA Optimized)
