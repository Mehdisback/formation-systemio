# 🎨 04 - Design et mise en page

⏱️ **Durée estimée** : 60 minutes
📊 **Niveau** : Intermédiaire

## 🎯 Objectifs

À la fin de ce guide, vous saurez :

- [ ] Définir et appliquer votre charte graphique
- [ ] Modifier les couleurs, polices et espacements
- [ ] Créer un design responsive (adaptatif mobile/tablette)
- [ ] Utiliser les bordures, ombres et effets visuels
- [ ] Optimiser les images et médias
- [ ] Garantir l'accessibilité et la cohérence visuelle

---

## 🎨 Charte graphique et cohérence visuelle

### Définir votre identité visuelle

Avant toute modification, identifiez votre palette de couleurs.

**Votre palette actuelle (à définir) :**

| Élément | Couleur | Code Hexa | Usage |
|---------|---------|-----------|-------|
| **Primaire** | [À définir] | #XXXXXX | Titres, CTA principaux |
| **Secondaire** | [À définir] | #XXXXXX | Sous-titres, accents |
| **Texte principal** | Noir/Gris foncé | #333333 | Corps de texte |
| **Texte secondaire** | Gris moyen | #666666 | Légendes, dates |
| **Fond** | Blanc/Beige clair | #FFFFFF | Arrière-plans |
| **Accent** | [À définir] | #XXXXXX | Éléments cliquables |

!!! tip "💡 Outil recommandé"
    Utilisez [Adobe Color](https://color.adobe.com) ou [Coolors](https://coolors.co) pour créer des palettes harmonieuses. Ces outils génèrent des combinaisons de couleurs qui fonctionnent bien ensemble.

### Psychologie des couleurs pour le coaching

| Couleur | Émotion | Recommandation |
|---------|---------|----------------|
| **Bleu** | Confiance, calme | ✅ Excellent pour coaching professionnel |
| **Rose/Mauve** | Douceur, féminité | ✅ Parfait pour coaching au féminin |
| **Vert** | Nature, équilibre | ✅ Bien-être, transition de vie |
| **Or/Beige** | Élégance, chaleur | ✅ Premium, accompagnement haut de gamme |
| **Rouge** | Urgence, passion | ⚠️ À utiliser avec parcimonie |
| **Noir** | Luxe, sophistication | ⚠️ Peut sembler froid seul |

!!! info "ℹ️ Choix des couleurs"
    Pour le coaching au féminin, privilégiez les teintes douces (rose, mauve, beige) qui évoquent la bienveillance et l'écoute. Évitez les couleurs trop agressives ou froides.

---

## 🎨 Modifier les couleurs

### Couleur d'un bloc de texte

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

### Couleur de fond d'une section

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

!!! tip "💡 Astuce dégradé"
    Pour un effet subtil et élégant, utilisez deux nuances de la même couleur (exemple : #F8F8F8 vers #FFFFFF). Les dégradés prononcés peuvent sembler datés.

### Couleur des boutons CTA

1. Cliquez sur le bouton
2. Panneau > **Style** > **Couleur**
3. Configurez :
    - **Fond (Background)** : Couleur principale
    - **Texte** : Contraste élevé (blanc généralement)
    - **Bordure (Border)** : Même couleur ou transparente
    - **Survol (Hover)** : Version plus foncée (auto ou manuelle)

**États du bouton :**

| État | Effet | Configuration |
|------|-------|---------------|
| **Normal** | Au repos | Couleur primaire |
| **Hover** | Souris dessus | 10-20% plus foncé |
| **Active** | Clic en cours | 20-30% plus foncé |
| **Focus** | Sélectionné (clavier) | Bordure visible |

!!! warning "⚠️ Accessibilité des boutons"
    Assurez-vous que l'état "hover" est bien visible mais pas trop différent. Les utilisateurs doivent comprendre qu'ils peuvent cliquer sans être surpris par un changement trop brutal.

---

## 🔤 Typographie (Polices)

### Hiérarchie typographique

**Règle de base :**

```
Titre H1:    48px - Gras
Titre H2:    36px - Gras
Titre H3:    28px - Gras
Corps:       16px - Normal
Légende:     14px - Normal
```

### Modifier la police d'un texte

1. Sélectionnez le texte
2. Panneau > **Police (Font Family)**
3. Choisissez dans la liste Systeme.io

**Polices recommandées pour coaching :**

| Police | Style | Usage | Personnalité |
|--------|-------|-------|--------------|
| **Montserrat** | Sans-serif | Titres | Moderne, clean |
| **Open Sans** | Sans-serif | Textes | Lisible, neutre |
| **Lora** | Serif | Titres élégants | Chaleureux, féminin |
| **Raleway** | Sans-serif | Tout usage | Élégant, aéré |
| **Playfair Display** | Serif | Titres premium | Luxe, sophistiqué |

!!! tip "💡 Conseil typographique"
    Maximum 2 polices différentes sur la page : 1 pour les titres, 1 pour les textes. Plus de polices = design brouillon et amateur.

### Taille et style de texte

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

| Poids | Valeur | Usage |
|-------|--------|-------|
| **Light** | 300 | Textes secondaires, légendes |
| **Normal** | 400 | Corps de texte standard |
| **Semi-Bold** | 600 | Mise en valeur dans le texte |
| **Bold** | 700 | Titres, CTA |

### Lisibilité et accessibilité

**Bonnes pratiques :**

- ✅ Taille minimum 16px pour corps de texte
- ✅ Hauteur de ligne (line-height) : 1.5 minimum
- ✅ Longueur de ligne : 50-75 caractères max
- ✅ Contraste texte/fond : minimum 4.5:1
- ❌ Éviter texte en capitales sur plusieurs lignes
- ❌ Éviter italique pour longs paragraphes

!!! warning "⚠️ Lisibilité critique"
    Un texte illisible fait fuir vos visiteurs. Privilégiez toujours la lisibilité au style. Testez votre page en conditions réelles (écran d'ordinateur à 1m de distance).

---

## 📐 Espacements et marges

### Types d'espacements

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

- **Margin** : Espace entre blocs (extérieur)
- **Padding** : Espace à l'intérieur du bloc

### Modifier les espacements d'un bloc

1. Cliquez sur le bloc
2. Panneau > **Espacement (Spacing)**
3. Configurez :

```
┌────────────────────────────┐
│ Margin (externe)          │
│ ├─ Haut:    [20] px      │
│ ├─ Droite:  [0] px       │
│ ├─ Bas:     [20] px      │
│ └─ Gauche:  [0] px       │
│                           │
│ Padding (interne)         │
│ ├─ Haut:    [15] px      │
│ ├─ Droite:  [15] px      │
│ ├─ Bas:     [15] px      │
│ └─ Gauche:  [15] px      │
└────────────────────────────┘
```

### Espacements recommandés

| Élément | Margin Top | Margin Bottom | Padding |
|---------|------------|---------------|---------|
| Titre H1 | 0px | 30px | 0px |
| Titre H2 | 60px | 20px | 0px |
| Paragraphe | 0px | 20px | 0px |
| Section | 80px | 80px | 40px |
| Bouton CTA | 30px | 30px | 15px 30px |

### Système d'espacement cohérent

Utilisez un système basé sur 8px :

```
8px, 16px, 24px, 32px, 40px, 48px, 56px, 64px, 80px
```

**Pourquoi ?**

- ✅ Cohérence visuelle automatique
- ✅ Proportions harmonieuses
- ✅ Alignement pixel-perfect
- ✅ Design professionnel

!!! tip "💡 Règle du 8"
    En utilisant toujours des multiples de 8px, votre design sera automatiquement plus cohérent et agréable à l'œil. C'est une règle utilisée par tous les grands designers.

---

## 📱 Responsive Design (Mobile/Tablette)

### Principe du Responsive

Votre page doit s'adapter à toutes les tailles d'écran :

```
┌──────────────┐  ┌─────────┐  ┌────┐
│   Desktop    │  │ Tablet  │  │ 📱 │
│   1920px     │  │  768px  │  │375 │
└──────────────┘  └─────────┘  └────┘
```

!!! danger "🚨 Mobile prioritaire"
    Plus de 60% de vos visiteurs sont sur mobile. Testez TOUJOURS votre page en vue mobile avant de publier. Une page cassée sur mobile = perte de clients.

### Basculer entre les vues

En bas de l'éditeur Systeme.io :

| Icône | Vue | Largeur | Usage prioritaire |
|-------|-----|---------|-------------------|
| 💻 | Desktop | 1920px | Ordinateurs |
| 📱 | Tablet | 768px | Tablettes, iPad |
| 📱 | Mobile | 375px | Smartphones |

### Règles d'adaptation mobile

#### Tailles de police

| Élément | Desktop | Mobile |
|---------|---------|--------|
| H1 | 48px | 32px |
| H2 | 36px | 28px |
| H3 | 28px | 22px |
| Corps | 16px | 16px |

#### Espacements

| Élément | Desktop | Mobile |
|---------|---------|--------|
| Section padding | 80px | 40px |
| Margin entre blocs | 60px | 30px |
| CTA height | 56px | 48px |

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

### Vérifier le responsive

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

!!! tip "💡 Test réel indispensable"
    L'aperçu mobile de l'éditeur est utile, mais ne remplace jamais un test sur un vrai téléphone. Testez avec votre propre smartphone et demandez à 2-3 personnes de faire de même.

---

## ✨ Bordures, ombres et effets

### Bordures (Borders)

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

| Style | Description | Usage |
|-------|-------------|-------|
| **Solid** | Trait continu | Standard, recommandé |
| **Dashed** | Pointillés | Séparation légère |
| **Dotted** | Points | Décoratif |
| **None** | Aucune bordure | Design minimaliste |

**Utilisation :**

- Séparer des sections
- Mettre en évidence une zone
- Créer des cartes (cards)

### Ombres (Shadows)

**Pourquoi utiliser des ombres ?**

- ✅ Profondeur visuelle
- ✅ Hiérarchie des éléments
- ✅ Effet moderne et professionnel
- ✅ Mise en avant de CTA

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

| Usage | Configuration | Rendu |
|-------|---------------|-------|
| **Subtile** | Y:2px Flou:4px | Élégant, discret |
| **Card** | Y:4px Flou:12px | Carte, bloc de contenu |
| **Forte** | Y:8px Flou:24px | CTA, popup |
| **Intérieure** | Type:Interne | Effet enfoncé |

!!! warning "⚠️ Modération des ombres"
    Trop d'ombres = design surchargé. Réservez les ombres prononcées aux éléments vraiment importants (CTA principaux, popups).

### Arrondir les coins

**Configuration :**

```
Border Radius: [8] px
```

**Degrés d'arrondi :**

| Valeur | Style | Personnalité |
|--------|-------|--------------|
| **0px** | Coins carrés | Strict, formel |
| **4-8px** | Légèrement arrondi | Moderne, doux |
| **12-16px** | Arrondi prononcé | Friendly, accueillant |
| **50%** | Cercle/pilule | Dynamique, jeune |

**Utilisation recommandée :**

- Images : 8-12px
- Boutons : 4-8px (ou 50% pour pilule)
- Cards : 8-16px
- Sections : 0-8px

---

## 🖼️ Images et médias

### Filtres d'image

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

| Effet | Configuration | Usage |
|-------|---------------|-------|
| **Image en arrière-plan** | Opacité: 30%, Luminosité: 120% | Lisibilité du texte par-dessus |
| **Photo noir et blanc** | Niveaux de gris: 100% | Style intemporel, élégant |
| **Image atténuée** | Saturation: 50%, Luminosité: 110% | Harmonie avec la charte graphique |

### Superposition (Overlay)

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

!!! tip "💡 Astuce overlay"
    Pour un texte blanc sur image de fond, utilisez toujours un overlay noir à 40-60%. Cela garantit que le texte reste lisible même si l'image change.

---

## 🎭 Thème et templates

### Utiliser un thème existant

Systeme.io propose des thèmes prédéfinis :

1. Dans l'éditeur, cliquez sur **"Thèmes"** ou **"Templates"**
2. Parcourez les thèmes disponibles
3. Survolez un thème pour prévisualiser
4. Cliquez sur **"Appliquer"**

!!! danger "🚨 Attention : Sauvegarde obligatoire"
    Appliquer un nouveau thème écrase votre design actuel. **Enregistrez une copie de votre page avant** en dupliquant le funnel.

### Créer votre propre thème

**Avantage :** Réutiliser vos couleurs/polices sur d'autres pages.

**Procédure :**

1. Configurez votre page avec couleurs/polices
2. Menu **"Paramètres"** > **"Thème"**
3. Cliquez **"Enregistrer comme nouveau thème"**
4. Nommez le thème : "Essentiel en Soi Brand"
5. Validez

**Votre thème contient :**

- Palette de couleurs complète
- Polices (titres et corps)
- Espacements par défaut
- Styles de boutons

---

## 🆘 Questions fréquentes et dépannage

### Mes couleurs ne s'affichent pas correctement

**Causes possibles :**

1. Code hexadécimal incorrect
2. Cache du navigateur
3. Thème qui surcharge les couleurs

**Solutions :**

1. Vérifiez que le code commence par # et contient 6 caractères
2. Videz le cache (++ctrl+shift+r++)
3. Réappliquez la couleur directement sur l'élément

### Le texte est illisible sur mon image de fond

**Cause :** Contraste insuffisant entre texte et image.

**Solutions :**

1. Ajoutez un overlay noir à 50%
2. Augmentez la luminosité de l'image
3. Utilisez du texte avec ombre portée
4. Placez le texte sur une zone unie de l'image

### Mon design est différent sur mobile

**Cause :** Systeme.io adapte automatiquement certains éléments.

**Solution :**

1. Passez en vue mobile dans l'éditeur
2. Ajustez les tailles/espacements spécifiquement pour mobile
3. Testez sur un vrai appareil

### Les espacements sont incohérents

**Cause :** Valeurs arbitraires sans système.

**Solution :**

1. Adoptez le système des multiples de 8px
2. Passez en revue tous vos blocs
3. Uniformisez progressivement

---

## ✅ Checklist de validation

Avant de publier, assurez-vous d'avoir :

### Cohérence visuelle

- [ ] Maximum 3 couleurs principales utilisées
- [ ] Maximum 2 polices différentes
- [ ] Espacements cohérents (système 8px)
- [ ] Arrondi uniforme sur tous les boutons
- [ ] Ombres similaires sur éléments similaires
- [ ] Style visuel homogène sur toute la page

### Accessibilité

- [ ] Contraste texte/fond ≥ 4.5:1 partout
- [ ] Taille de texte ≥ 16px pour le corps
- [ ] Boutons ≥ 44x44px (mobile)
- [ ] Alt text sur toutes les images importantes
- [ ] Navigation possible au clavier
- [ ] Hiérarchie des titres respectée (H1 → H2 → H3)

### Responsive

- [ ] Testé sur Desktop (1920px)
- [ ] Testé sur Tablet (768px)
- [ ] Testé sur Mobile (375px)
- [ ] Aucun défilement horizontal sur aucune vue
- [ ] Textes lisibles sans zoom sur mobile
- [ ] Images non déformées sur toutes les vues
- [ ] CTA accessibles facilement sur mobile

### Performance

- [ ] Images optimisées (< 200Ko chacune)
- [ ] Pas de vidéos en autoplay
- [ ] Chargement de page < 3 secondes
- [ ] Fonts chargées efficacement
- [ ] Pas d'animations lourdes

!!! success "🎉 Félicitations !"
    Votre page a maintenant un design professionnel, cohérent et accessible ! Un bon design augmente la crédibilité et les conversions de 40% en moyenne.

---

## 🔗 Navigation

- ⬅️ **Précédent** : [03 - Gestion des CTA et Calendly](03-GESTION-CTA-CALENDLY.md)
- ➡️ **Suivant** : [05 - Formulaires et données](05-FORMULAIRES-DONNEES.md)
- 🏠 **Accueil** : [Retour à l'accueil](index.md)

---

## 📚 Ressources complémentaires

### Outils couleurs

- [Adobe Color](https://color.adobe.com) - Créateur de palettes
- [Coolors](https://coolors.co) - Générateur de combinaisons
- [Contrast Checker](https://webaim.org/resources/contrastchecker/) - Vérification accessibilité

### Outils polices

- [Google Fonts](https://fonts.google.com) - Polices gratuites
- [Font Pair](https://fontpair.co) - Combinaisons de polices

### Outils images

- [Unsplash](https://unsplash.com) - Photos gratuites haute qualité
- [Pexels](https://www.pexels.com) - Banque d'images libres
- [TinyPNG](https://tinypng.com) - Optimisation d'images

### Inspiration design

- [Dribbble](https://dribbble.com) - Inspiration design
- [Behance](https://www.behance.net) - Portfolios créatifs
- [Awwwards](https://www.awwwards.com) - Meilleurs sites web

---

**Prêt à continuer ? Passez au [Guide 05 - Formulaires et données](05-FORMULAIRES-DONNEES.md) !** 📝
