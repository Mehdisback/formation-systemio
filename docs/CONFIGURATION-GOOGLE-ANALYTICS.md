# Configuration Google Analytics 4 (GA4)

Guide complet pour configurer Google Analytics 4 sur votre documentation Formation Systeme.io.

---

## 📊 Pourquoi Google Analytics ?

Google Analytics vous permet de :

- **Suivre les visiteurs** : Nombre de visiteurs, pages vues, durée des sessions
- **Analyser le comportement** : Quels guides sont les plus consultés ?
- **Mesurer l'engagement** : Temps passé sur chaque page, taux de rebond
- **Comprendre votre audience** : Provenance géographique, appareils utilisés
- **Améliorer le contenu** : Identifier les pages à améliorer

---

## 🚀 Étape 1 : Créer un compte Google Analytics

### 1.1 Accéder à Google Analytics

1. Aller sur [https://analytics.google.com](https://analytics.google.com)
2. Se connecter avec votre compte Google
3. Cliquer sur **"Commencer à mesurer"**

### 1.2 Créer une propriété GA4

1. **Nom du compte** : `Formation Systeme.io` (ou votre nom)
2. **Nom de la propriété** : `Formation Systeme.io - L'Essentiel en Soi`
3. **Fuseau horaire** : `(GMT+01:00) Paris`
4. **Devise** : `Euro (EUR)`

### 1.3 Configurer le flux de données

1. Type de plateforme : **Web**
2. URL du site web : `https://mehdisback.github.io`
3. Nom du flux : `Formation Systeme.io GitHub Pages`
4. Cliquer sur **"Créer un flux"**

### 1.4 Récupérer l'ID de mesure

Après création, vous verrez l'**ID de mesure** au format :

```
G-XXXXXXXXXX
```

**C'est cet ID qu'il faut utiliser dans la configuration MkDocs.**

---

## ⚙️ Étape 2 : Configurer MkDocs

### 2.1 Ouvrir mkdocs.yml

Ouvrir le fichier `mkdocs.yml` à la racine du projet.

### 2.2 Trouver la section Google Analytics

Rechercher la section (autour de la ligne 220) :

```yaml
google_analytics:
  - G-XXXXXXXXXX  # ← REMPLACER ICI
  - auto
```

### 2.3 Remplacer l'ID placeholder

Remplacer `G-XXXXXXXXXX` par votre vrai ID de mesure :

```yaml
google_analytics:
  - G-ABC123XYZ  # ← Votre ID réel
  - auto
```

**Exemple concret :**

```yaml
# Analytics
google_analytics:
  - G-H7M2K9P3R5  # ID de mesure GA4
  - auto            # Configure automatiquement les pageviews
```

### 2.4 Sauvegarder et committer

```bash
git add mkdocs.yml
git commit -m "feat: Configurer Google Analytics 4"
git push origin main
```

---

## ✅ Étape 3 : Vérifier l'installation

### 3.1 Déployer les changements

Après le push vers `main`, GitHub Actions va :
1. Builder la documentation
2. Déployer sur GitHub Pages
3. Inclure le code de tracking GA4

### 3.2 Tester en temps réel

1. Aller sur [https://analytics.google.com](https://analytics.google.com)
2. Sélectionner votre propriété
3. Cliquer sur **"Rapports" → "Temps réel"**
4. Ouvrir votre site : https://mehdisback.github.io/formation-systemio/
5. Vous devriez voir votre visite apparaître dans GA4 (délai : 30 secondes)

### 3.3 Vérifier le code de tracking

1. Ouvrir votre site dans un navigateur
2. Appuyer sur **F12** pour ouvrir les outils de développement
3. Aller dans l'onglet **"Console"**
4. Rechercher des messages liés à `gtag` ou `analytics`
5. Vous devriez voir des requêtes vers `https://www.google-analytics.com/g/collect`

---

## 📊 Étape 4 : Configurer les événements personnalisés (optionnel)

Pour suivre des interactions spécifiques (clics sur boutons, téléchargements PDF, etc.).

### 4.1 Ajouter du JavaScript personnalisé

Créer le fichier `docs/javascripts/analytics-events.js` :

```javascript
// Tracking des clics sur les boutons de partage social
document.addEventListener('DOMContentLoaded', function() {
  const shareButtons = document.querySelectorAll('.share-button');

  shareButtons.forEach(button => {
    button.addEventListener('click', function() {
      const network = this.classList[1]; // twitter, facebook, linkedin

      gtag('event', 'share', {
        'event_category': 'Social',
        'event_label': network,
        'value': 1
      });
    });
  });
});

// Tracking des téléchargements PDF
document.querySelectorAll('a[href$=".pdf"]').forEach(link => {
  link.addEventListener('click', function() {
    gtag('event', 'download', {
      'event_category': 'Downloads',
      'event_label': this.href,
      'value': 1
    });
  });
});

// Tracking du temps passé sur chaque guide
let startTime = Date.now();
window.addEventListener('beforeunload', function() {
  const timeSpent = Math.round((Date.now() - startTime) / 1000);

  gtag('event', 'timing_complete', {
    'name': 'Guide Reading Time',
    'value': timeSpent,
    'event_category': 'Engagement'
  });
});
```

### 4.2 Référencer le script dans mkdocs.yml

```yaml
extra_javascript:
  - javascripts/analytics-events.js
```

---

## 📈 Rapports utiles dans GA4

### Rapports en temps réel
- **Utilisateurs actifs** : Combien de personnes sur le site maintenant
- **Pages consultées** : Quelles pages sont vues en ce moment

### Rapports d'acquisition
- **Vue d'ensemble** : D'où viennent vos visiteurs (Google, réseaux sociaux, direct)
- **Source/Support** : Détails des canaux d'acquisition

### Rapports d'engagement
- **Pages et écrans** : Pages les plus consultées
- **Événements** : Interactions personnalisées (partages, téléchargements)

### Rapports démographiques
- **Données démographiques** : Âge et sexe des visiteurs
- **Données technologiques** : Appareils, navigateurs, systèmes d'exploitation

---

## 🎯 Métriques clés à suivre

### Métriques de base
| Métrique | Cible | Comment l'améliorer |
|----------|-------|---------------------|
| **Utilisateurs** | Augmentation mensuelle | SEO, partage sur réseaux sociaux |
| **Sessions** | 2+ par utilisateur | Contenu engageant, navigation claire |
| **Taux de rebond** | < 40% | Améliorer intro, ajouter liens internes |
| **Durée moyenne session** | > 5 minutes | Contenu détaillé, exemples pratiques |

### Métriques de contenu
| Métrique | Cible | Action |
|----------|-------|--------|
| **Pages/session** | > 3 | Liens de navigation clairs |
| **Taux de complétion** | > 60% | Suivre progression dans les guides |
| **Pages populaires** | - | Créer plus de contenu similaire |
| **Pages abandonnées** | < 50% | Améliorer contenu, ajouter médias |

---

## 🔒 Confidentialité et RGPD

### Conformité RGPD

Google Analytics 4 est **conforme au RGPD** si configuré correctement :

1. **Anonymisation IP** : Activée par défaut dans GA4
2. **Consentement cookies** : À implémenter si site commercial
3. **Politique de confidentialité** : À ajouter dans le footer

### Bannière de cookies (optionnel)

Pour un site de documentation non-commercial, une bannière n'est pas obligatoire, mais recommandée.

**Exemple simple dans `overrides/main.html` :**

```html
<div id="cookie-banner" style="position: fixed; bottom: 0; width: 100%; background: #333; color: white; padding: 1rem; text-align: center; z-index: 1000;">
  <p style="margin: 0 0 0.5rem 0;">
    Ce site utilise Google Analytics pour améliorer votre expérience.
    <a href="/politique-confidentialite/" style="color: #7E57C2; text-decoration: underline;">En savoir plus</a>
  </p>
  <button onclick="acceptCookies()" style="background: #7E57C2; color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;">
    J'accepte
  </button>
</div>

<script>
function acceptCookies() {
  localStorage.setItem('cookies_accepted', 'true');
  document.getElementById('cookie-banner').style.display = 'none';
}

// Cacher si déjà accepté
if (localStorage.getItem('cookies_accepted')) {
  document.getElementById('cookie-banner').style.display = 'none';
}
</script>
```

---

## 🛠️ Dépannage

### Le tracking ne fonctionne pas

**1. Vérifier l'ID de mesure**

- L'ID doit commencer par `G-` (pas `UA-`)
- Vérifier qu'il n'y a pas d'espaces ou de fautes de frappe

**2. Vérifier le déploiement**

```bash
# Builder localement
mkdocs build

# Vérifier que le code GA est présent dans le HTML
grep -r "G-ABC123XYZ" site/
```

**3. Bloqueurs de publicité**

- Les bloqueurs de pub (uBlock, AdBlock) bloquent Google Analytics
- Tester en navigation privée sans extensions

**4. Délai d'affichage**

- Les données peuvent prendre 24-48h pour apparaître dans les rapports standards
- Utiliser le rapport "Temps réel" pour des résultats immédiats

### Erreur : "Data stream not found"

Vérifier que le flux de données GA4 est bien créé et actif.

### Aucune donnée après 48h

1. Vérifier que le site est bien déployé sur GitHub Pages
2. S'assurer que robots.txt autorise le crawling
3. Vérifier les filtres GA4 (aucun filtre IP ne bloque le trafic)

---

## 📚 Ressources

- [Documentation Google Analytics 4](https://support.google.com/analytics/answer/10089681)
- [MkDocs Material - Analytics](https://squidfunk.github.io/mkdocs-material/setup/setting-up-site-analytics/)
- [RGPD et Google Analytics](https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/google-analytics-et-autres-outils-de-mesure-daudience)

---

## ✅ Checklist de configuration

- [ ] Compte Google Analytics créé
- [ ] Propriété GA4 créée
- [ ] Flux de données Web configuré
- [ ] ID de mesure récupéré (G-XXXXXXXXXX)
- [ ] ID ajouté dans mkdocs.yml
- [ ] Changements committés et pushés
- [ ] Site redéployé sur GitHub Pages
- [ ] Tracking vérifié en temps réel
- [ ] Événements personnalisés configurés (optionnel)
- [ ] Bannière cookies ajoutée (optionnel)

---

**Date de ce document** : 2025-11-12
**Dernière mise à jour** : Version initiale
