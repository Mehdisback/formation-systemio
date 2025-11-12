# 📝 05 - Formulaires et données

⏱️ **Durée estimée** : 50 minutes
📊 **Niveau** : Intermédiaire

## 🎯 Objectifs

À la fin de ce guide, vous saurez :

- [ ] Créer et configurer des formulaires de contact
- [ ] Gérer le consentement RGPD et la conformité légale
- [ ] Configurer les notifications et emails automatiques
- [ ] Exporter et segmenter vos contacts
- [ ] Synchroniser avec des outils externes (CRM, Google Sheets)
- [ ] Respecter les droits des utilisateurs sur leurs données

---

## 📋 Types de formulaires sur votre page

### Formulaires disponibles

Votre tunnel utilise principalement **Calendly** pour la collecte d'informations. Mais Systeme.io permet d'ajouter des formulaires complémentaires :

| Type | Usage | Exemple |
|------|-------|---------|
| **Contact simple** | Email uniquement | Newsletter, téléchargement |
| **Contact complet** | Nom, email, téléphone, message | Demande d'information |
| **Lead magnet** | Email contre ressource gratuite | Guide PDF, checklist |
| **Questionnaire** | Qualification prospect | Besoin spécifique, budget |

### Calendly comme formulaire principal

**Avantages :**

- ✅ Collecte nom, email, téléphone automatiquement
- ✅ Réservation directe dans l'agenda
- ✅ Confirmations et rappels automatiques
- ✅ Questions personnalisées possibles

**Limites :**

- ❌ Nécessite une réservation de créneau
- ❌ Pas adapté pour simple collecte d'email

!!! info "ℹ️ Quand utiliser un formulaire Systeme.io"
    Utilisez un formulaire classique quand vous voulez collecter des emails **sans** imposer une réservation immédiate. Par exemple : newsletter, téléchargement de guide gratuit, demande d'information préalable.

---

## ➕ Ajouter un formulaire Systeme.io

### Créer un nouveau formulaire

**Procédure :**

1. Dans l'éditeur, cliquez sur **"+"** (Ajouter un bloc)
2. Cherchez **"Formulaire"** ou **"Form"**
3. Sélectionnez un modèle :
    - Simple (email seulement)
    - Standard (nom + email)
    - Complet (tous champs)
4. Le formulaire s'insère dans la page

### Configurer les champs du formulaire

**Champs disponibles :**

| Champ | Type | Requis | Usage |
|-------|------|--------|-------|
| **Prénom** | Texte court | Optionnel | Personnalisation |
| **Nom** | Texte court | Optionnel | Identification |
| **Email** | Email | **Obligatoire** | Contact principal |
| **Téléphone** | Téléphone | Optionnel | Contact rapide |
| **Message** | Texte long | Optionnel | Demande spécifique |
| **Case à cocher** | Checkbox | RGPD | Consentement |

**Modifier les champs :**

1. Cliquez sur le formulaire
2. Panneau de droite > **Champs**
3. Pour chaque champ :

```
┌────────────────────────────┐
│ Email                     │
│ ├─ Label: [Votre email]  │
│ ├─ Placeholder: [ex: ...] │
│ ├─ Requis: [✓]           │
│ └─ Validation: [Email]    │
└────────────────────────────┘
```

!!! tip "💡 Moins de champs = Plus de conversions"
    Chaque champ supplémentaire réduit le taux de conversion de 10-15%. Limitez-vous à 3-4 champs maximum : Nom, Email, Message suffisent dans 90% des cas.

### Ajouter/Supprimer un champ

**Ajouter :**

1. Formulaire sélectionné > **"Ajouter un champ"**
2. Choisir le type
3. Configurer les propriétés

**Supprimer :**

1. Cliquer sur le champ à supprimer
2. Icône corbeille 🗑️

---

## ⚖️ Configuration RGPD et consentement

### Obligations légales (France/Europe)

**RGPD (Règlement Général sur la Protection des Données) impose :**

- ✅ Consentement explicite et éclairé
- ✅ Information claire sur l'usage des données
- ✅ Possibilité de se désinscrire facilement
- ✅ Sécurisation des données

!!! danger "🚨 RGPD obligatoire"
    Le non-respect du RGPD peut entraîner des amendes jusqu'à **20 millions d'euros ou 4% du chiffre d'affaires**. Ce n'est pas optionnel : chaque formulaire DOIT avoir une case de consentement.

### Case de consentement obligatoire

**Ajoutez systématiquement :**

```
☐ J'accepte de recevoir des informations de [Votre nom]
  et j'ai pris connaissance de la politique de confidentialité.
```

**Configuration :**

1. Ajoutez un champ **Checkbox**
2. Texte : Votre phrase de consentement + lien vers politique
3. **Requis : OUI** (obligatoire pour soumettre)

**Lien vers politique de confidentialité :**

```markdown
[politique de confidentialité](https://votre-site.com/confidentialite)
```

### Texte de consentement recommandé

```
En soumettant ce formulaire, j'accepte que mes données soient
utilisées pour me recontacter dans le cadre de ma demande.
Conformément au RGPD, je dispose d'un droit d'accès, de
rectification et de suppression de mes données.
```

!!! tip "💡 Soyez transparent"
    Plus votre texte de consentement est clair et honnête, plus les visiteurs auront confiance. Ne cachez rien : expliquez exactement ce que vous allez faire de leurs données.

---

## 📧 Actions après soumission du formulaire

### Configuration de la redirection

**Après soumission, le visiteur peut :**

| Action | Configuration | Usage |
|--------|---------------|-------|
| **Message de remerciement** | Afficher un message | Simple, rapide |
| **Page de remerciement** | Redirection URL | Tracking, upsell |
| **Téléchargement** | Lien vers fichier | Lead magnet |
| **Calendly** | Ouvrir widget | Prendre RDV après |

**Paramétrer la redirection :**

1. Formulaire sélectionné > **Actions**
2. **Après soumission** > Choisir l'action
3. Si redirection :

```
URL: [https://...page-merci]
Délai: [Immédiat / 3 secondes]
```

### Page de remerciement

**Éléments à inclure :**

```
┌─────────────────────────────────────┐
│ ✓ Merci [Prénom] !                 │
│                                     │
│ Votre demande a bien été reçue.    │
│ Je vous recontacte sous 24-48h.    │
│                                     │
│ En attendant :                      │
│ - [Téléchargez votre guide]        │
│ - [Réservez votre séance gratuite] │
│ - [Suivez-moi sur LinkedIn]        │
└─────────────────────────────────────┘
```

!!! tip "💡 Profitez de la page de remerciement"
    C'est le moment où le visiteur est le plus engagé ! Proposez-lui une action complémentaire : téléchargement, réservation, suivi sur les réseaux sociaux.

---

## 🔔 Notifications et emails automatiques

### Notification pour vous (administrateur)

**Recevoir un email à chaque soumission :**

1. Systeme.io Dashboard > **Emails** > **Automation**
2. Créer une automatisation :

```
Déclencheur: Formulaire soumis
Action: Envoyer email à [votre-email@example.com]
```

**Contenu de l'email notification :**

```
Sujet: Nouvelle demande de contact - L'Essentiel en Soi

Bonjour Armelle,

Vous avez reçu une nouvelle demande :

Prénom: {FIRST_NAME}
Nom: {LAST_NAME}
Email: {EMAIL}
Téléphone: {PHONE}
Message: {MESSAGE}

Rendez-vous sur Systeme.io pour répondre.
```

### Email de confirmation automatique

**Envoyer un email au visiteur après soumission :**

```
Sujet: Merci pour votre message, [Prénom]

Bonjour [Prénom],

Merci de votre intérêt pour L'Essentiel en Soi.

J'ai bien reçu votre demande et je vous recontacterai
sous 24-48h pour échanger sur votre situation.

En attendant, n'hésitez pas à réserver directement
votre séance découverte gratuite :
[Réserver maintenant]

À très bientôt,
Armelle Bodénès
```

**Configuration :**

1. Automation > **Ajouter une action**
2. **Envoyer email** > Destinataire : Contact
3. Rédigez le contenu
4. Variables disponibles :
    - `{FIRST_NAME}` - Prénom
    - `{LAST_NAME}` - Nom
    - `{EMAIL}` - Email
    - `{PHONE}` - Téléphone
    - `{MESSAGE}` - Message du formulaire

!!! warning "⚠️ Testez vos emails"
    Envoyez-vous toujours un email de test avant d'activer l'automatisation. Vérifiez que les variables s'affichent correctement et que le lien de désinscription fonctionne.

---

## 📊 Gérer et exporter les contacts

### Accéder à la base de contacts

1. Dashboard Systeme.io
2. Menu **"Contacts"** 👥
3. Tous les contacts collectés s'affichent

**Vue d'ensemble :**

```
┌─────────────────────────────────────────────────┐
│ CONTACTS                                        │
├──────────┬────────────┬──────────┬──────────────┤
│ Nom      │ Email      │ Source   │ Date         │
├──────────┼────────────┼──────────┼──────────────┤
│ Marie D. │ marie@...  │ Form #1  │ 10/11/2025   │
│ Pierre L.│ pierre@... │ Calendly │ 09/11/2025   │
│ ...      │ ...        │ ...      │ ...          │
└──────────┴────────────┴──────────┴──────────────┘
```

### Filtrer les contacts

**Filtres disponibles :**

| Filtre | Usage |
|--------|-------|
| **Date** | Contacts reçus cette semaine/mois |
| **Source** | Provenance (form, Calendly, etc.) |
| **Tags** | Catégories personnalisées |
| **Statut** | Actif, désabonné |

### Exporter les contacts

**Format Excel/CSV pour traitement :**

1. Page Contacts > Bouton **"Exporter"**
2. Choisir le format :
    - **CSV** : Compatible Excel, Google Sheets
    - **Excel** : Fichier .xlsx direct
3. Sélectionner les champs à exporter
4. Cliquez **"Télécharger"**

**Fichier exporté contient :**

- Nom, Prénom
- Email, Téléphone
- Date d'inscription
- Source
- Tags éventuels

!!! tip "💡 Exportez régulièrement"
    Prenez l'habitude d'exporter votre base de contacts tous les mois. C'est une sauvegarde de sécurité et ça vous permet d'analyser l'évolution dans Excel.

### Synchronisation avec CRM externe

**Intégrations possibles :**

| CRM | Méthode | Difficulté |
|-----|---------|------------|
| **Google Sheets** | Zapier / Make | ⭐ Facile |
| **HubSpot** | API / Zapier | ⭐⭐ Moyen |
| **Pipedrive** | API / Zapier | ⭐⭐ Moyen |
| **Mailchimp** | Intégration native | ⭐ Facile |

**Avec Zapier (recommandé) :**

1. Créez un compte sur [zapier.com](https://zapier.com)
2. Créez un "Zap" :
    - **Trigger** : Systeme.io - New Contact
    - **Action** : Google Sheets - Add Row
3. Configurez les champs à synchroniser
4. Activez le Zap

---

## 🏷️ Tags et segmentation

### Pourquoi segmenter ?

**Avantages :**

- ✅ Emails ciblés selon l'intérêt
- ✅ Suivi personnalisé
- ✅ Offres adaptées au profil
- ✅ Meilleur taux de conversion (+40% en moyenne)

### Créer des tags

**Exemples de tags pertinents :**

| Tag | Signification | Usage |
|-----|---------------|-------|
| `#accompagnement-juridique` | Intéressé par accompagnement juridique | Email ciblé sur ce service |
| `#essentiel-en-soi` | Intéressé par coaching personnel | Email sur bien-être |
| `#lead-chaud` | Très intéressé, répondu rapidement | Relance prioritaire |
| `#seance-decouverte-faite` | A déjà eu une séance | Proposition forfait |

**Appliquer un tag automatiquement :**

1. Formulaire > **Actions après soumission**
2. **Ajouter un tag** > Créer ou sélectionner
3. Le tag s'applique à tous les contacts de ce formulaire

!!! tip "💡 Stratégie de tags"
    Créez des tags basés sur le **comportement** (a téléchargé, a réservé) et l'**intérêt** (juridique, bien-être). Évitez de créer trop de tags : 5-10 tags bien pensés suffisent.

### Segmentation avancée

**Créer une liste de contacts ciblée :**

1. Contacts > **Filtres**
2. Combinez plusieurs critères :
    - Tag = `#accompagnement-juridique`
    - Date > Derniers 30 jours
    - Statut = Actif
3. Enregistrez le filtre > **"Liste personnalisée"**

---

## 🔒 Respect de la vie privée

### Droits des utilisateurs (RGPD)

**Les visiteurs ont le droit de :**

| Droit | Description |
|-------|-------------|
| **Accès** | Voir leurs données collectées |
| **Rectification** | Corriger leurs données |
| **Suppression** | Supprimer leurs données ("droit à l'oubli") |
| **Portabilité** | Recevoir leurs données dans un format lisible |
| **Opposition** | Refuser l'usage de leurs données |

### Gérer les demandes RGPD

**Un contact demande la suppression de ses données :**

1. Contacts > Rechercher l'email
2. Cliquez sur le contact
3. Bouton **"Supprimer"** (icône corbeille)
4. Confirmez la suppression

!!! danger "🚨 Suppression définitive"
    La suppression est irréversible. Assurez-vous que c'est bien la demande du contact avant de valider. Conservez une trace écrite de la demande (email) pendant 1 an.

### Politique de confidentialité

**Éléments obligatoires :**

```markdown
# Politique de Confidentialité

## Données collectées
- Nom, prénom, email, téléphone via formulaires
- Données de navigation (cookies)

## Usage des données
- Répondre à vos demandes
- Envoi d'informations sur nos services
- Amélioration de nos services

## Durée de conservation
- 3 ans après dernier contact

## Vos droits
- Accès, rectification, suppression
- Contact : [votre-email]

## Hébergement
- Systeme.io (serveurs UE)
```

**Lien vers la politique :**

Ajoutez le lien dans :

- Footer de la page
- Formulaires (case de consentement)
- Emails automatiques

!!! info "ℹ️ Modèles gratuits"
    Vous pouvez utiliser des générateurs gratuits de politique de confidentialité comme [Privacy Policy Generator](https://www.privacypolicygenerator.info/). Adaptez ensuite le texte à votre activité.

---

## 💡 Bonnes pratiques

### Optimiser le taux de conversion

**Règles d'or :**

- ✅ **Minimum de champs** : 3 champs maximum (nom, email, message)
- ✅ **Valeur proposée** : "Recevez votre guide gratuit"
- ✅ **Urgence douce** : "Offre limitée" (si vrai)
- ✅ **Réassurance** : "Sans engagement", "Réponse sous 24h"
- ❌ **Éviter** : Trop de champs, jargon, design négligé

### Tests A/B

**Éléments à tester :**

| Élément | Version A | Version B |
|---------|-----------|-----------|
| **Titre** | "Contactez-moi" | "Réservez votre séance gratuite" |
| **Champs** | 5 champs | 3 champs |
| **Bouton** | "Envoyer" | "Je réserve maintenant" |
| **Couleur CTA** | Bleu | Rose |

**Durée de test :** 2 semaines minimum par variante

!!! warning "⚠️ Testez un élément à la fois"
    Si vous changez le titre ET le nombre de champs ET la couleur en même temps, vous ne saurez pas quel changement a amélioré (ou dégradé) les résultats.

---

## 🆘 Questions fréquentes et dépannage

### Le formulaire ne s'envoie pas

**Causes possibles :**

1. Champs obligatoires non remplis
2. Format email invalide
3. Case RGPD non cochée
4. Problème de connexion internet

**Solutions :**

1. Vérifiez que tous les champs marqués (*) sont remplis
2. Vérifiez le format de l'email (doit contenir @)
3. Assurez-vous que la case de consentement est cochée
4. Testez avec un autre navigateur ou appareil

### Je ne reçois pas les notifications

**Cause :** Configuration incorrecte ou emails en spam.

**Solutions :**

1. Vérifiez votre adresse email dans **Paramètres** > **Notifications**
2. Regardez dans vos **spams/courrier indésirable**
3. Ajoutez l'adresse d'envoi Systeme.io à vos contacts
4. Testez avec une soumission de formulaire

### Impossible d'exporter les contacts

**Cause :** Fonctionnalité limitée selon votre plan Systeme.io.

**Solutions :**

1. Vérifiez votre abonnement (certains plans limitent l'export)
2. Essayez d'exporter moins de contacts à la fois
3. Contactez le support Systeme.io si le problème persiste

### Un contact veut se désinscrire

**Procédure obligatoire :**

1. Chaque email automatique doit contenir un **lien de désinscription** en bas
2. Le lien doit fonctionner en 1 clic (pas de connexion requise)
3. Une fois désabonné, le contact ne reçoit plus d'emails
4. Conservez la trace du désabonnement

---

## ✅ Checklist de validation

Avant de mettre votre formulaire en ligne, assurez-vous d'avoir :

### Configuration

- [ ] Champs pertinents uniquement (3-5 max)
- [ ] Email toujours en champ obligatoire
- [ ] Case RGPD avec lien vers politique de confidentialité
- [ ] Bouton de soumission clair ("Envoyer ma demande")
- [ ] Message de validation ou redirection configuré
- [ ] Tags appliqués automatiquement (si segmentation)

### Design

- [ ] Formulaire bien visible (contraste suffisant)
- [ ] Labels clairs au-dessus des champs
- [ ] Placeholders informatifs dans les champs
- [ ] Responsive (testé sur mobile)
- [ ] Champs assez grands pour le tactile (min 44px hauteur)
- [ ] Cohérence visuelle avec le reste de la page

### Automatisations

- [ ] Notification admin configurée et testée
- [ ] Email de confirmation au contact
- [ ] Variables personnalisées fonctionnelles ({FIRST_NAME}, etc.)
- [ ] Lien de désinscription présent dans les emails
- [ ] Redirection après soumission paramétrée

### RGPD et légal

- [ ] Politique de confidentialité rédigée et accessible
- [ ] Consentement explicite requis
- [ ] Possibilité de désinscription visible
- [ ] Procédure de suppression des données documentée
- [ ] Durée de conservation définie (max 3 ans)

!!! success "🎉 Félicitations !"
    Votre système de collecte de données est maintenant conforme, automatisé et optimisé. Un bon formulaire peut multiplier vos contacts par 3 !

---

## 🔗 Navigation

- ⬅️ **Précédent** : [04 - Design et mise en page](04-DESIGN-MISE-EN-PAGE.md)
- ➡️ **Suivant** : [06 - SEO et référencement](06-SEO-REFERENCEMENT.md)
- 🏠 **Accueil** : [Retour à l'accueil](index.md)

---

## 📚 Ressources complémentaires

### Outils d'automatisation

- [Zapier](https://zapier.com) - Automatisation sans code
- [Make (ex-Integromat)](https://www.make.com) - Alternative à Zapier
- [IFTTT](https://ifttt.com) - Automatisations simples

### RGPD et conformité

- [CNIL - Guide RGPD](https://www.cnil.fr/fr/rgpd-de-quoi-parle-t-on) - Référence officielle
- [Privacy Policy Generator](https://www.privacypolicygenerator.info/) - Générateur gratuit
- [GDPR.eu](https://gdpr.eu/) - Guide complet en anglais

### Optimisation formulaires

- [Typeform](https://www.typeform.com) - Formulaires conversationnels
- [Google Forms](https://www.google.com/forms/) - Formulaires simples gratuits
- [Formspree](https://formspree.io/) - Backend formulaires

---

**Prêt à continuer ? Passez au [Guide 06 - SEO et référencement](06-SEO-REFERENCEMENT.md) !** 🔍
