## 🎯 Objectif de ce guide

Personnaliser l'apparence visuelle de votre landing page : couleurs, polices, espacements et responsive design.

---

## 1. Charte graphique et cohérence visuelle

### 1.1 Définir votre identité visuelle

Avant toute modification, identifiez votre palette de couleurs :

**Votre palette actuelle (à définir) :**

|Élément|Couleur|Code Hexa|Usage|
|---|---|---|---|
|**Primaire**|[À définir]|#XXXXXX|Titres, CTA principaux|
|**Secondaire**|[À définir]|#XXXXXX|Sous-titres, accents|
|**Texte principal**|Noir/Gris foncé|#333333|Corps de texte|
|**Texte secondaire**|Gris moyen|#666666|Légendes, dates|
|**Fond**|Blanc/Beige clair|#FFFFFF|Arrière-plans|
|**Accent**|[À définir]|#XXXXXX|Éléments cliquables|

> 💡 **Outil recommandé :** Adobe Color (https://color.adobe.com) pour créer des palettes harmonieuses.

### 1.2 Psychologie des couleurs pour le coaching

|Couleur|Émotion|Recommandation|
|---|---|---|
|**Bleu**|Confiance, calme|✅ Excellent pour coaching juridique|
|**Rose/Mauve**|Douceur, féminité|✅ Parfait pour coaching féminin|
|**Vert**|Nature, équilibre|✅ Bien-être, transition|
|**Or/Beige**|Élégance, chaleur|✅ Premium, accompagnement|
|**Rouge**|Urgence, passion|⚠️ À utiliser avec parcimonie|
|**Noir**|Luxe, sophistication|⚠️ Peut sembler froid seul|

---

## 2. Modifier les couleurs

### 2.1 Couleur d'un bloc de texte

1. Cliquez sur le bloc de texte
2. Panneau de droite > **Style** > **Couleur**
3. Choisissez :
    - **Palette prédéfinie** : Couleurs de votre thème
    - **Personnalisée** : Code hexadécimal
    - **Pipette** : Copier une couleur existante

**Entrée manuelle d'un code couleur :**

```
Couleur: [#] [4][A][9][0][E][2]
         ↑   ↑ Code hexadécimal
```

### 2.2 Couleur de fond d'une section

1. Cliquez sur la section (pas le texte, mais le bloc entier)
2. Panneau > **Fond (Background)**
3. Options :
    - **Couleur unie** : 1 seule couleur
    - **Dégradé (Gradient)** : Transition entre 2 couleurs
    - **Image** : Photo de fond

**Utiliser un dégradé :**

```
┌────────────────────────────┐
│ Type: [Dégradé ▼]         │
│ Couleur 1: [#FFFFFF]      │
│ Couleur 2: [#F0F0F0]      │
│ Direction: [Haut→Bas ▼]   │
│ Angle: [0°]               │
└────────────────────────────┘
```

### 2.3 Couleur des boutons CTA

1. Cliquez sur le bouton
2. Panneau > **Style** > **Couleur**
3. Configurez :
    - **Fond (Background)** : Couleur principale
    - **Texte** : Contraste élevé (blanc généralement)
    - **Bordure (Border)** : Même couleur ou transparente
    - **Survol (Hover)** : Version plus foncée (auto ou manuelle)

**États du bouton :**

|État|Effet|Configuration|
|---|---|---|
|**Normal**|Au repos|Couleur primaire|
|**Hover**|Souris dessus|10-20% plus foncé|
|**Active**|Clic en cours|20-30% plus foncé|
|**Focus**|Sélectionné (clavier)|Bordure visible|

---

## 3. Typographie (Polices)

### 3.1 Hiérarchie typographique

**Règle de base :**

```
Titre H1:    48px - Gras
Titre H2:    36px - Gras
Titre H3:    28px - Gras
Corps:       16px - Normal
Légende:     14px - Normal
```

### 3.2 Modifier la police d'un texte

1. Sélectionnez le texte
2. Panneau > **Police (Font Family)**
3. Choisissez dans la liste Systeme.io

**Polices recommandées pour coaching :**

|Police|Style|Usage|Personnalité|
|---|---|---|---|
|**Montserrat**|Sans-serif|Titres|Moderne, clean|
|**Open Sans**|Sans-serif|Textes|Lisible, neutre|
|**Lora**|Serif|Titres élégants|Chaleureux, féminin|
|**Raleway**|Sans-serif|Tout usage|Élégant, aéré|
|**Playfair Display**|Serif|Titres premium|Luxe, sophistiqué|

> 💡 **Conseil :** Maximum 2 polices différentes sur la page (1 pour titres, 1 pour textes).

### 3.3 Taille et style de texte

**Panneau de propriétés :**

```
┌────────────────────────────┐
│ Typographie               │
│ ├─ Police: [Montserrat ▼]│
│ ├─ Taille: [16] px       │
│ ├─ Poids: [Normal ▼]     │
│ │   (Thin, Light, Normal,│
│ │    Medium, Bold, Black)│
│ ├─ Style: [ ] Italique   │
│ ├─ Hauteur de ligne: [1.5]│
│ ├─ Espacement lettres: [0]│
│ └─ Transformation:        │
│     [Aucune ▼]            │
└────────────────────────────┘
```

**Poids de police (Font Weight) :**

- **300 (Light)** : Textes secondaires, légendes
- **400 (Normal)** : Corps de texte standard
- **600 (Semi-Bold)** : Mise en valeur dans le texte
- **700 (Bold)** : Titres, CTA

### 3.4 Lisibilité et accessibilité

**Bonnes pratiques :**

- ✅ Taille minimum 16px pour corps de texte
- ✅ Hauteur de ligne (line-height) : 1.5 minimum
- ✅ Longueur de ligne : 50-75 caractères max
- ✅ Contraste texte/fond : minimum 4.5:1
- ❌ Éviter texte en capitales sur plusieurs lignes
- ❌ Éviter italique pour longs paragraphes

---

## 4. Espacements et marges

### 4.1 Types d'espacements

```
┌─────────────────────────────────────┐
│ Margin (Marge externe)              │
│   ┌─────────────────────────────┐   │
│   │ Padding (Marge interne)     │   │
│   │   ┌─────────────────────┐   │   │
│   │   │ CONTENU             │   │   │
│   │   └─────────────────────┘   │   │
│   └─────────────────────────────┘   │
└─────────────────────────────────────┘
```

**Différence :**

- **Margin** : Espace entre blocs
- **Padding** : Espace à l'intérieur du bloc

### 4.2 Modifier les espacements d'un bloc

1. Cliquez sur le bloc
2. Panneau > **Espacement (Spacing)**
3. Configurez :
    
    ```
    ┌────────────────────────────┐│ Margin (externe)          ││ ├─ Haut:    [20] px      ││ ├─ Droite:  [0] px       ││ ├─ Bas:     [20] px      ││ └─ Gauche:  [0] px       ││                           ││ Padding (interne)         ││ ├─ Haut:    [15] px      ││ ├─ Droite:  [15] px      ││ ├─ Bas:     [15] px      ││ └─ Gauche:  [15] px      │└────────────────────────────┘
    ```
    

### 4.3 Espacements recommandés

|Élément|Margin Top|Margin Bottom|Padding|
|---|---|---|---|
|Titre H1|0px|30px|0px|
|Titre H2|60px|20px|0px|
|Paragraphe|0px|20px|0px|
|Section|80px|80px|40px|
|Bouton CTA|30px|30px|15px 30px|

### 4.4 Système d'espacement cohérent

Utilisez un système basé sur 8px :

```
8px, 16px, 24px, 32px, 40px, 48px, 56px, 64px, 80px
```

**Pourquoi ?**

- ✅ Cohérence visuelle
- ✅ Proportions harmonieuses
- ✅ Alignement pixel-perfect
- ✅ Design professionnel

---

## 5. Responsive Design (Mobile/Tablette)

### 5.1 Principe du Responsive

Votre page doit s'adapter à toutes les tailles d'écran :

```
┌──────────────┐  ┌─────────┐  ┌────┐
│   Desktop    │  │ Tablet  │  │ 📱 │
│   1920px     │  │  768px  │  │375 │
└──────────────┘  └─────────┘  └────┘
```

### 5.2 Basculer entre les vues

En bas de l'éditeur Systeme.io :

|Icône|Vue|Largeur|Usage prioritaire|
|---|---|---|---|
|💻|Desktop|1920px|Ordinateurs|
|📱|Tablet|768px|Tablettes, iPad|
|📱|Mobile|375px|Smartphones|

### 5.3 Règles d'adaptation mobile

#### Tailles de police

|Élément|Desktop|Mobile|
|---|---|---|
|H1|48px|32px|
|H2|36px|28px|
|H3|28px|22px|
|Corps|16px|16px|

#### Espacements

|Élément|Desktop|Mobile|
|---|---|---|
|Section padding|80px|40px|
|Margin entre blocs|60px|30px|
|CTA height|56px|48px|

#### Disposition

**Desktop :**

```
┌────────────┬────────────┐
│  Texte     │   Image    │
│  50%       │   50%      │
└────────────┴────────────┘
```

**Mobile :**

```
┌────────────────────────┐
│        Image           │
├────────────────────────┤
│        Texte           │
│        100%            │
└────────────────────────┘
```

### 5.4 Vérifier le responsive

**Checklist mobile :**

- [ ] Textes lisibles sans zoom
- [ ] Boutons cliquables facilement (min 44x44px)
- [ ] Images non déformées
- [ ] Pas de défilement horizontal
- [ ] CTA bien visibles
- [ ] Formulaires utilisables
- [ ] Chargement rapide (< 3 sec)

**Tester sur vrais appareils :**

1. Prenez votre smartphone
2. Ouvrez votre landing page
3. Naviguez complètement
4. Testez tous les CTA
5. Notez les problèmes

---

## 6. Bordures, ombres et effets

### 6.1 Bordures (Borders)

**Configuration :**

```
┌────────────────────────────┐
│ Bordure                   │
│ ├─ Style: [Solide ▼]     │
│ ├─ Largeur: [1] px       │
│ ├─ Couleur: [#E0E0E0]    │
│ └─ Rayon (arrondi): [8] px│
└────────────────────────────┘
```

**Styles de bordure :**

- **Solid** : Trait continu (standard)
- **Dashed** : Pointillés
- **Dotted** : Points
- **None** : Aucune bordure

**Utilisation :**

- Séparer des sections
- Mettre en évidence une zone
- Créer des cartes (cards)

### 6.2 Ombres (Shadows)

**Pourquoi utiliser des ombres ?**

- ✅ Profondeur visuelle
- ✅ Hiérarchie des éléments
- ✅ Effet moderne
- ✅ Mise en avant

**Configuration ombre :**

```
┌────────────────────────────┐
│ Ombre                     │
│ ├─ Type: [Externe ▼]     │
│ ├─ X: [0] px             │
│ ├─ Y: [4] px             │
│ ├─ Flou: [12] px         │
│ ├─ Étendue: [0] px       │
│ └─ Couleur: [#000 20%]   │
└────────────────────────────┘
```

**Exemples d'ombres :**

|Usage|Configuration|Rendu|
|---|---|---|
|**Subtile**|Y:2px Flou:4px|Élégant, discret|
|**Card**|Y:4px Flou:12px|Carte, bloc|
|**Forte**|Y:8px Flou:24px|CTA, popup|
|**Intérieure**|Type:Interne|Effet enfoncé|

### 6.3 Arrondir les coins

**Configuration :**

```
Border Radius: [8] px
```

**Degrés d'arrondi :**

- **0px** : Coins carrés (strict, formel)
- **4-8px** : Légèrement arrondi (moderne, doux)
- **12-16px** : Arrondi prononcé (friendly, accueillant)
- **50%** : Cercle parfait (si carré) ou pilule

**Utilisation :**

- Images : 8-12px
- Boutons : 4-8px (ou 50% pour pilule)
- Cards : 8-16px
- Sections : 0-8px

---

## 7. Images et médias

### 7.1 Filtres d'image

Appliquer des effets visuels aux images :

**Panneau d'effets :**

```
┌────────────────────────────┐
│ Filtres d'image           │
│ ├─ Luminosité: [100] %   │
│ ├─ Contraste: [100] %    │
│ ├─ Saturation: [100] %   │
│ ├─ Opacité: [100] %      │
│ ├─ Flou: [0] px          │
│ ├─ Sépia: [0] %          │
│ └─ Niveaux de gris: [0]% │
└────────────────────────────┘
```

**Cas d'usage :**

|Effet|Configuration|Usage|
|---|---|---|
|**Image en arrière-plan**|Opacité: 30%, Luminosité: 120%|Lisibilité du texte|
|**Photo noir et blanc**|Niveaux de gris: 100%|Style intemporel|
|**Image atténuée**|Saturation: 50%, Luminosité: 110%|Harmonie colorimétrique|

### 7.2 Superposition (Overlay)

Ajouter une couche colorée sur une image de fond :

```
┌────────────────────────────┐
│ Superposition             │
│ ├─ Activé: [✓]           │
│ ├─ Couleur: [#000000]    │
│ ├─ Opacité: [50] %       │
│ └─ Mode: [Multiplier ▼]  │
└────────────────────────────┘
```

**Usage typique :**

- Image de fond + overlay noir 50% + texte blanc
- Garantit lisibilité du texte sur toute image

---

## 8. Thème et templates

### 8.1 Utiliser un thème existant

Systeme.io propose des thèmes prédéfinis :

1. Dans l'éditeur, cliquez sur **"Thèmes"** ou **"Templates"**
2. Parcourez les thèmes disponibles
3. Survolez un thème pour prévisualiser
4. Cliquez sur **"Appliquer"**

> ⚠️ **Attention :** Appliquer un nouveau thème écrase le design actuel. Enregistrez une copie de votre page avant.

### 8.2 Créer votre propre thème

**Avantage :** Réutiliser les couleurs/polices sur d'autres pages.

**Procédure :**

1. Configurez votre page avec couleurs/polices
2. Menu **"Paramètres"** > **"Thème"**
3. Cliquez **"Enregistrer comme nouveau thème"**
4. Nommez le thème : "Essentiel en Soi Brand"
5. Validez

**Votre thème contient :**

- Palette de couleurs
- Polices (titres et corps)
- Espacements par défaut
- Styles de boutons

---

## 9. Checklist Design

Avant de publier :

### ✅ Cohérence visuelle

- [ ] Maximum 3 couleurs principales
- [ ] Maximum 2 polices
- [ ] Espacements cohérents (système 8px)
- [ ] Arrondi uniforme sur tous les boutons
- [ ] Ombres similaires sur éléments similaires

### ✅ Accessibilité

- [ ] Contraste texte/fond ≥ 4.5:1
- [ ] Taille de texte ≥ 16px
- [ ] Boutons ≥ 44x44px (mobile)
- [ ] Alt text sur toutes les images
- [ ] Navigation possible au clavier

### ✅ Responsive

- [ ] Testé sur Desktop (1920px)
- [ ] Testé sur Tablet (768px)
- [ ] Testé sur Mobile (375px)
- [ ] Aucun défilement horizontal
- [ ] Textes lisibles sans zoom
- [ ] Images non déformées

### ✅ Performance

- [ ] Images optimisées (< 200Ko)
- [ ] Pas de vidéos en autoplay
- [ ] Chargement de page < 3 sec
- [ ] Fonts chargées efficacement

---

## 10. Outils recommandés

### Couleurs

- **Adobe Color** : https://color.adobe.com
- **Coolors** : https://coolors.co
- **Contrast Checker** : https://webaim.org/resources/contrastchecker/

### Polices

- **Google Fonts** : https://fonts.google.com
- **Font Pair** : https://fontpair.co

### Images

- **Unsplash** : https://unsplash.com (photos gratuites)
- **Pexels** : https://www.pexels.com
- **TinyPNG** : https://tinypng.com (optimisation)

### Inspiration Design

- **Dribbble** : https://dribbble.com
- **Behance** : https://www.behance.net
- **Awwwards** : https://www.awwwards.com

---

**Prochaine étape : [Guide 05 - Formulaires et collecte de données](05-FORMULAIRES-DONNEES.md) 📝**