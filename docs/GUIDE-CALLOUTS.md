# 🎨 Guide des Callouts (Admonitions)

Les callouts (ou admonitions) sont des blocs colorés qui mettent en valeur des informations importantes. Voici tous les types disponibles avec des exemples concrets pour votre formation.

---

## 📋 Callouts standards

### ✅ Success - Réussites et félicitations

```markdown
!!! success "Bravo !"
    Vous avez réussi à modifier votre premier CTA ! Votre landing page est maintenant personnalisée.
```

!!! success "Bravo !"
    Vous avez réussi à modifier votre premier CTA ! Votre landing page est maintenant personnalisée.

---

### 💡 Tip - Conseils pratiques

```markdown
!!! tip "Astuce pro"
    Pour gagner du temps, dupliquez votre section existante avant de la modifier. Ainsi, vous gardez toujours une sauvegarde.
```

!!! tip "Astuce pro"
    Pour gagner du temps, dupliquez votre section existante avant de la modifier. Ainsi, vous gardez toujours une sauvegarde.

---

### ⚠️ Warning - Attention importante

```markdown
!!! warning "Attention !"
    Ne supprimez jamais votre lien Calendly sans en avoir créé un nouveau. Vos clientes ne pourraient plus prendre rendez-vous.
```

!!! warning "Attention !"
    Ne supprimez jamais votre lien Calendly sans en avoir créé un nouveau. Vos clientes ne pourraient plus prendre rendez-vous.

---

### 🚨 Danger - Erreurs critiques

```markdown
!!! danger "Erreur à éviter absolument"
    Ne modifiez JAMAIS le code HTML si vous n'êtes pas à l'aise. Une erreur peut casser toute votre page.
```

!!! danger "Erreur à éviter absolument"
    Ne modifiez JAMAIS le code HTML si vous n'êtes pas à l'aise. Une erreur peut casser toute votre page.

---

### ℹ️ Info - Informations complémentaires

```markdown
!!! info "Bon à savoir"
    Systeme.io sauvegarde automatiquement vos modifications toutes les 30 secondes.
```

!!! info "Bon à savoir"
    Systeme.io sauvegarde automatiquement vos modifications toutes les 30 secondes.

---

### 📝 Note - Notes générales

```markdown
!!! note "Rappel"
    Cette formation est optimisée pour Systeme.io version 2024. Certaines interfaces peuvent légèrement différer.
```

!!! note "Rappel"
    Cette formation est optimisée pour Systeme.io version 2024. Certaines interfaces peuvent légèrement différer.

---

## 🎯 Callouts avancés

### ✏️ Example - Exercices pratiques

```markdown
!!! example "Exercice : Modifier votre titre principal"
    **Objectif** : Changer le titre H1 de votre landing page

    **Étapes :**

    1. Cliquez sur le titre existant
    2. Tapez votre nouveau titre (ex: "Découvrez votre profil Ennéagramme")
    3. Cliquez sur "Enregistrer"
    4. Prévisualisez le résultat
```

!!! example "Exercice : Modifier votre titre principal"
    **Objectif** : Changer le titre H1 de votre landing page

    **Étapes :**

    1. Cliquez sur le titre existant
    2. Tapez votre nouveau titre (ex: "Découvrez votre profil Ennéagramme")
    3. Cliquez sur "Enregistrer"
    4. Prévisualisez le résultat

---

### ❓ Question - Quiz et réflexions

```markdown
!!! question "Quiz : Testez vos connaissances"
    Quelle est la différence entre un CTA primaire et un CTA secondaire ?

    **Réponse** : Un CTA primaire incite à l'action principale (ex: prendre RDV), tandis qu'un CTA secondaire propose une action alternative (ex: en savoir plus).
```

!!! question "Quiz : Testez vos connaissances"
    Quelle est la différence entre un CTA primaire et un CTA secondaire ?

    **Réponse** : Un CTA primaire incite à l'action principale (ex: prendre RDV), tandis qu'un CTA secondaire propose une action alternative (ex: en savoir plus).

---

### 💬 Quote - Témoignages et citations

```markdown
!!! quote "Témoignage de Marie, Coach certifiée"
    "Grâce à cette formation, j'ai pu modifier ma landing page en 2h au lieu de faire appel à un prestataire. J'ai économisé 500€ !"
```

!!! quote "Témoignage de Marie, Coach certifiée"
    "Grâce à cette formation, j'ai pu modifier ma landing page en 2h au lieu de faire appel à un prestataire. J'ai économisé 500€ !"

---

### 🐛 Bug - Problèmes connus

```markdown
!!! bug "Problème connu"
    Sur certains navigateurs, le bouton Calendly peut mettre 2-3 secondes à charger. C'est normal, soyez patiente.
```

!!! bug "Problème connu"
    Sur certains navigateurs, le bouton Calendly peut mettre 2-3 secondes à charger. C'est normal, soyez patiente.

---

### 📊 Abstract - Résumés

```markdown
!!! abstract "Résumé du module"
    Dans ce module, vous avez appris à :

    - ✅ Modifier vos titres et textes
    - ✅ Changer vos images
    - ✅ Personnaliser vos CTA
    - ✅ Intégrer Calendly
```

!!! abstract "Résumé du module"
    Dans ce module, vous avez appris à :

    - ✅ Modifier vos titres et textes
    - ✅ Changer vos images
    - ✅ Personnaliser vos CTA
    - ✅ Intégrer Calendly

---

## 🎨 Callouts pliables

Pour créer un callout pliable (fermé par défaut), utilisez `???` au lieu de `!!!` :

```markdown
??? tip "Astuce avancée (cliquez pour déplier)"
    Cette technique est réservée aux utilisateurs confirmées. Si vous êtes débutante, passez cette section.

    Pour optimiser votre SEO, ajoutez des balises alt sur toutes vos images...
```

??? tip "Astuce avancée (cliquez pour déplier)"
    Cette technique est réservée aux utilisateurs confirmées. Si vous êtes débutante, passez cette section.

    Pour optimiser votre SEO, ajoutez des balises alt sur toutes vos images...

---

Pour un callout pliable **ouvert par défaut**, utilisez `???+` :

```markdown
???+ warning "Important : Lisez avant de continuer"
    Ce module nécessite d'avoir terminé les modules 1 et 2. Assurez-vous d'avoir :

    - [ ] Créé votre compte Systeme.io
    - [ ] Connecté votre domaine
    - [ ] Créé votre première page
```

???+ warning "Important : Lisez avant de continuer"
    Ce module nécessite d'avoir terminé les modules 1 et 2. Assurez-vous d'avoir :

    - [ ] Créé votre compte Systeme.io
    - [ ] Connecté votre domaine
    - [ ] Créé votre première page

---

## 🌈 Callouts sans titre

Omettez le titre pour un style plus épuré :

```markdown
!!! success
    Modification enregistrée avec succès !
```

!!! success
    Modification enregistrée avec succès !

---

## 📚 Cas d'usage recommandés

| Callout | Quand l'utiliser | Exemple contexte formation |
|---------|------------------|----------------------------|
| `success` | Validation d'étape | "Bravo, votre CTA est configuré !" |
| `tip` | Conseil pratique | "Utilisez des verbes d'action dans vos CTA" |
| `warning` | Attention importante | "Sauvegardez avant de quitter" |
| `danger` | Erreur critique | "Ne supprimez pas cette section" |
| `info` | Information utile | "Cette fonctionnalité est en version beta" |
| `note` | Rappel | "Pensez à tester sur mobile" |
| `example` | Exercice | "Exercice : Modifier votre image de fond" |
| `question` | Quiz | "Quelle taille d'image recommandée ?" |
| `quote` | Témoignage | "Ce qu'en pensent nos apprenantes" |
| `abstract` | Résumé | "Ce que vous avez appris dans ce module" |

---

## 🎯 Bonnes pratiques

### ✅ À faire

- Utilisez des callouts pour les informations **vraiment** importantes
- Variez les types pour éviter la monotonie
- Gardez les messages **courts et clairs**
- Utilisez un **emoji** dans le titre pour plus de visibilité
- Privilégiez les callouts **pliables** pour les contenus longs

### ❌ À éviter

- Abuser des callouts (maximum 2-3 par page)
- Utiliser uniquement des `warning` ou `danger` (effet alarmiste)
- Mettre trop de texte dans un seul callout
- Utiliser des callouts pour du contenu banal
- Oublier de tester l'affichage mobile

---

## 🚀 Exemples contextuels

### Pour un guide de démarrage

```markdown
!!! tip "Avant de commencer"
    Prévoyez 15 minutes sans interruption pour ce module. Ayez votre ordinateur et votre accès Systeme.io prêts.

!!! example "Exercice pratique"
    Connectez-vous à votre compte Systeme.io et ouvrez votre landing page en mode édition.

!!! success "Checkpoint"
    Vous devriez maintenant voir l'éditeur avec tous vos blocs de contenu visibles.
```

### Pour un guide avancé

```markdown
??? warning "Prérequis"
    Ce module nécessite de maîtriser les bases de Systeme.io. Si c'est votre première utilisation, commencez par le Module 01.

!!! danger "Attention : Manipulation de code"
    Cette section contient du code HTML. Une erreur peut casser votre page. Faites une sauvegarde avant de continuer.

??? tip "Astuce pour développeurs"
    Si vous êtes à l'aise avec le code, vous pouvez directement modifier le CSS pour des ajustements avancés.
```

---

## 📖 Ressources

Pour plus de personnalisation, consultez :

- [Documentation Material Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)
- [Liste complète des types](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#supported-types)
- [Personnalisation CSS](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#customization)
