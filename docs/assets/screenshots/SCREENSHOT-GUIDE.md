# 📸 Guide de création des captures d'écran

## 🎯 Objectif

Créer 25 captures d'écran annotées de qualité professionnelle pour illustrer les 10 guides de formation.

## 🛠️ Outils recommandés

### Windows
- **Snagit** (payant, ~50€) - Le meilleur pour annotations
- **Greenshot** (gratuit) - Excellent et gratuit
- **ShareX** (gratuit, open-source) - Puissant mais interface technique

### macOS
- **Snagit** (payant, ~50€)
- **CleanShot X** (payant, ~29€/an) - Très populaire sur Mac
- **Cmd + Shift + 4** (natif) + **Preview** pour annotations

### Linux
- **Flameshot** (gratuit) - Équivalent Greenshot
- **Shutter** (gratuit) - Avec éditeur intégré
- **GNOME Screenshot** + **GIMP** pour édition

## 📋 Liste des captures nécessaires

### Guide 01 - Démarrage rapide (5 screenshots)
- [ ] `01-page-connexion-systemio.png` - Page de login Systeme.io
- [ ] `02-dashboard-principal.png` - Vue d'ensemble du dashboard
- [ ] `03-menu-funnels.png` - Localisation du menu Funnels
- [ ] `04-liste-funnels.png` - Liste des tunnels avec "Essentiel en Soi" surligné
- [ ] `05-editeur-ouvert.png` - Interface de l'éditeur visuel

### Guide 02 - Modification contenu (6 screenshots)
- [ ] `06-clic-sur-titre.png` - Titre sélectionné avec curseur
- [ ] `07-panneau-proprietes.png` - Panneau de droite avec options
- [ ] `08-modification-texte.png` - Texte en cours d'édition
- [ ] `09-ajout-image.png` - Dialogue d'ajout d'image
- [ ] `10-bibliotheque-images.png` - Bibliothèque d'images Systeme.io
- [ ] `11-temoignage-edition.png` - Édition d'un témoignage

### Guide 03 - CTA et Calendly (4 screenshots)
- [ ] `12-bouton-cta-selection.png` - CTA sélectionné
- [ ] `13-parametres-bouton.png` - Options de style du bouton
- [ ] `14-lien-calendly.png` - Configuration lien Calendly
- [ ] `15-test-cta.png` - Test du CTA en aperçu

### Guide 04 - Design (3 screenshots)
- [ ] `16-palette-couleurs.png` - Sélecteur de couleurs
- [ ] `17-styles-typographie.png` - Options de polices
- [ ] `18-responsive-mobile.png` - Vue mobile de la page

### Guide 05 - Formulaires (2 screenshots)
- [ ] `19-editeur-formulaire.png` - Configuration formulaire
- [ ] `20-champs-formulaire.png` - Liste des champs disponibles

### Guide 06 - SEO (2 screenshots)
- [ ] `21-parametres-seo.png` - Onglet SEO dans paramètres
- [ ] `22-meta-tags.png` - Configuration meta titre et description

### Guide 07 - Analytics (2 screenshots)
- [ ] `23-statistiques-dashboard.png` - Statistiques dans dashboard
- [ ] `24-google-analytics.png` - Configuration Google Analytics

### Guide 08 - Maintenance (1 screenshot)
- [ ] `25-historique-versions.png` - Historique des versions

## 🎨 Standards de qualité

### Résolution
- **Largeur** : 1920px (ou moins si responsive)
- **Format** : PNG (qualité maximale)
- **Compression** : Après annotations, compresser avec TinyPNG

### Annotations

**Flèches** :
- Couleur : Rouge (#FF0000) ou orange vif
- Épaisseur : 3-4px
- Pointes bien visibles

**Encadrés** :
- Bordure rouge ou orange
- Épaisseur : 2-3px
- Coins arrondis (optionnel)

**Textes** :
- Police : Arial ou Roboto
- Taille : 16-20px
- Couleur : Rouge ou orange
- Fond : Blanc semi-transparent si sur fond sombre

**Numérotation** :
- Cercles numérotés pour séquences (1, 2, 3...)
- Couleur : Blanc sur fond rouge/orange
- Taille : 24-30px de diamètre

### Zones sensibles à flouter

Pour la protection des données :
- Adresses email personnelles
- Noms complets (sauf Armelle Bodénès)
- Numéros de téléphone
- Données financières
- URLs de tunnels privés (si différents de l'exemple)

**Outil de floutage** : Flèche de flou dans Snagit, ou Pixelate dans GIMP

## 📝 Template alt text

Pour chaque screenshot, rédiger un alt text descriptif :

```markdown
![Capture d'écran montrant [ACTION/ÉLÉMENT PRINCIPAL], avec [ANNOTATIONS/INDICATIONS] surlignées en rouge, dans l'interface [CONTEXTE]](chemin/screenshot.png)
```

**Exemples** :

✅ **Bon** :
```markdown
![Capture d'écran de la page de connexion Systeme.io avec les champs Email et Mot de passe encadrés en rouge, et le bouton "Se connecter" surligné](01-page-connexion-systemio.png)
```

❌ **Mauvais** :
```markdown
![screenshot](01-page-connexion-systemio.png)
```

## 🔄 Workflow de création

1. **Préparer l'environnement**
   - Se connecter à Systeme.io
   - Ouvrir la landing page "Essentiel en Soi"
   - Vider cache navigateur pour interface propre
   - Mettre navigateur en plein écran (F11)

2. **Capturer**
   - Utiliser Snagit/Greenshot
   - Capturer zone pertinente (pas forcément tout l'écran)
   - Sauvegarder en PNG haute qualité

3. **Annoter**
   - Ajouter flèches vers éléments clés
   - Encadrer zones importantes
   - Numéroter si séquence d'actions
   - Ajouter textes explicatifs si nécessaire
   - Flouter données sensibles

4. **Optimiser**
   - Aller sur [TinyPNG](https://tinypng.com/)
   - Uploader le PNG
   - Télécharger version compressée (70% de réduction typique)
   - Renommer selon convention : `XX-nom-descriptif.png`

5. **Intégrer**
   - Placer dans `docs/assets/screenshots/`
   - Ajouter dans le guide concerné avec alt text
   - Tester affichage (mode clair et sombre)
   - Vérifier responsive (mobile, tablet, desktop)

## ✅ Checklist par screenshot

- [ ] Résolution 1920px ou adaptée
- [ ] Format PNG
- [ ] Annotations claires (flèches, encadrés)
- [ ] Données sensibles floutées
- [ ] Compressé avec TinyPNG
- [ ] Nommage convention `XX-nom-descriptif.png`
- [ ] Alt text rédigé (150-200 caractères)
- [ ] Intégré dans guide correspondant
- [ ] Testé en mode clair et sombre
- [ ] Vérifié responsive

## 💡 Astuces

### Captures de qualité
- Fermer onglets inutiles pour interface propre
- Désactiver extensions navigateur (icônes en haut)
- Zoom navigateur à 100% (Ctrl+0)
- Thème interface : clair (plus lisible)

### Annotations efficaces
- Moins c'est mieux : annoter uniquement l'essentiel
- Flèches courtes et directes
- Textes courts (3-5 mots max)
- Contraste élevé pour visibilité

### Organisation
- Créer sous-dossiers par guide si besoin
- Versionner les screenshots (v1, v2) si modifications UI Systeme.io
- Garder originaux non annotés (backup)

## 📊 Estimation temps

- **Préparation compte Systeme.io** : 10 min
- **Captures (25 screenshots)** : 1h30
- **Annotations et floutage** : 2h
- **Optimisation et intégration** : 1h
- **Tests et corrections** : 30 min

**Total : ~5 heures**

Peut être réparti sur plusieurs sessions.

## 🆘 Ressources

- [Snagit Tutorial](https://www.techsmith.com/tutorial-snagit.html)
- [Greenshot Docs](https://getgreenshot.org/help/)
- [TinyPNG](https://tinypng.com/)
- [Alt Text Best Practices](https://webaim.org/techniques/alttext/)

---

**Une fois terminé, marquer cette tâche comme complétée dans le rapport d'audit !** ✅
