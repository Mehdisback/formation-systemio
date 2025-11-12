# Guide de Test - Tracking Google Analytics 4

Ce guide vous aide à tester que les boutons de partage et le tracking GA4 fonctionnent correctement.

---

## 🧪 Test 1 : Vérifier le script (localhost)

### Étapes

1. **Lancer le serveur local**
   ```bash
   mkdocs serve
   ```

2. **Ouvrir dans le navigateur**
   ```
   http://127.0.0.1:8000
   ```

3. **Ouvrir la console** (F12 > Console)

4. **Naviguer vers un guide** (ex: Guide 01)

### Résultats attendus

Vous devriez voir dans la console :

```
[Analytics] ℹ️ Mode développement - Simulation du tracking (gtag non chargé)
[Analytics] 🚀 Initialisation des événements personnalisés
[Analytics] 4 boutons de partage trackés
[Analytics] X liens PDF trackés
[Analytics] X boutons de navigation trackés
[Analytics] X admonitions trackées
[Analytics] X liens externes trackés
[Analytics] ✅ Tous les événements personnalisés sont configurés
```

5. **Tester un bouton de partage**

Cliquer sur "🐦 Twitter" → Vous devriez voir :
```
[Analytics DEV] event, share, {event_category: "Social", event_label: "Twitter", ...}
```

6. **Tester un checkbox**

Cocher un item de checklist → Vous devriez voir :
```
[Analytics DEV] event, checklist_item, {event_category: "Engagement", ...}
```

7. **Tester la navigation**

Cliquer sur "Suivant" → Vous devriez voir :
```
[Analytics DEV] event, navigation, {event_category: "Navigation", event_label: "Next Guide", ...}
```

✅ **Si vous voyez ces logs, le tracking fonctionne en mode dev !**

---

## 🚀 Test 2 : Configurer Google Analytics (optionnel maintenant)

Si vous voulez tester avec un vrai GA4 :

### Étape 1 : Obtenir un ID GA4

1. Aller sur [https://analytics.google.com](https://analytics.google.com)
2. Créer une propriété GA4 (voir `docs/CONFIGURATION-GOOGLE-ANALYTICS.md`)
3. Récupérer l'ID (format : `G-ABC123XYZ`)

### Étape 2 : Configurer mkdocs.yml

```yaml
# mkdocs.yml ligne 227
extra:
  analytics:
    provider: google
    property: G-ABC123XYZ  # ← Votre vrai ID ici
```

### Étape 3 : Rebuild et redéployer

```bash
mkdocs build
# Ou pusher vers main pour déploiement auto
```

### Étape 4 : Tester en production

1. Aller sur votre site déployé
2. Ouvrir la console (F12)
3. Vérifier les logs :
   ```
   [Analytics] ✅ Google Analytics (gtag) chargé
   [Analytics] 🚀 Initialisation des événements personnalisés
   [Analytics] ✅ Tous les événements configurés
   ```

4. Cliquer sur un bouton de partage
5. Aller dans GA4 > Rapports > Temps réel > Événements
6. Vérifier que l'événement `share` apparaît (délai : 5-30s)

---

## 🔍 Test 3 : Vérifier les boutons de partage

### Sur chaque guide (01-10)

1. **Défiler jusqu'à la fin du guide**
2. **Chercher la section "📤 Partager ce guide"**
3. **Vérifier 4 boutons présents** :
   - 🐦 Twitter
   - 📘 Facebook
   - 💼 LinkedIn
   - ✉️ Email

4. **Tester chaque bouton** :

   **Twitter** :
   - Clic → Ouvre Twitter avec texte pré-rempli
   - URL : `formation-systemio/XX-NOM-GUIDE/`
   - Texte : `Formation Systeme.io - [Titre]`

   **Facebook** :
   - Clic → Ouvre Facebook share dialog
   - URL partagée correcte

   **LinkedIn** :
   - Clic → Ouvre LinkedIn share
   - URL partagée correcte

   **Email** :
   - Clic → Ouvre client email
   - Sujet : `Formation Systeme.io - [Titre]`
   - Corps : Lien vers le guide

✅ **Tous les boutons doivent ouvrir le bon réseau avec les bonnes informations**

---

## 📊 Test 4 : Événements GA4 (après configuration)

### Événements à tester

| Action | Événement GA4 | Comment vérifier |
|--------|---------------|------------------|
| Clic partage Twitter | `share` | GA4 > Temps réel > Événements |
| Navigation → Suivant | `navigation` | GA4 > Temps réel > Événements |
| Scroll 50% | `scroll_depth` | GA4 > Temps réel > Événements |
| Cocher checkbox | `checklist_item` | GA4 > Temps réel > Événements |
| Clic lien externe | `external_link` | GA4 > Temps réel > Événements |
| Rester 60+ secondes | `scroll_engagement` | GA4 > Temps réel > Événements |
| Quitter la page (≥10s) | `timing_complete` | GA4 > Engagement > Pages et écrans |

### Dans GA4 (24-48h après activation)

**Rapports > Engagement > Événements** :

Vous devriez voir :
- `share` : Nombre de partages sociaux
- `navigation` : Clics entre guides
- `scroll_depth` : Jalons de lecture (25%, 50%, 75%, 90%, 100%)
- `checklist_item` : Items cochés
- `external_link` : Liens sortants
- `timing_complete` : Temps passé par guide

**Analyser les dimensions personnalisées** :
- `event_label` : Type de réseau social, type de navigation
- `page_title` : Titre du guide
- `guideNumber` : Numéro du guide (01-10)

---

## ⚠️ Dépannage

### Problème : Aucun log dans la console

**Cause** : JavaScript désactivé ou erreur de syntaxe

**Solution** :
```bash
# Vérifier qu'il n'y a pas d'erreur
grep -n "SyntaxError" /tmp/mkdocs-serve.log

# Rebuild clean
mkdocs build --clean
mkdocs serve
```

---

### Problème : "gtag n'est pas chargé" en production

**Cause** : ID GA4 non configuré ou incorrect dans mkdocs.yml

**Solution** :
1. Vérifier `mkdocs.yml` ligne 227
2. S'assurer que l'ID commence par `G-` (pas `UA-`)
3. Rebuild et redéployer

---

### Problème : Boutons de partage ne s'affichent pas

**Cause** : CSS non chargé ou guide non mis à jour

**Solution** :
```bash
# Vérifier que le CSS existe
ls -la docs/stylesheets/extra.css

# Vérifier qu'un guide a bien les boutons
grep -A5 "📤 Partager ce guide" docs/01-GUIDE-DEMARRAGE-RAPIDE.md

# Rebuild
mkdocs build --clean
```

---

### Problème : Événements n'apparaissent pas dans GA4

**Cause** : Délai de traitement ou configuration incorrecte

**Solution** :
1. **Attendre 5-30 secondes** (Temps réel)
2. **Vérifier dans "Temps réel" pas dans "Rapports"** (délai 24-48h)
3. **Désactiver bloqueurs de pub** (uBlock, AdBlock)
4. **Tester en navigation privée**

---

### Problème : Trop de logs dans la console

**Cause** : Mode développement activé

**Solution** : Normal en localhost ! Les logs disparaîtront en production.

---

## ✅ Checklist de validation complète

### Développement (localhost)
- [ ] `mkdocs serve` démarre sans erreur
- [ ] Console affiche `[Analytics] ℹ️ Mode développement`
- [ ] Console affiche `[Analytics] ✅ Tous les événements configurés`
- [ ] Clic partage → Log `[Analytics DEV]`
- [ ] Clic navigation → Log `[Analytics DEV]`
- [ ] Checkbox → Log `[Analytics DEV]`
- [ ] Aucune erreur JavaScript

### Boutons de partage
- [ ] Guide 01 : Section "📤 Partager" visible
- [ ] Guide 02 : Section "📤 Partager" visible
- [ ] ... (répéter pour guides 03-10)
- [ ] Bouton Twitter ouvre Twitter avec bon texte
- [ ] Bouton Facebook ouvre Facebook
- [ ] Bouton LinkedIn ouvre LinkedIn
- [ ] Bouton Email ouvre client email

### Production (après GA4 configuré)
- [ ] Console affiche `[Analytics] ✅ gtag chargé`
- [ ] GA4 > Temps réel > Événements affiche activité
- [ ] Événement `share` apparaît après clic
- [ ] Événement `navigation` apparaît
- [ ] Événement `scroll_depth` apparaît après scroll
- [ ] Événement `timing_complete` enregistré au départ
- [ ] Aucune erreur dans la console

### Analytics (après 24-48h)
- [ ] Rapports > Engagement > Événements montre tous les types
- [ ] Dimensions personnalisées visibles (event_label, page_title)
- [ ] Données cohérentes avec l'utilisation réelle
- [ ] Possibilité de créer des rapports personnalisés

---

## 📞 Support

Si vous rencontrez un problème non listé :

1. Vérifier `docs/CONFIGURATION-GOOGLE-ANALYTICS.md`
2. Vérifier `docs/CORRECTIONS-PLUGINS.md`
3. Consulter la console du navigateur (F12)
4. Vérifier les logs GitHub Actions (si déploiement)

---

**Date de création** : 2025-11-12
**Version** : 1.3.0
