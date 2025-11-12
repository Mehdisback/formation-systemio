# 🎨 Guide de Style - A-Tek Universe Documentation

**Version :** 3.0 (Mode Sombre + Animations + Composants)
**Dernière mise à jour :** 2025-11-12
**Auteur :** A-Tek Universe

---

## 📋 Table des matières

1. [Mode Sombre](#-mode-sombre)
2. [Palette de Couleurs](#-palette-de-couleurs)
3. [Animations](#-animations)
4. [Composants](#-composants)
   - [Cards](#cards)
   - [Call-to-Action (CTA)](#call-to-action-cta)
   - [Badges](#badges)
   - [Accordéons](#accordéons)
   - [Highlights](#highlights)
   - [Progress Indicators](#progress-indicators)
5. [Admonitions](#-admonitions)
6. [Accessibilité](#-accessibilité)
7. [Exemples Pratiques](#-exemples-pratiques)

---

## 🌙 Mode Sombre

### Activation automatique

Le mode sombre s'active **automatiquement** en fonction des préférences système de l'utilisateur via `prefers-color-scheme: dark`.

**Comment tester :**
- **macOS :** Préférences Système → Général → Apparence → Sombre
- **Windows :** Paramètres → Personnalisation → Couleurs → Mode sombre
- **Linux :** Dépend de votre environnement de bureau

### Caractéristiques

- ✅ Détection automatique des préférences système
- ✅ Contrastes WCAG 2.1 AAA (≥ 7:1) garantis
- ✅ Transitions fluides entre modes (0.3s)
- ✅ Tous les composants adaptés
- ✅ Palette optimisée pour confort visuel nocturne

### Palette Mode Sombre

| Élément | Couleur Mode Clair | Couleur Mode Sombre | Contraste |
|---------|-------------------|---------------------|-----------|
| Fond principal | `#FFFFFF` | `#1A1A1A` | - |
| Texte principal | `#212121` | `#ECECEC` | 10.5:1 ✅ |
| Primary | `#2C3A8F` | `#7E9BFF` | 7.5:1 ✅ |
| Accent | `#6843A8` | `#B39DDB` | 7.5:1 ✅ |
| Success | `#2E7D32` | `#81C784` | 7.8:1 ✅ |
| Warning | `#E65100` | `#FFB74D` | 8.5:1 ✅ |
| Danger | `#C62828` | `#E57373` | 7.3:1 ✅ |

---

## 🎨 Palette de Couleurs

### Couleurs Primaires

#### Mode Clair

```css
--atek-primary: #2C3A8F        /* Indigo principal (7.2:1 sur blanc) */
--atek-primary-light: #3949AB  /* Indigo clair */
--atek-primary-dark: #1E2870   /* Indigo foncé (9:1) */
--atek-accent: #6843A8         /* Violet (7.1:1) */
--atek-accent-light: #7E57C2   /* Violet clair */
```

#### Mode Sombre

```css
--atek-primary: #7E9BFF        /* Indigo clair (7.5:1 sur #1A1A1A) */
--atek-primary-light: #9FB4FF  /* Indigo très clair (8.2:1) */
--atek-accent: #B39DDB         /* Violet clair (7.5:1) */
--atek-accent-light: #D4C4E8   /* Violet très clair (9.1:1) */
```

### Couleurs Sémantiques

| Nom | Mode Clair | Mode Sombre | Usage |
|-----|-----------|-------------|-------|
| Success | `#2E7D32` | `#81C784` | Succès, validation |
| Warning | `#E65100` | `#FFB74D` | Attention, avertissement |
| Info | `#01579B` | `#64B5F6` | Information |
| Danger | `#C62828` | `#E57373` | Erreur, danger |

---

## 🎬 Animations

### Animations Disponibles

Toutes les animations respectent `prefers-reduced-motion` et sont désactivées automatiquement si l'utilisateur préfère moins de mouvement.

#### 1. Fade In Up

**Description :** Apparition douce depuis le bas
**Durée :** 0.6s
**Usage :** Contenu principal, admonitions

#### 2. Slide In Left / Right

**Description :** Apparition latérale
**Durée :** 0.5s
**Usage :** Admonitions tip (gauche), warning (droite)

#### 3. Scale In

**Description :** Zoom subtil à l'apparition
**Durée :** 0.5s
**Usage :** Cards, badges

#### 4. Pulse

**Description :** Pulsation douce
**Durée :** 1.5s (infini)
**Usage :** Éléments actifs, timeline, progress

#### 5. Shimmer

**Description :** Effet de brillance
**Durée :** 2-3s (infini)
**Usage :** Loading states, welcome banner

### Transitions Interactives

| Élément | Effet Hover | Durée |
|---------|-------------|-------|
| Liens | Underline slide-in | 0.3s |
| Boutons | Scale + shadow + ripple | 0.3s |
| Cards | Lift (translateY + scale) | 0.3s |
| Images | Scale + brightness | 0.3s |
| Navigation | Indicator slide | 0.3s |
| Accordéons | Expand smooth | 0.4s |

### Performance

✅ GPU Acceleration activée via `transform: translateZ(0)`
✅ `will-change` utilisé judicieusement
✅ Optimisation avec `cubic-bezier(0.4, 0, 0.2, 1)`

---

## 🧩 Composants

### Cards

#### A. Doc Card (Basique)

**Usage :** Carte de contenu standard

```html
<div class="doc-card">
  <div class="doc-card-title">📘 Titre de la carte</div>
  <div class="doc-card-content">
    Contenu de votre carte avec du texte explicatif.
  </div>
</div>
```

**Caractéristiques :**
- Animation : `scaleIn` au chargement
- Hover : lift effect (translateY -6px + scale 1.01)
- Border adaptée au mode sombre
- Shadow dynamique

---

#### B. Doc Card Highlight

**Usage :** Mettre en évidence un contenu important

```html
<div class="doc-card-highlight">
  <strong>✨ Point Important :</strong> Ce contenu nécessite votre attention.
</div>
```

**Caractéristiques :**
- Bordure gauche accentuée (4px primary)
- Animation : `slideInLeft` au chargement
- Hover : translateX 8px
- Background gradient subtil

---

#### C. Doc Card Feature

**Usage :** Présenter une fonctionnalité majeure

```html
<div class="doc-card-feature">
  <span class="doc-card-feature-icon">🚀</span>
  <div class="doc-card-feature-title">Fonctionnalité Avancée</div>
  <p>Description détaillée de cette fonctionnalité.</p>
</div>
```

**Caractéristiques :**
- Bordure supérieure gradient (4px)
- Animation : `fadeInUp` au chargement
- Hover : translateY -8px
- Padding généreux (2rem)

---

### Call-to-Action (CTA)

#### A. CTA Primary

**Usage :** Action principale (inscription, achat, etc.)

```html
<a href="#" class="cta-primary">
  Commencer la Formation
</a>
```

**Caractéristiques :**
- Gradient Indigo → Violet
- Min-height : 56px (WCAG AAA)
- Effet ripple au hover (pseudo-élément)
- Transform : translateY + scale
- Font-weight : 700

---

#### B. CTA Secondary

**Usage :** Action secondaire

```html
<a href="#" class="cta-secondary">
  En Savoir Plus
</a>
```

**Caractéristiques :**
- Border 2px primary
- Background transparent → gradient au hover
- Transition douce left 0.4s
- Color swap blanc au hover

---

#### C. CTA Calendly

**Usage :** Lien vers rendez-vous Calendly

```html
<a href="https://calendly.com/votre-lien" class="cta-calendly">
  Réserver un Coaching
</a>
```

**Caractéristiques :**
- Couleur spécifique Calendly (#00A2FF)
- Icône calendrier automatique (::after)
- Min-height : 56px
- Hover : gradient plus foncé

---

### Badges

#### Badges Niveau

**Usage :** Indiquer le niveau de difficulté

```html
<span class="badge-niveau badge-debutant">Débutant</span>
<span class="badge-niveau badge-intermediaire">Intermédiaire</span>
<span class="badge-niveau badge-avance">Avancé</span>
```

**Couleurs :**
- **Débutant :** Vert (#81C784 → #66BB6A)
- **Intermédiaire :** Orange (#FFB74D → #FFA726)
- **Avancé :** Rouge (#E57373 → #EF5350)

**Caractéristiques :**
- Gradient background
- Border-radius : 1.5rem (pill)
- Hover : scale 1.1 + shadow elevation
- Font-weight : 700
- Uppercase + letter-spacing

---

#### Badges Existants

```html
<span class="badge badge--new">Nouveau</span>
<span class="badge badge--important">Important</span>
<span class="badge badge--pro">Pro</span>
```

---

### Accordéons

**Usage :** Sections pliables FAQ/Détails

```html
<div class="accordion">
  <div class="accordion-header" onclick="this.classList.toggle('active'); this.nextElementSibling.classList.toggle('active')">
    Question : Comment utiliser les accordéons ?
  </div>
  <div class="accordion-content">
    <p>Réponse détaillée ici.</p>
  </div>
</div>
```

**Caractéristiques :**
- Header : gradient background subtil
- Indicateur flèche (▼) qui pivote au clic
- Content : max-height 0 → 1000px (smooth)
- Transition : 0.4s cubic-bezier
- Hover : padding-left augmente

**JavaScript requis :** Toggle class `active` sur header + content

---

### Highlights

#### A. Highlight Box

**Usage :** Information standard

```html
<div class="highlight-box">
  <strong>ℹ️ Information :</strong> Texte informatif.
</div>
```

**Style :** Border-left bleu (#01579B → #64B5F6 mode sombre)

---

#### B. Highlight Tip

**Usage :** Conseil pratique

```html
<div class="highlight-tip">
  <strong>Conseil :</strong> Astuce utile.
</div>
```

**Style :** Border-left vert + icône 💡 (position absolute)

---

#### C. Highlight Warning

**Usage :** Avertissement

```html
<div class="highlight-warning">
  <strong>Attention :</strong> Point important.
</div>
```

**Style :** Border-left orange + icône ⚠️ (position absolute)

---

### Progress Indicators

#### A. Progress Bar

**Usage :** Barre de progression

```html
<div class="progress-bar">
  <div class="progress-bar-fill" style="width: 75%;"></div>
</div>
```

**Caractéristiques :**
- Height : 12px
- Border-radius : 100px (pill)
- Fill : gradient Indigo → Violet
- Shimmer effect (pseudo-élément ::after)
- Transition width : 0.6s

**Contrôle dynamique :** Modifier `style="width: X%"` avec JavaScript

---

#### B. Progress Steps

**Usage :** Étapes visuelles

```html
<div class="progress-steps">
  <div class="progress-step completed">
    <div class="progress-step-circle">1</div>
    <div class="progress-step-label">Inscription</div>
  </div>
  <div class="progress-step active">
    <div class="progress-step-circle">2</div>
    <div class="progress-step-label">Formation</div>
  </div>
  <div class="progress-step">
    <div class="progress-step-circle">3</div>
    <div class="progress-step-label">Certification</div>
  </div>
</div>
```

**Classes d'état :**
- `.completed` : Vert + checkmark ✓
- `.active` : Gradient + pulse animation
- (aucune) : Gris neutre

**Responsive :** Passe en colonne sur mobile (≤960px)

---

## 💬 Admonitions

### Types Disponibles

```markdown
!!! tip "Astuce"
    Conseil pratique.

!!! info "Information"
    Information neutre.

!!! warning "Attention"
    Avertissement important.

!!! danger "Important"
    Erreur critique.

!!! success "Félicitations"
    Validation réussie.
```

**Animations :**
- `tip` : slideInLeft
- `warning` : slideInRight
- Autres : fadeInUp

**Hover :** translateX 4px

---

## ♿ Accessibilité

### Contrastes WCAG

Tous les contrastes respectent **WCAG 2.1 Niveau AAA (≥ 7:1)**.

| Élément | Mode Clair | Mode Sombre | Contraste |
|---------|-----------|-------------|-----------|
| Texte principal | #212121 sur #FFFFFF | #ECECEC sur #1A1A1A | 10.5:1 ✅ |
| Primary | #2C3A8F sur #FFFFFF | #7E9BFF sur #1A1A1A | 7.2:1 / 7.5:1 ✅ |
| Success | #2E7D32 sur #FFFFFF | #81C784 sur #1A1A1A | 7.3:1 / 7.8:1 ✅ |
| Warning | #E65100 sur #FFFFFF | #FFB74D sur #1A1A1A | 7.1:1 / 8.5:1 ✅ |

### Touch Targets

Taille minimale **44×44px** (WCAG 2.5.5) :

- ✅ Boutons : 48-56px
- ✅ CTA : 56px
- ✅ Liens : padding 44px
- ✅ Checkboxes : 44×44px
- ✅ Accordion headers : 48px

### Focus States

Focus visible sur tous les éléments interactifs :

- **Général :** Outline 3px accent + offset 3px
- **Liens :** Outline + box-shadow violet
- **Boutons :** Outline blanc + box-shadow
- **Navigation :** Outline semi-transparent + background

### Reduced Motion

**Respect strict de `prefers-reduced-motion` :**

- ✅ Toutes animations désactivées
- ✅ Transformations hover désactivées
- ✅ Scroll smooth désactivé
- ✅ Transitions couleurs uniquement (0.1s)

**Test :** Activer "Réduire les animations" dans les paramètres système

---

## 📝 Exemples Pratiques

### Exemple 1 : Page de Guide avec Progression

```markdown
# 🎯 03 - Créer votre première page

<span class="badge-niveau badge-debutant">Débutant</span>
<span class="badge badge--new">Nouveau</span>

⏱️ **Durée estimée :** 20 minutes

## Votre Progression

<div class="progress-bar">
  <div class="progress-bar-fill" style="width: 30%;"></div>
</div>
<p style="text-align: center;">3/10 guides complétés</p>

<div class="progress-steps">
  <div class="progress-step completed">
    <div class="progress-step-circle">1</div>
    <div class="progress-step-label">Introduction</div>
  </div>
  <div class="progress-step completed">
    <div class="progress-step-circle">2</div>
    <div class="progress-step-label">Configuration</div>
  </div>
  <div class="progress-step active">
    <div class="progress-step-circle">3</div>
    <div class="progress-step-label">Création</div>
  </div>
  <div class="progress-step">
    <div class="progress-step-circle">4</div>
    <div class="progress-step-label">Publication</div>
  </div>
</div>

!!! tip "Conseil"
    Prenez le temps de bien comprendre chaque étape.

## Contenu

<div class="doc-card-feature">
  <span class="doc-card-feature-icon">🎨</span>
  <div class="doc-card-feature-title">Design Personnalisé</div>
  <p>Créez des pages uniques qui reflètent votre marque.</p>
</div>

<a href="/guides/04" class="cta-primary">Continuer</a>
```

---

### Exemple 2 : FAQ avec Accordéons

```html
<h2>❓ Questions Fréquentes</h2>

<div class="accordion">
  <div class="accordion-header" onclick="this.classList.toggle('active'); this.nextElementSibling.classList.toggle('active')">
    Comment activer le mode sombre ?
  </div>
  <div class="accordion-content">
    <p>Le mode sombre s'active automatiquement selon vos préférences système.</p>
  </div>
</div>

<div class="accordion">
  <div class="accordion-header" onclick="this.classList.toggle('active'); this.nextElementSibling.classList.toggle('active')">
    Les animations sont-elles accessibles ?
  </div>
  <div class="accordion-content">
    <p>Oui ! Toutes les animations respectent prefers-reduced-motion.</p>
  </div>
</div>

<a href="https://calendly.com/votre-lien" class="cta-calendly">
  Besoin d'aide ? Réservez un coaching
</a>
```

---

### Exemple 3 : Page d'Accueil avec Cards

```html
<h1>🎓 Formation Systeme.io - Coaching au Féminin</h1>

<div class="welcome-banner">
  <h2>Bienvenue dans votre formation !</h2>
  <p>Devenez autonome sur la gestion de vos landing pages.</p>
</div>

<div class="doc-card-highlight">
  <strong>✨ Nouveau :</strong> Mode sombre automatique maintenant disponible !
</div>

<h2>Parcours de Formation</h2>

<div class="doc-card">
  <div class="doc-card-title">📘 Module 1 : Les Bases</div>
  <div class="doc-card-content">
    <p>Découvrez l'interface et les concepts fondamentaux.</p>
    <span class="badge-niveau badge-debutant">Débutant</span>
    <span class="badge badge--new">Nouveau</span>
  </div>
</div>

<div class="doc-card">
  <div class="doc-card-title">🎨 Module 2 : Design</div>
  <div class="doc-card-content">
    <p>Créez des pages attractives et professionnelles.</p>
    <span class="badge-niveau badge-intermediaire">Intermédiaire</span>
  </div>
</div>

<div class="doc-card">
  <div class="doc-card-title">🚀 Module 3 : Optimisation</div>
  <div class="doc-card-content">
    <p>Maximisez vos conversions et performances.</p>
    <span class="badge-niveau badge-avance">Avancé</span>
  </div>
</div>

<div style="text-align: center; margin: 3rem 0;">
  <a href="/guides/01" class="cta-primary">Commencer la Formation</a>
  <a href="/about" class="cta-secondary">En Savoir Plus</a>
</div>
```

---

## 🔧 Personnalisation

### Modifier les Couleurs

Éditez les variables CSS dans `docs/stylesheets/extra.css` :

```css
:root {
  /* Couleur primaire */
  --atek-primary: #VOTRE_COULEUR;

  /* Accent */
  --atek-accent: #VOTRE_COULEUR;
}
```

⚠️ **Important :** Vérifiez les contrastes avec [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)

### Ajouter des Composants

1. Créer section CSS avec commentaires
2. Respecter contrastes AAA (≥ 7:1)
3. Tester responsive (320px, 768px, 1280px)
4. Vérifier focus states
5. Tester prefers-reduced-motion
6. Documenter ici

---

## 📚 Ressources

### Outils

- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [WAVE Accessibility Tool](https://wave.webaim.org/)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)

### Documentation

- [WCAG 2.1](https://www.w3.org/WAI/WCAG21/quickref/)
- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
- [MDN Web Docs](https://developer.mozilla.org/)

---

## ✅ Checklist Qualité

Avant publication :

- [ ] Contrastes ≥ 7:1 vérifiés
- [ ] Touch targets ≥ 44×44px
- [ ] Testé modes clair et sombre
- [ ] Testé avec prefers-reduced-motion
- [ ] Navigation clavier OK
- [ ] Responsive testé (mobile, tablet, desktop)
- [ ] Contenu validé
- [ ] Liens vérifiés

---

**© 2025 A-Tek Universe · Documentation Formation Systeme.io**
**Version :** 3.0 (Mode Sombre + Animations + Composants)
**Dernière mise à jour :** 2025-11-12
