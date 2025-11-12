# 🔘 03 - Gestion des CTA et Calendly

⏱️ **Durée estimée** : 45 minutes
📊 **Niveau** : Intermédiaire

## 🎯 Objectifs

À la fin de ce guide, vous saurez :

- [ ] Comprendre et créer des Call-to-Actions (CTA) efficaces
- [ ] Modifier le texte et le style de vos boutons CTA
- [ ] Positionner stratégiquement vos CTA sur la page
- [ ] Intégrer et tester votre lien Calendly
- [ ] Optimiser vos CTA pour maximiser les conversions
- [ ] Résoudre les problèmes courants d'intégration

---

## 📖 Comprendre les CTA (Call-to-Action)

### Qu'est-ce qu'un CTA ?

Un **Call-to-Action** (Appel à l'action) est un élément qui incite le visiteur à effectuer une action précise.

**Sur votre page, les CTA sont :**

- Les boutons "Réservez votre séance découverte gratuite"
- Les liens textuels vers Calendly
- Tout élément cliquable menant à une action de conversion

### Types de CTA sur votre landing page

#### CTA Principal (Primary CTA)

```
┌─────────────────────────────────────┐
│  [Réservez votre séance découverte] │
│         gratuite (30 min)           │
└─────────────────────────────────────┘
```

| Caractéristique | Description |
|-----------------|-------------|
| **Couleur** | Accent (couleur principale de votre marque) |
| **Position** | En-tête, milieu, et fin de page |
| **Taille** | Grande, très visible |
| **Action** | Ouvre Calendly pour réservation |

#### CTA Secondaires

- Liens textuels vers la prise de contact
- Boutons "En savoir plus" vers sections spécifiques
- Boutons de navigation internes

### Anatomie d'un CTA efficace

```
┌────────────────────────────────────────┐
│  [VERBE D'ACTION] + [BÉNÉFICE]        │
│                                        │
│  Exemple :                             │
│  "Je réserve ma séance GRATUITE"      │
│                                        │
│  ✅ Action claire                      │
│  ✅ 1ère personne ("Je")               │
│  ✅ Bénéfice mis en avant (GRATUITE)  │
│  ✅ Sans engagement sous-entendu       │
└────────────────────────────────────────┘
```

**Éléments clés d'un bon CTA :**

1. **Verbe d'action** : Réserver, Découvrir, Commencer, Télécharger
2. **Bénéfice** : Gratuit, Rapide, Sans engagement
3. **Urgence** (optionnelle) : Maintenant, Aujourd'hui, Places limitées
4. **1ère personne** : "Je réserve" (plus engageant que "Réserver")

!!! tip "💡 Conseil de rédaction"
    Utilisez la première personne ("Je réserve") plutôt que l'infinitif ("Réserver"). C'est plus engageant et augmente le taux de conversion de 15% en moyenne.

---

## ✏️ Modifier vos boutons CTA

### Accéder aux paramètres d'un bouton

1. Dans l'éditeur, **cliquez sur le bouton CTA**
2. Le panneau de propriétés s'ouvre à droite

### Modifier le texte du bouton

#### Panneau de propriétés

```
┌─────────────────────────────────────┐
│ PROPRIÉTÉS DU BOUTON                │
├─────────────────────────────────────┤
│ Contenu                             │
│ ├─ Texte du bouton :                │
│ │  [Réservez votre séance...     ] │
│ │                                   │
│ ├─ Sous-texte (optionnel) :        │
│ │  [30 minutes - Sans engagement ] │
│ │                                   │
│ Style                               │
│ ├─ Style: [Plein ▼]                │
│ ├─ Taille: [Grande ▼]              │
│ ├─ Couleur: [■ #4A90E2]           │
│ ├─ Forme: [Arrondie ▼]            │
│ │                                   │
│ Action                              │
│ ├─ Type: [Lien externe ▼]         │
│ └─ URL: [calendly.com/...       ] │
└─────────────────────────────────────┘
```

#### Modifier le texte

1. Cliquez dans le champ **"Texte du bouton"**
2. Supprimez l'ancien texte
3. Tapez le nouveau texte
4. Ajoutez un sous-texte si pertinent

**Exemples de textes efficaces :**

| Objectif | Texte du bouton | Sous-texte |
|----------|-----------------|------------|
| Séance découverte | "Je réserve ma séance gratuite" | "30 min - Sans engagement" |
| Premier contact | "Parlons-en ensemble" | "Échange confidentiel" |
| Urgence | "Réserver maintenant" | "Places limitées ce mois-ci" |
| Bas engagement | "Découvrir l'accompagnement" | "Séance découverte offerte" |

### Personnaliser le style du bouton

#### Couleur

**Couleur principale (Primary) :**

- Utilisez votre couleur de marque
- Contraste élevé avec le fond (minimum 4.5:1 pour accessibilité)
- Testez sur mobile

!!! warning "⚠️ Contraste et accessibilité"
    Vérifiez toujours le contraste de votre bouton avec [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/). Un contraste insuffisant rend votre CTA invisible pour certains visiteurs.

**Exemples de contraste :**

- ✅ Blanc sur bleu foncé : Excellent contraste
- ✅ Blanc sur rose vif : Bon contraste
- ❌ Gris clair sur blanc : Mauvais contraste

#### Taille

| Taille | Usage | Exemple |
|--------|-------|---------|
| **Grande** | CTA principal, conversion | "Réservez votre séance" |
| **Moyenne** | CTA secondaire | "En savoir plus" |
| **Petite** | CTA tertiaire (footer) | "Contactez-moi" |

!!! tip "💡 Règle d'or"
    Un seul CTA principal (grand) par section de page. Trop de CTA principaux dilue l'attention et réduit les conversions.

#### Forme

| Forme | Style | Personnalité |
|-------|-------|--------------|
| **Arrondie** | Moderne, douce | Coaching, bien-être ✅ |
| **Carrée** | Classique, sérieuse | Juridique, corporate |
| **Pilule (très arrondie)** | Dynamique, jeune | Startups, tech |

**Recommandation pour votre activité :** Arrondie (chaleureux, accueillant)

#### Style de bouton

- **Plein (Solid)** : Bouton avec fond coloré (CTA principal)
- **Contour (Outline)** : Bouton avec bordure uniquement (CTA secondaire)
- **Texte (Link)** : Lien simple souligné (CTA tertiaire)

### Positionner stratégiquement vos CTA

#### Règle des 3 CTA

Placez des CTA à 3 endroits stratégiques :

```
┌─────────────────────────────────────┐
│ 1. HERO (En-tête)                   │
│    └─ CTA immédiat après intro      │
│                                     │
│ 2. MILIEU DE PAGE                   │
│    └─ Après présentation services   │
│                                     │
│ 3. FIN DE PAGE (avant footer)       │
│    └─ Dernière opportunité          │
└─────────────────────────────────────┘
```

**Pourquoi 3 CTA ?**

- **CTA 1 (Haut)** : Pour les visiteurs qui décident rapidement
- **CTA 2 (Milieu)** : Pour ceux qui ont besoin d'être convaincus
- **CTA 3 (Bas)** : Pour ceux qui lisent tout avant d'agir

!!! info "ℹ️ Statistiques de conversion"
    En moyenne, 20% des visiteurs cliquent sur le premier CTA, 35% sur le deuxième (après avoir été convaincus), et 25% sur le dernier. Sans ces 3 CTA, vous perdriez 60% de conversions potentielles.

#### Déplacer un CTA

1. Cliquez sur le bouton
2. Icône **déplacer** ⋮⋮ en haut du bloc
3. Glissez-déposez à la nouvelle position
4. Enregistrez

---

## 📅 Intégration Calendly

### Qu'est-ce que Calendly ?

**Calendly** est un outil de prise de rendez-vous en ligne qui :

- Affiche vos disponibilités automatiquement
- Permet aux clients de réserver sans échange d'emails
- Envoie des confirmations et rappels automatiques
- Se synchronise avec votre agenda (Google Calendar, Outlook, etc.)

### Votre lien Calendly

**Structure du lien Calendly :**

```
https://calendly.com/[votre-nom]/[type-de-seance]
```

**Exemple :**

```
https://calendly.com/armelle-bodenes/seance-decouverte-30min
```

!!! danger "🚨 Important"
    Ce lien est unique et configuré dans votre compte Calendly. Ne le modifiez pas dans Systeme.io sans avoir vérifié qu'il fonctionne. Un lien incorrect = zéro réservation.

### Vérifier et modifier le lien Calendly d'un CTA

#### Procédure

1. Cliquez sur le bouton CTA
2. Dans le panneau de droite, section **"Action"**
3. Vérifiez le champ **"URL"** :

```
┌──────────────────────────────────┐
│ Action                           │
│ ├─ Type: [Lien externe ▼]      │
│ └─ URL:                         │
│    [https://calendly.com/...  ] │
│                                  │
│ Paramètres                       │
│ ├─ Ouvrir dans: [Pop-up ▼]    │
│ └─ Tracking: [Activer ☑]      │
└──────────────────────────────────┘
```

#### Modifier le lien Calendly

1. Copiez votre nouveau lien Calendly depuis votre compte Calendly
2. Collez-le dans le champ **"URL"**
3. Vérifiez que le lien commence par `https://calendly.com/`
4. **Enregistrez**

### Tester le lien Calendly

**Avant de publier :**

1. Cliquez sur **[Aperçu]**
2. Cliquez sur le bouton CTA
3. Vérifiez que :
    - ✅ Le pop-up Calendly s'ouvre
    - ✅ Vos créneaux de disponibilité s'affichent
    - ✅ Le formulaire de réservation fonctionne
    - ✅ Le bon type de rendez-vous est proposé

**Test complet (recommandé) :**

1. Effectuez une réservation test avec votre propre email
2. Vérifiez la réception de l'email de confirmation
3. Annulez le rendez-vous test depuis l'email reçu

!!! tip "💡 Astuce pro"
    Faites ce test complet au moins une fois par mois pour vous assurer que tout fonctionne. Un système de réservation cassé peut vous faire perdre des clients sans que vous le sachiez.

### Ouvrir Calendly en Pop-up vs Nouvel onglet

#### Pop-up (Recommandé ✅)

```
Type: Lien externe
Ouvrir dans: Pop-up / Modal
```

| Avantages | Inconvénients |
|-----------|---------------|
| ✅ Visiteur reste sur votre page | ❌ Peut être bloqué par certains navigateurs (rare) |
| ✅ Meilleur taux de conversion | |
| ✅ Expérience fluide | |
| ✅ Pas de perte de contexte | |

#### Nouvel onglet

```
Type: Lien externe
Ouvrir dans: Nouvel onglet
```

| Avantages | Inconvénients |
|-----------|---------------|
| ✅ Toujours fonctionnel | ❌ Visiteur quitte votre page |
| ✅ Compatible tous navigateurs | ❌ Risque de ne pas revenir |
| | ❌ Taux de conversion plus faible |

!!! tip "💡 Recommandation"
    Pop-up par défaut. Si vous constatez des problèmes techniques, basculez sur nouvel onglet.

---

## 🎨 Personnalisation avancée Calendly

### Paramètres UTM pour tracking

Ajoutez des paramètres UTM à votre lien Calendly pour suivre d'où viennent vos réservations.

**Lien de base :**

```
https://calendly.com/armelle-bodenes/seance-decouverte
```

**Lien avec UTM :**

```
https://calendly.com/armelle-bodenes/seance-decouverte?utm_source=landing&utm_medium=cta&utm_campaign=essentiel-en-soi
```

#### Structure des paramètres UTM

| Paramètre | Description | Exemple |
|-----------|-------------|---------|
| `utm_source` | Source du trafic | `landing`, `google`, `facebook` |
| `utm_medium` | Média/Canal | `cta`, `email`, `social` |
| `utm_campaign` | Nom de la campagne | `essentiel-en-soi`, `promo-septembre` |

**Comment ajouter les UTM :**

1. Générez votre lien avec UTM sur [Google Campaign URL Builder](https://ga-dev-tools.google/campaign-url-builder/)
2. Copiez le lien complet
3. Collez-le dans le champ URL de votre CTA Systeme.io

### Pré-remplir des informations

Calendly permet de pré-remplir certains champs via l'URL.

**Exemple : Pré-remplir le nom et email**

```
https://calendly.com/armelle-bodenes/seance-decouverte?name=Marie%20Dupont&email=marie@example.com
```

**Paramètres disponibles :**

- `name` : Nom complet
- `email` : Adresse email
- `a1` : Réponse à la question personnalisée 1
- `guests` : Ajouter des invités (emails séparés par des virgules)

!!! info "ℹ️ Usage pratique"
    Utile si vous collectez des informations via un formulaire avant d'envoyer vers Calendly. Cela simplifie l'expérience utilisateur.

### Personnaliser l'apparence du widget Calendly

Dans votre compte Calendly (pas Systeme.io) :

1. Allez dans **Settings** > **Appearance**
2. Personnalisez :
    - **Couleur principale** : Doit correspondre à votre charte graphique
    - **Logo** : Ajoutez votre logo en en-tête
    - **Texte de confirmation** : Message après réservation

**Correspondance visuelle :**

| Élément | Votre charte | Calendly à configurer |
|---------|--------------|----------------------|
| Couleur principale | #4A90E2 (exemple) | Primary color |
| Police | Montserrat | Font family (si disponible) |
| Logo | Logo-essentiel-en-soi.png | Upload logo |

---

## 🔧 Créer différents types de CTA

### CTA Texte (lien simple)

Pour un CTA discret dans un paragraphe :

**Exemple :** "Besoin d'en discuter ? [Réservez votre séance découverte gratuite](#calendly)"

#### Procédure

1. Sélectionnez le texte dans votre paragraphe
2. Cliquez sur l'icône **lien** 🔗
3. Collez votre URL Calendly
4. Cochez **"Ouvrir dans un nouvel onglet"** (optionnel)
5. Validez

**Style du lien :**

- Couleur : Accent (couleur CTA)
- Soulignement : Oui (pour visibilité)
- Gras : Optionnel

### CTA Image cliquable

Transformer une image en CTA.

**Exemple :** Image "Réservez maintenant" cliquable

#### Procédure

1. Cliquez sur l'image
2. Dans le panneau de propriétés, section **"Lien"**
3. Collez votre URL Calendly
4. Paramètres :
    - **Ouvrir dans** : Pop-up
    - **Alt text** : "Réserver une séance découverte gratuite"
5. Enregistrez

!!! tip "💡 Usage recommandé"
    Parfait pour les bannières promotionnelles ou visuels call-to-action graphiques. Attention : l'image doit clairement indiquer qu'elle est cliquable.

### CTA flottant (Sticky button)

Bouton qui reste visible lors du scroll (avancé).

**Concept :**

```
┌─────────────────────────────────────┐
│ Contenu de la page                  │
│                                     │
│                  [Réserver]  ←─ Flottant │
│                                     │
│ Plus de contenu...                  │
│                                     │
│                  [Réserver]  ←─ Toujours visible │
└─────────────────────────────────────┘
```

#### Configuration dans Systeme.io

1. Créez un bouton CTA classique
2. Dans les propriétés, section **"Avancé"**
3. Cherchez **"Position"** ou **"Sticky"**
4. Activez **"Sticky Bottom"** (en bas de l'écran)

!!! warning "⚠️ Fonctionnalité avancée"
    Si cette option n'est pas disponible nativement dans Systeme.io, cette fonctionnalité nécessite du code personnalisé. Contactez votre développeur si besoin.

---

## 📈 Optimiser les conversions de vos CTA

### Principes de persuasion

#### Principe de rareté

"Places limitées ce mois-ci" → Crée l'urgence

#### Principe de gratuité

"Séance découverte 100% gratuite" → Lève l'objection du coût

#### Principe de preuve sociale

Placez CTA après les témoignages → Rassure et pousse à l'action

#### Principe de spécificité

"30 minutes d'échange confidentiel" → Concret, rassurant

### A/B Testing des CTA (Test comparatif)

**Qu'est-ce que l'A/B Testing ?**

Tester 2 versions d'un CTA pour voir laquelle convertit le mieux.

**Exemple de test :**

| Version A | Version B |
|-----------|-----------|
| "Réservez votre séance gratuite" | "Je réserve ma séance découverte" |
| Couleur : Bleu | Couleur : Rose |
| Taille : Grande | Taille : Grande |

**Comment tester :**

1. **Semaine 1** : Version A en ligne
    - Notez le nombre de clics (dans Systeme.io Analytics)
2. **Semaine 2** : Version B en ligne
    - Notez le nombre de clics
3. **Comparez** : Quelle version a le meilleur taux de clic ?
4. **Gardez la gagnante** définitivement

!!! warning "⚠️ Important"
    Ne testez qu'un seul élément à la fois (texte OU couleur, pas les deux). Sinon, vous ne saurez pas quel changement a amélioré les résultats.

### Heatmap (Carte de chaleur) - Avancé

**Qu'est-ce qu'une heatmap ?**

Visualisation graphique des zones cliquées par les visiteurs.

**Outils recommandés :**

- **Hotjar** (gratuit jusqu'à 35 sessions/jour)
- **Microsoft Clarity** (gratuit, illimité)
- **Lucky Orange**

**Comment installer :**

1. Créez un compte sur l'outil choisi
2. Copiez le code de tracking
3. Dans Systeme.io :
    - Allez dans **Settings** > **Tracking Code**
    - Collez le code dans **"Custom HTML"**
    - Enregistrez
4. Attendez 7 jours de collecte de données
5. Analysez la heatmap

**Analyse :**

- ✅ Zones chaudes (rouge) : CTA bien placés
- ❌ Zones froides (bleu) : CTA mal placés ou peu visibles

---

## 🆘 Questions fréquentes et dépannage

### Le lien Calendly ne s'ouvre pas

**Causes possibles :**

1. Lien incorrect (typo, espace)
2. Bloqueur de pop-up actif
3. Compte Calendly désactivé

**Solutions :**

**1. Vérifier le lien :**

- Copier le lien depuis le CTA
- Le coller dans un nouvel onglet
- S'il ne fonctionne pas, le lien est incorrect

**2. Désactiver le bloqueur de pop-up :**

- Dans Chrome : icône 🚫 dans la barre d'adresse
- Cliquez > "Toujours autoriser les pop-ups"

**3. Vérifier votre compte Calendly :**

- Connectez-vous à calendly.com
- Vérifiez que votre lien d'événement est actif

### Le bouton CTA n'est pas cliquable

**Causes possibles :**

1. Aucun lien configuré
2. Bloc désactivé
3. Calque superposé (élément devant le bouton)

**Solutions :**

**1. Vérifier l'URL :**

- Cliquez sur le bouton
- Panneau de droite > Section Action
- L'URL doit être remplie

**2. Vérifier la visibilité :**

- Propriétés > Visibilité
- Doit être sur "Visible"

**3. Ordre des calques :**

- Le bouton doit être au premier plan
- Propriétés > Ordre > Mettre au premier plan

### Calendly affiche le mauvais créneau/service

**Cause :** Le lien pointe vers un événement Calendly différent.

**Solution :**

1. Connectez-vous à votre compte Calendly
2. Accédez à l'événement souhaité (ex: "Séance découverte 30 min")
3. Copiez le lien public
4. Remplacez dans Systeme.io

!!! tip "💡 Astuce"
    Vérifiez l'URL, elle doit contenir le nom de l'événement :
    ```
    https://calendly.com/armelle-bodenes/seance-decouverte-30min
                                         ↑ Nom de l'événement
    ```

### Les réservations n'arrivent pas dans mon agenda

**Cause :** Calendly n'est pas synchronisé avec votre agenda Google/Outlook.

**Solution :**

1. Allez sur calendly.com
2. **Account** > **Calendar Connections**
3. Connectez votre Google Calendar ou Outlook
4. Autorisez l'accès
5. Sélectionnez le calendrier à synchroniser

---

## ✅ Checklist de validation

Avant de publier votre page, assurez-vous d'avoir :

### Vérifications techniques

- [ ] Tous les liens Calendly sont fonctionnels
- [ ] Pop-up Calendly s'ouvre correctement
- [ ] Créneaux de disponibilité s'affichent
- [ ] Formulaire de réservation fonctionne
- [ ] Emails de confirmation sont envoyés
- [ ] Test de réservation effectué et annulé

### Vérifications design

- [ ] CTA principal bien visible (contraste, taille)
- [ ] Au minimum 3 CTA sur la page (haut, milieu, bas)
- [ ] Texte des CTA clair et actionnable
- [ ] Style des boutons cohérent
- [ ] CTA responsive (testés sur mobile)
- [ ] Couleurs respectent le contraste minimum (4.5:1)

### Vérifications copy (texte)

- [ ] Verbes d'action utilisés ("Réserver", "Découvrir")
- [ ] Bénéfices mis en avant ("Gratuit", "30 min")
- [ ] 1ère personne privilégiée ("Je réserve")
- [ ] Aucune ambiguïté sur l'action
- [ ] Sous-texte ajouté si pertinent

### Optimisation conversion

- [ ] CTA placés après sections persuasives (témoignages)
- [ ] Urgence ou rareté mentionnée (si applicable)
- [ ] Proposition de valeur claire
- [ ] Sans engagement explicité
- [ ] CTA après chaque section importante

!!! success "🎉 Félicitations !"
    Vos CTA sont maintenant optimisés pour maximiser vos conversions ! Un bon CTA peut multiplier vos réservations par 2 ou 3.

---

## 📤 Partager ce guide

<div class="share-buttons">
  <span class="share-buttons-title">Partager ce guide</span>
  <a href="https://twitter.com/intent/tweet?url=https://mehdisback.github.io/formation-systemio/03-GESTION-CTA-CALENDLY/&text=Formation%20Systeme.io%20-%20Gestion des CTA et Calendly" class="share-button twitter" target="_blank" rel="noopener noreferrer">
    🐦 Twitter
  </a>
  <a href="https://www.facebook.com/sharer/sharer.php?u=https://mehdisback.github.io/formation-systemio/03-GESTION-CTA-CALENDLY/" class="share-button facebook" target="_blank" rel="noopener noreferrer">
    📘 Facebook
  </a>
  <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://mehdisback.github.io/formation-systemio/03-GESTION-CTA-CALENDLY/" class="share-button linkedin" target="_blank" rel="noopener noreferrer">
    💼 LinkedIn
  </a>
  <a href="mailto:?subject=Formation%20Systeme.io%20-%20Gestion des CTA et Calendly&body=Je%20partage%20avec%20toi%20ce%20guide%20:%20https://mehdisback.github.io/formation-systemio/03-GESTION-CTA-CALENDLY/" class="share-button email">
    ✉️ Email
  </a>
</div>

---

## 🔗 Navigation

- ⬅️ **Précédent** : [02 - Modification du contenu](02-MODIFICATION-CONTENU.md)
- ➡️ **Suivant** : [04 - Design et mise en page](04-DESIGN-MISE-EN-PAGE.md)
- 🏠 **Accueil** : [Retour à l'accueil](index.md)

---

## 📚 Ressources complémentaires

### Outils de création de liens UTM

- [Google Campaign URL Builder](https://ga-dev-tools.google/campaign-url-builder/)

### Outils de tracking et heatmap

- [Microsoft Clarity](https://clarity.microsoft.com) (gratuit, recommandé)
- [Hotjar](https://www.hotjar.com) (freemium)

### Documentation Calendly

- [Centre d'aide Calendly](https://help.calendly.com)
- [Paramètres d'URL Calendly](https://help.calendly.com/hc/en-us/articles/360054920714)

---

**Prêt à continuer ? Passez au [Guide 04 - Design et mise en page](04-DESIGN-MISE-EN-PAGE.md) !** 🎨
