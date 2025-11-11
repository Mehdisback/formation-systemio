## 🎯 Objectif

Gérer les formulaires, collecter des informations visiteurs, configurer les notifications et exporter les données.

---

## 1. Types de formulaires sur votre page

### 1.1 Formulaires existants

Votre tunnel utilise principalement **Calendly** pour la collecte d'informations. Mais Systeme.io permet d'ajouter des formulaires complémentaires :

|Type|Usage|Exemple|
|---|---|---|
|**Contact simple**|Email uniquement|Newsletter, téléchargement|
|**Contact complet**|Nom, email, téléphone, message|Demande d'information|
|**Lead magnet**|Email contre ressource gratuite|Guide PDF, checklist|
|**Questionnaire**|Qualification prospect|Besoin spécifique, budget|

### 1.2 Calendly comme formulaire principal

**Avantages :**

- ✅ Collecte nom, email, téléphone automatiquement
- ✅ Réservation directe dans l'agenda
- ✅ Confirmations et rappels automatiques
- ✅ Questions personnalisées possibles

**Limites :**

- ❌ Nécessite une réservation de créneau
- ❌ Pas adapté pour simple collecte d'email

---

## 2. Ajouter un formulaire Systeme.io

### 2.1 Créer un nouveau formulaire

**Procédure :**

1. Dans l'éditeur, cliquez sur **"+"** (Ajouter un bloc)
2. Cherchez **"Formulaire"** ou **"Form"**
3. Sélectionnez un modèle :
    - Simple (email seulement)
    - Standard (nom + email)
    - Complet (tous champs)
4. Le formulaire s'insère dans la page

### 2.2 Configurer les champs du formulaire

**Champs disponibles :**

|Champ|Type|Requis|Usage|
|---|---|---|---|
|**Prénom**|Texte court|Optionnel|Personnalisation|
|**Nom**|Texte court|Optionnel|Identification|
|**Email**|Email|**Obligatoire**|Contact principal|
|**Téléphone**|Téléphone|Optionnel|Contact rapide|
|**Message**|Texte long|Optionnel|Demande spécifique|
|**Case à cocher**|Checkbox|RGPD|Consentement|

**Modifier les champs :**

1. Cliquez sur le formulaire
2. Panneau de droite > **Champs**
3. Pour chaque champ :
    
    ```
    ┌────────────────────────────┐│ Email                     ││ ├─ Label: [Votre email]  ││ ├─ Placeholder: [ex: ...] ││ ├─ Requis: [✓]           ││ └─ Validation: [Email]    │└────────────────────────────┘
    ```
    

### 2.3 Ajouter/Supprimer un champ

**Ajouter :**

1. Formulaire sélectionné > **"Ajouter un champ"**
2. Choisir le type
3. Configurer les propriétés

**Supprimer :**

1. Cliquer sur le champ à supprimer
2. Icône corbeille 🗑️

---

## 3. Configuration RGPD et consentement

### 3.1 Obligations légales (France/Europe)

**RGPD (Règlement Général sur la Protection des Données) impose :**

- ✅ Consentement explicite
- ✅ Information claire sur l'usage des données
- ✅ Possibilité de se désinscrire
- ✅ Sécurisation des données

### 3.2 Case de consentement obligatoire

**Ajoutez systématiquement :**

```
☐ J'accepte de recevoir des informations de [Votre nom] 
  et j'ai pris connaissance de la politique de confidentialité.
```

**Configuration :**

1. Ajoutez un champ **Checkbox**
2. Texte : Votre phrase de consentement + lien vers politique
3. **Requis : OUI**

**Lien vers politique de confidentialité :**

```markdown
[politique de confidentialité](https://votre-site.com/confidentialite)
```

### 3.3 Texte de consentement recommandé

```
En soumettant ce formulaire, j'accepte que mes données soient 
utilisées pour me recontacter dans le cadre de ma demande. 
Conformément au RGPD, je dispose d'un droit d'accès, de 
rectification et de suppression de mes données.
```

---

## 4. Actions après soumission du formulaire

### 4.1 Configuration de la redirection

**Après soumission, le visiteur peut :**

|Action|Configuration|Usage|
|---|---|---|
|**Message de remerciement**|Afficher un message|Simple, rapide|
|**Page de remerciement**|Redirection URL|Tracking, upsell|
|**Téléchargement**|Lien vers fichier|Lead magnet|
|**Calendly**|Ouvrir widget|Prendre RDV après|

**Paramétrer la redirection :**

1. Formulaire sélectionné > **Actions**
2. **Après soumission** > Choisir l'action
3. Si redirection :
    
    ```
    URL: [https://...page-merci]Délai: [Immédiat / 3 secondes]
    ```
    

### 4.2 Page de remerciement

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

---

## 5. Notifications et emails automatiques

### 5.1 Notification pour vous (administrateur)

**Recevoir un email à chaque soumission :**

1. Systeme.io Dashboard > **Emails** > **Automation**
2. Créer une automatisation :
    
    ```
    Déclencheur: Formulaire soumisAction: Envoyer email à [votre-email@example.com]
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

### 5.2 Email de confirmation automatique

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
    - `{FIRST_NAME}`
    - `{LAST_NAME}`
    - `{EMAIL}`
    - etc.

---

## 6. Gérer et exporter les contacts

### 6.1 Accéder à la base de contacts

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

### 6.2 Filtrer les contacts

**Filtres disponibles :**

|Filtre|Usage|
|---|---|
|**Date**|Contacts reçus cette semaine/mois|
|**Source**|Provenance (form, Calendly, etc.)|
|**Tags**|Catégories personnalisées|
|**Statut**|Actif, désabonné|

### 6.3 Exporter les contacts

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

### 6.4 Synchronisation avec CRM externe

**Intégrations possibles :**

|CRM|Méthode|Difficulté|
|---|---|---|
|**Google Sheets**|Zapier / Make|⭐ Facile|
|**HubSpot**|API / Zapier|⭐⭐ Moyen|
|**Pipedrive**|API / Zapier|⭐⭐ Moyen|
|**Mailchimp**|Intégration native|⭐ Facile|

**Avec Zapier (recommandé) :**

1. Créez un compte sur zapier.com
2. Créez un "Zap" :
    - **Trigger** : Systeme.io - New Contact
    - **Action** : Google Sheets - Add Row
3. Configurez les champs à synchroniser
4. Activez le Zap

---

## 7. Tags et segmentation

### 7.1 Pourquoi segmenter ?

**Avantages :**

- ✅ Emails ciblés selon intérêt
- ✅ Suivi personnalisé
- ✅ Offres adaptées au profil
- ✅ Meilleur taux de conversion

### 7.2 Créer des tags

**Exemples de tags pertinents :**

|Tag|Signification|Usage|
|---|---|---|
|`#accompagnement-juridique`|Intéressé par accompagnement juridique|Email ciblé sur ce service|
|`#essentiel-en-soi`|Intéressé par coaching personnel|Email sur bien-être|
|`#lead-chaud`|Très intéressé, répondu rapidement|Relance prioritaire|
|`#seance-decouverte-faite`|A déjà eu une séance|Proposition forfait|

**Appliquer un tag automatiquement :**

1. Formulaire > **Actions après soumission**
2. **Ajouter un tag** > Créer ou sélectionner
3. Le tag s'applique à tous les contacts de ce formulaire

### 7.3 Segmentation avancée

**Créer une liste de contacts ciblée :**

1. Contacts > **Filtres**
2. Combinez plusieurs critères :
    - Tag = `#accompagnement-juridique`
    - Date > Derniers 30 jours
    - Statut = Actif
3. Enregistrez le filtre > **"Liste personnalisée"**

---

## 8. Respect de la vie privée

### 8.1 Droits des utilisateurs (RGPD)

**Les visiteurs ont le droit de :**

- **Accès** : Voir leurs données collectées
- **Rectification** : Corriger leurs données
- **Suppression** : Supprimer leurs données
- **Portabilité** : Recevoir leurs données
- **Opposition** : Refuser l'usage de leurs données

### 8.2 Gérer les demandes RGPD

**Un contact demande la suppression de ses données :**

1. Contacts > Rechercher l'email
2. Cliquez sur le contact
3. Bouton **"Supprimer"** (icône corbeille)
4. Confirmez la suppression

> ⚠️ **Important :** Suppression définitive, non réversible.

### 8.3 Politique de confidentialité

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

---

## 9. Checklist formulaires

### ✅ Configuration

- [ ] Champs pertinents uniquement (3-5 max)
- [ ] Email toujours en champ obligatoire
- [ ] Case RGPD avec lien vers politique
- [ ] Bouton de soumission clair ("Envoyer ma demande")
- [ ] Message de validation configuré

### ✅ Design

- [ ] Formulaire visible (contraste)
- [ ] Labels clairs au-dessus des champs
- [ ] Placeholders informatifs
- [ ] Responsive (testémobi le)
- [ ] Champs assez grands (tactile)

### ✅ Automatisations

- [ ] Notification admin configurée
- [ ] Email de confirmation au contact
- [ ] Tags appliqués automatiquement
- [ ] Redirection après soumission

### ✅ RGPD et légal

- [ ] Politique de confidentialité accessible
- [ ] Consentement explicite
- [ ] Possibilité de désinscription
- [ ] Procédure de suppression documentée

---

## 10. Bonnes pratiques

### 10.1 Optimiser le taux de conversion

**Règles d'or :**

- ✅ **Minimum de champs** : 3 champs maximum (nom, email, message)
- ✅ **Valeur proposée** : "Recevez votre guide gratuit"
- ✅ **Urgence douce** : "Offre limitée" (si vrai)
- ✅ **Réassurance** : "Sans engagement", "Réponse sous 24h"
- ❌ **Éviter** : Trop de champs, jargon, design négligé

### 10.2 Tests A/B

**Éléments à tester :**

|Élément|Version A|Version B|
|---|---|---|
|**Titre**|"Contactez-moi"|"Réservez votre séance gratuite"|
|**Champs**|5 champs|3 champs|
|**Bouton**|"Envoyer"|"Je réserve maintenant"|
|**Couleur CTA**|Bleu|Rose|

**Durée de test :** 2 semaines minimum par variante

---

## 🆘 Problèmes courants

**Q : Le formulaire ne s'envoie pas**  
R : Vérifiez que tous les champs obligatoires sont remplis et que la case RGPD est cochée

**Q : Je ne reçois pas les notifications**  
R : Vérifiez votre adresse email dans Paramètres > Notifications. Regardez vos spams.

**Q : Impossible d'exporter les contacts**  
R : Vérifiez votre abonnement Systeme.io (fonctionnalité selon plan)

**Q : Un contact veut se désinscrire**  
R : Chaque email automatique doit contenir un lien de désinscription en bas

---

**Prochaine étape : [Guide 06 - SEO et Référencement](https://claude.ai/chat/06-SEO-REFERENCEMENT.md) 🔍**