# Dépannage Google Analytics 4 - Diagnostic Complet

Guide de résolution des problèmes lorsque Google Analytics ne se charge pas malgré une configuration correcte.

---

## 🔍 Symptôme : "gtag n'est pas chargé"

Vous voyez dans la console du navigateur :

```
[Analytics] ⚠️ Google Analytics (gtag) non disponible après 10000 ms
[Analytics] Vérifiez que l'ID GA4 est configuré dans mkdocs.yml
```

**Ce guide vous aide à identifier la cause exacte du problème.**

---

## 📊 Diagnostic automatique

### Étape 1 : Lancer le script de diagnostic

```bash
python scripts/diagnose_analytics.py
```

Ce script vérifie :
- ✅ Présence de la section `extra.analytics` dans mkdocs.yml
- ✅ Format de l'ID GA4 (doit commencer par `G-`, pas `UA-`)
- ✅ Version de MkDocs Material dans requirements.txt
- ✅ Configuration des scripts personnalisés

### Étape 2 : Analyser les logs console améliorés

Depuis la version 1.3.0, le fichier `analytics-events.js` affiche un diagnostic détaillé :

```
[Analytics] 🔍 Diagnostic du problème
Hostname: mehdisback.github.io
URL complète: https://mehdisback.github.io/formation-systemio/01-GUIDE-DEMARRAGE-RAPIDE/
Scripts GA4 détectés dans le DOM: ✅ OUI ou ❌ NON
```

**Ce message révèle immédiatement la cause du problème !**

---

## 🧩 Cas 1 : "Scripts GA4 détectés: ❌ NON"

### Signification

MkDocs Material **n'a pas injecté** le script Google Analytics dans la page.

### Causes possibles

#### 1.1 ID GA4 non configuré ou placeholder

**Vérifier** : `mkdocs.yml` ligne ~227

```yaml
extra:
  analytics:
    provider: google
    property: G-XXXXXXXXXX  # ❌ PLACEHOLDER - Remplacer par vrai ID !
```

**Solution** :

```yaml
extra:
  analytics:
    provider: google
    property: G-ABC123XYZ  # ✅ Votre vrai ID GA4
```

**Commiter et redéployer** :

```bash
git add mkdocs.yml
git commit -m "fix: Configurer vrai ID Google Analytics 4"
git push origin main
```

---

#### 1.2 Ancienne syntaxe MkDocs Material (< 9.0)

**Vérifier** : Si vous voyez `google_analytics:` au lieu de `extra.analytics:`

```yaml
# ❌ ANCIENNE SYNTAXE (Material < 9.0)
google_analytics:
  - G-ABC123XYZ
  - auto
```

**Solution** : Migrer vers la nouvelle syntaxe (Material ≥ 9.0)

```yaml
# ✅ NOUVELLE SYNTAXE (Material ≥ 9.0)
extra:
  analytics:
    provider: google
    property: G-ABC123XYZ
```

**Référence** : [MkDocs Material 9.0 Release Notes](https://squidfunk.github.io/mkdocs-material/setup/setting-up-site-analytics/)

---

#### 1.3 Version de MkDocs Material obsolète

**Vérifier** : `requirements.txt`

```txt
mkdocs-material==8.5.0  # ❌ Trop ancien !
```

**Solution** : Mettre à jour vers ≥ 9.0.0

```txt
mkdocs-material>=9.0.0  # ✅ Version compatible
```

**Appliquer** :

```bash
pip install --upgrade mkdocs-material
mkdocs build
```

---

#### 1.4 Erreur d'indentation YAML

**Vérifier** : L'indentation dans mkdocs.yml (espaces, pas tabs)

```yaml
extra:
analytics:  # ❌ Mauvaise indentation !
  provider: google
  property: G-ABC123XYZ
```

**Solution** : 2 espaces par niveau

```yaml
extra:
  analytics:  # ✅ Bonne indentation
    provider: google
    property: G-ABC123XYZ
```

**Tester** :

```bash
python -c "import yaml; yaml.safe_load(open('mkdocs.yml'))"
# Si pas d'erreur → YAML valide
```

---

#### 1.5 Déploiement non effectué

**Vérifier** : Avez-vous rebuild et redéployé après la modification ?

```bash
# En local (pour tester)
mkdocs build
grep -r "googletagmanager" site/index.html

# Si vide → mkdocs.yml n'a pas été pris en compte
```

**Solution** : Forcer le rebuild complet

```bash
mkdocs build --clean
mkdocs serve  # Tester en local d'abord
git push      # Puis déployer
```

---

## 🛡️ Cas 2 : "Scripts GA4 détectés: ✅ OUI"

### Signification

Le script Google Analytics **est présent** dans la page, mais `gtag` n'est **pas défini**.

**Cause très probable : Bloqueur de publicité actif**

---

### 2.1 Bloqueurs de publicité courants

Les extensions suivantes bloquent Google Analytics :

| Extension | Chrome | Firefox | Edge |
|-----------|--------|---------|------|
| **uBlock Origin** | ✅ | ✅ | ✅ |
| **AdBlock Plus** | ✅ | ✅ | ✅ |
| **Ghostery** | ✅ | ✅ | ✅ |
| **Privacy Badger** | ✅ | ✅ | - |
| **Brave Shields** | ✅ (intégré) | - | - |

---

### 2.2 Solutions

#### Option 1 : Désactiver le bloqueur pour ce site

**Chrome/Edge** :
1. Cliquer sur l'icône de l'extension (ex: uBlock)
2. Cliquer sur le bouton **"Désactiver pour ce site"**
3. Recharger la page (F5)

**Firefox** :
1. Cliquer sur l'icône du bouclier (barre d'adresse)
2. Désactiver la **"Protection renforcée contre le pistage"**
3. Recharger la page

**Brave** :
1. Cliquer sur le lion Brave (barre d'adresse)
2. Désactiver **"Shields"**
3. Recharger

---

#### Option 2 : Tester en navigation privée SANS extensions

**Chrome** : Ctrl+Shift+N (Windows) ou Cmd+Shift+N (Mac)

**Firefox** : Ctrl+Shift+P (Windows) ou Cmd+Shift+P (Mac)

**Edge** : Ctrl+Shift+N

**Important** : Les extensions sont désactivées par défaut en navigation privée.

Si GA4 fonctionne en navigation privée → **Confirme qu'une extension bloque le tracking**.

---

#### Option 3 : Ajouter une exception dans uBlock Origin

1. Ouvrir uBlock Origin
2. Aller dans **"Tableau de bord"**
3. Onglet **"Liste blanche"**
4. Ajouter :
   ```
   mehdisback.github.io
   ```
5. Cliquer **"Appliquer les changements"**
6. Recharger le site

---

### 2.3 Autres causes possibles (rares)

#### DNS bloquant (Pi-hole, NextDNS, AdGuard DNS)

**Vérifier** :

```bash
nslookup www.googletagmanager.com
```

Si la résolution échoue ou retourne 0.0.0.0 → DNS bloquant actif.

**Solution** : Désactiver temporairement ou ajouter une exception.

---

#### Pare-feu d'entreprise / VPN

Certains VPN et réseaux d'entreprise bloquent les trackers publicitaires.

**Tester** : Désactiver le VPN et réessayer.

---

#### Politique CSP (Content Security Policy) trop stricte

**Vérifier** : Console → Onglet "Network" → Chercher une erreur CSP

```
Refused to load the script 'https://www.googletagmanager.com/...' because it violates the following Content Security Policy directive: "script-src 'self'"
```

**Solution** : MkDocs Material gère automatiquement CSP, mais si vous avez personnalisé `overrides/main.html`, vérifier :

```html
<meta http-equiv="Content-Security-Policy" content="script-src 'self' https://www.googletagmanager.com;">
```

---

## 🧪 Cas 3 : Localhost (Mode développement)

### Comportement attendu

Sur `localhost` ou `127.0.0.1`, **gtag n'est jamais chargé** (comportement normal).

Le script `analytics-events.js` détecte automatiquement localhost et active le **mode développement** :

```
[Analytics] ℹ️ Mode développement - Simulation du tracking (gtag non chargé)
[Analytics] 🚀 Initialisation des événements personnalisés
[Analytics DEV] event, share, {event_category: "Social", ...}
```

**C'est normal !** Les événements sont simulés avec `console.log`.

---

### Tester GA4 en production

1. **Déployer** sur GitHub Pages
2. **Ouvrir** : https://mehdisback.github.io/formation-systemio/
3. **Console** : Doit afficher `[Analytics] ✅ Google Analytics (gtag) chargé`

---

## 📋 Checklist de dépannage complète

### Étape 1 : Configuration

- [ ] ID GA4 dans `mkdocs.yml` commence par `G-` (pas `UA-`)
- [ ] Section `extra.analytics` présente (syntaxe Material 9.x)
- [ ] Pas de placeholder `G-XXXXXXXXXX`
- [ ] Indentation YAML correcte (2 espaces)
- [ ] `requirements.txt` : `mkdocs-material>=9.0.0`

### Étape 2 : Build et déploiement

- [ ] `mkdocs build` sans erreur ni warning
- [ ] `grep -r "googletagmanager" site/index.html` retourne du contenu
- [ ] Changements committés et pushés
- [ ] GitHub Actions terminé avec succès (check ✅)
- [ ] Site déployé sur GitHub Pages

### Étape 3 : Test navigateur (production uniquement)

- [ ] Ouvrir le site en production (pas localhost)
- [ ] Ouvrir la console (F12)
- [ ] Vérifier le diagnostic automatique dans la console
- [ ] Si "Scripts GA4: ❌ NON" → Revoir Étape 1
- [ ] Si "Scripts GA4: ✅ OUI" → Désactiver bloqueur de pub

### Étape 4 : Validation GA4

- [ ] Aller sur [Google Analytics](https://analytics.google.com)
- [ ] Sélectionner votre propriété GA4
- [ ] **Rapports → Temps réel**
- [ ] Naviguer sur votre site
- [ ] Vérifier qu'un utilisateur actif apparaît (délai : 5-30s)
- [ ] Cliquer sur un bouton de partage
- [ ] Vérifier l'événement `share` dans "Événements par nom"

---

## 🛠️ Outils de diagnostic

### 1. Script Python de diagnostic

```bash
python scripts/diagnose_analytics.py
```

Analyse `mkdocs.yml` et détecte les erreurs de configuration.

---

### 2. Vérifier le HTML généré

```bash
mkdocs build
grep -A5 -B5 "googletagmanager" site/index.html
```

**Attendu** :

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-ABC123XYZ"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-ABC123XYZ');
</script>
```

Si vide → MkDocs Material n'injecte pas le script → Revoir configuration.

---

### 3. Console navigateur (F12)

**Onglet Console** :

- Chercher les logs `[Analytics]`
- Lire le **diagnostic automatique** (nouvelle version 1.3.0)
- Noter si "Scripts GA4 détectés: OUI/NON"

**Onglet Network** :

- Filtrer par "gtag" ou "googletagmanager"
- Vérifier qu'une requête est faite vers `https://www.googletagmanager.com/gtag/js?id=G-...`
- Si status 200 mais pas de gtag → Bloqueur actif
- Si aucune requête → Configuration incorrecte

**Onglet Application** :

- Section **"Frames" → "Top" → "Scripts"**
- Chercher `gtag/js?id=G-...`
- Si présent → Script chargé (problème = bloqueur)
- Si absent → Script non injecté (problème = configuration)

---

### 4. Extension Chrome "Tag Assistant"

**Installer** : [Tag Assistant Legacy](https://chrome.google.com/webstore/detail/tag-assistant-legacy-by-g/kejbdjndbnbjgmefkgdddjlbokphdefk)

**Utilisation** :
1. Ouvrir votre site
2. Cliquer sur l'extension Tag Assistant
3. Cliquer **"Enable"**
4. Recharger la page
5. Tag Assistant affiche tous les tags Google détectés
6. Vérifier que **"Google Analytics 4"** est présent et vert

Si rouge ou absent → Problème de configuration ou blocage.

---

## 📚 Références

### Documentation officielle

- [MkDocs Material - Setting up Site Analytics](https://squidfunk.github.io/mkdocs-material/setup/setting-up-site-analytics/)
- [Google Analytics 4 - Quick Start](https://support.google.com/analytics/answer/9304153)
- [MkDocs Material 9.0 Release Notes](https://squidfunk.github.io/mkdocs-material/changelog/#900)

### Fichiers du projet

- Configuration : `mkdocs.yml` ligne ~227
- Script de tracking : `docs/javascripts/analytics-events.js`
- Script de diagnostic : `scripts/diagnose_analytics.py`
- Guide de configuration : `docs/CONFIGURATION-GOOGLE-ANALYTICS.md`
- Guide de test : `docs/GUIDE-TEST-ANALYTICS.md`

---

## 💡 Résumé : Arbre de décision

```
gtag non chargé
│
├─ Localhost ?
│  └─ ✅ Normal ! Mode dev activé automatiquement
│
├─ Console : "Scripts GA4: ❌ NON"
│  ├─ Vérifier mkdocs.yml → ID GA4 configuré ?
│  ├─ Vérifier syntaxe → extra.analytics (Material 9.x) ?
│  ├─ Vérifier version → mkdocs-material >= 9.0.0 ?
│  ├─ Vérifier YAML → Indentation correcte ?
│  └─ Rebuild et redéployer
│
└─ Console : "Scripts GA4: ✅ OUI"
   ├─ Désactiver bloqueur de pub
   ├─ Tester en navigation privée
   ├─ Vérifier DNS bloquant (Pi-hole, etc.)
   └─ Vérifier VPN / Pare-feu
```

---

## ✅ Cas d'usage réel : Votre situation

D'après votre message :

> "j'ai pourtant bien renseigné property sur une autre branche mais tu n'y a juste pas accès ici"

**Analyse** :

1. ✅ Vous avez configuré l'ID GA4 sur une autre branche
2. ❓ Le problème persiste malgré la configuration

**Prochaines étapes recommandées** :

1. **Sur la branche configurée** : Ouvrir le site déployé en production
2. **Ouvrir la console** (F12)
3. **Lire le diagnostic automatique** :
   - Si "Scripts GA4: ❌ NON" → Problème de configuration (ID non pris en compte, syntaxe, version)
   - Si "Scripts GA4: ✅ OUI" → Bloqueur de publicité actif
4. **Tester en navigation privée** sans extensions
5. **Si ça fonctionne en nav privée** → Confirme qu'une extension bloque GA4

**Diagnostic le plus probable** : Bloqueur de publicité (uBlock Origin, AdBlock, etc.)

---

**Date de création** : 2025-11-12
**Version** : 1.3.0
**Dernière mise à jour** : Ajout diagnostic automatique amélioré dans analytics-events.js
