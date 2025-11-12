# 📋 Historique des versions

Toutes les modifications notables de cette documentation sont documentées ici.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/), et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

---

## [Non publié] - En cours de développement

### À venir
- Création des 24 screenshots manquants pour les guides
- Tests utilisateurs avec le public cible
- Ajout de vidéos tutorielles intégrées
- Intégration commentaires et feedback utilisateurs

---

## [1.2.0] - 2025-11-12

### ✨ Ajouté

#### Documentation
- **Guide Google Analytics 4** (`CONFIGURATION-GOOGLE-ANALYTICS.md`) : Guide complet étape par étape
  - Création compte et propriété GA4
  - Configuration du flux de données Web
  - Intégration dans MkDocs
  - Événements personnalisés (partages, téléchargements, temps passé)
  - Conformité RGPD et bannière cookies
  - Métriques clés à suivre
  - Section dépannage complète
  - Checklist de configuration

#### Scripts d'automatisation (4 nouveaux)
- **optimize_images.py** (225 lignes) : Optimisation d'images
  - Compression PNG/JPG avec Pillow
  - Conversion WebP optionnelle
  - Génération versions responsive (320px → 1920px)
  - Rapport gains en KB et pourcentage

- **validate_frontmatter.py** (285 lignes) : Validation métadonnées YAML
  - Vérification syntaxe YAML
  - Champs requis et recommandés
  - Validation longueur description SEO (50-160 car.)
  - Mode normal vs strict

- **generate_stats.py** (325 lignes) : Statistiques documentation
  - Nombre pages, mots, temps de lecture
  - Éléments de contenu (code, images, liens)
  - Couverture assets
  - Top 5 pages longues
  - Export JSON

- **check_spelling.py** (275 lignes) : Vérification orthographique française
  - Dictionnaire français + personnalisé (50+ mots techniques)
  - Suggestions de corrections
  - Top 10 erreurs fréquentes
  - Ajout de mots au dictionnaire

### 🔧 Amélioré

- **Palette de couleurs** (04-DESIGN-MISE-EN-PAGE.md)
  - Codes hexadécimaux réels (fini les placeholders #XXXXXX)
  - 8 couleurs définies avec noms descriptifs
  - Ratios de contraste WCAG AA/AAA
  - Note d'accessibilité ajoutée

- **robots.txt** enrichi
  - Règles pour crawlers IA (GPTBot, Claude, Gemini, CCBot)
  - Désindexation /404.html et /search/
  - Crawl-delay configuré (1 seconde)
  - Documentation inline complète

- **scripts/README.md** : Documentation 4 nouveaux scripts
  - Installation dépendances
  - Exemples d'usage
  - Fonctionnalités détaillées

- **requirements.txt** : Dépendances optionnelles ajoutées
  - Pillow, PyYAML, pyspellchecker, requests
  - Documentation inline

### 📊 Statistiques

- **+1,800 lignes de code** ajoutées
- **5 nouveaux fichiers** créés
- **4 fichiers existants** améliorés
- **+9 nouveaux outils/guides**

---

## [1.1.1] - 2025-11-12

### 🔧 Corrigé
- **Plugin Git Revision Date** : Activé le plugin `mkdocs-git-revision-date-localized-plugin`
  - Affichage automatique des dates de dernière modification
  - Format français avec fallback sur date de build
- **Documentation Sitemap** : Clarification que le sitemap est intégré dans MkDocs core
  - Correction du commentaire erroné sur `mkdocs-sitemap` (package inexistant)
  - Documentation complète dans `CORRECTIONS-PLUGINS.md`
- **CI/CD GitHub Actions** : Correction erreur de déploiement
  - Installation du plugin git-revision-date-localized dans le workflow
  - Ajout de `fetch-depth: 0` pour historique Git complet
  - Utilisation de `requirements.txt` pour gestion des dépendances
  - Ajout du cache pip pour builds plus rapides

### 📚 Documentation
- Nouveau guide `docs/CORRECTIONS-PLUGINS.md` : Résolution des erreurs d'installation communes
- Instructions d'installation corrigées pour les plugins

### ✨ Ajouté
- **requirements.txt** : Gestion centralisée des dépendances Python
  - Versions minimales spécifiées pour tous les packages
  - Documentation inline pour chaque dépendance
  - Support export PDF (commenté, optionnel)

---

## [1.1.0] - 2025-11-12

### ✨ Ajouté
- **Boutons de partage social** : Possibilité de partager les guides sur Twitter, Facebook, LinkedIn et par email
- **Commande /export-pdf** : Nouvelle commande pour exporter la documentation complète en PDF
- **CHANGELOG.md** : Historique des versions et modifications de la documentation

### 🔧 Amélioré
- **Styles d'impression** : Amélioration massive des styles CSS pour impression/PDF
  - Gestion intelligente des sauts de page
  - Affichage des URLs pour les liens externes
  - Optimisation des tableaux et blocs de code
  - Numérotation automatique des pages
  - En-têtes et pieds de page personnalisés
- **Configuration de recherche** : Options avancées pour une recherche plus rapide et pertinente
  - Longueur minimale de recherche : 2 caractères
  - Indexation complète activée
  - Index pré-construit pour des performances optimales

### 📚 Documentation
- Guide d'utilisation des boutons de partage social dans `docs/snippets/share-buttons.md`
- Documentation complète de la commande `/export-pdf` avec instructions d'installation

---

## [1.0.0] - 2025-11-10

### 🎉 Version initiale

Cette version marque le lancement officiel de la formation Systeme.io pour L'Essentiel en Soi.

### ✨ Fonctionnalités principales

#### 📚 Contenu de formation
- **10 modules complets** couvrant tous les aspects de Systeme.io
  1. Guide de démarrage rapide
  2. Modification de contenu
  3. Ajout de boutons et CTA
  4. Design et mise en page
  5. Gestion des formulaires
  6. SEO et référencement
  7. Intégration Calendly
  8. Statistiques et suivi
  9. Maintenance régulière
  10. Dépannage et solutions

#### 🎨 Design et expérience utilisateur
- **Thème Material for MkDocs** avec personnalisation complète
- **Mode sombre/clair** avec transition fluide
- **Design responsive** optimisé mobile, tablette et desktop
- **2,407 lignes de CSS personnalisé** pour une identité visuelle unique
- **Accessibilité WCAG AAA** : Contraste, navigation clavier, lecteurs d'écran
- **Animations et transitions** pour une expérience fluide
- **Emojis et icônes** pour faciliter la navigation

#### 🛠️ Fonctionnalités techniques
- **Recherche en français** avec stemming et filtres
- **Minification HTML/CSS/JS** pour performances optimales
- **Navigation intuitive** avec fil d'Ariane et liens précédent/suivant
- **Admonitions stylisées** : Success, Tip, Warning, Danger, Info
- **Checklists interactives** pour valider les étapes
- **Tableaux comparatifs** pour les options Systeme.io
- **Blocs de code** avec coloration syntaxique

#### 🚀 Infrastructure et déploiement
- **CI/CD GitHub Actions** : Déploiement automatique sur push
- **Hébergement GitHub Pages** : https://mehdisback.github.io/formation-systemio/
- **Commandes slash personnalisées** :
  - `/serve` - Serveur de développement local
  - `/build` - Construction de la documentation
  - `/deploy` - Déploiement sur GitHub Pages
  - `/add-guide` - Création d'un nouveau guide
  - `/validate-docs` - Validation de l'intégrité
  - `/check-links` - Vérification des liens
- **Agents spécialisés** :
  - `@content-reviewer` - Révision du contenu français
  - `@accessibility-checker` - Audit d'accessibilité WCAG

#### 📊 SEO et analytics
- **Meta tags optimisés** pour chaque page
- **Open Graph** pour partage sur réseaux sociaux
- **Google Analytics 4** prêt à configurer
- **Sitemap XML** (à activer)
- **robots.txt** structuré
- **Descriptions personnalisées** pour chaque guide

#### ♿ Accessibilité
- **Navigation au clavier** : Tab, Enter, Esc
- **Contraste AAA** : Ratios ≥ 7:1
- **Skip links** : Accès direct au contenu
- **ARIA labels** : Support des lecteurs d'écran
- **Focus visible** : Indicateurs clairs
- **Tailles de texte** : Ajustables sans casser la mise en page

#### 🎯 Public cible
- **Professionnel·les du coaching** : Utilisatrices non techniques
- **Cas d'usage** : Formation autonome pour gestion de landing pages
- **Objectif** : Autonomie complète sur Systeme.io
- **Branding** : Coaching au Féminin + A-Tek Universe

### 📦 Assets
- Logo personnalisé : `docs/assets/logo.png`
- Favicon : `docs/assets/favicon.png`
- Spécifications OG Image : `docs/assets/branding/OG-IMAGE-SPECS.md`
- 1/25 screenshots créés (phase 2 à venir)

### 🔧 Configuration
- **Python** : ≥ 3.8
- **MkDocs** : ≥ 1.5.0
- **MkDocs Material** : ≥ 9.0.0
- **Plugins** : search, minify (+ sitemap, git-revision-date en attente)

### 📖 Documentation technique
- `CLAUDE.md` : Guide complet pour Claude Code
- `README.md` : Instructions d'installation et utilisation
- `AMELIORATIONS-APPLIQUEES.md` : Historique des améliorations techniques

---

## Convention de versionnage

Ce projet suit le [Semantic Versioning](https://semver.org/lang/fr/) :

- **MAJOR** (X.0.0) : Changements incompatibles avec versions antérieures
- **MINOR** (0.X.0) : Ajout de fonctionnalités compatibles
- **PATCH** (0.0.X) : Corrections de bugs compatibles

### Types de changements

- **Ajouté** : Nouvelles fonctionnalités
- **Modifié** : Changements dans les fonctionnalités existantes
- **Déprécié** : Fonctionnalités bientôt supprimées
- **Supprimé** : Fonctionnalités supprimées
- **Corrigé** : Corrections de bugs
- **Sécurité** : Corrections de vulnérabilités

---

## Roadmap future

### Version 1.2.0 (Prévu T1 2026)
- [ ] Ajout des 24 screenshots manquants
- [ ] Intégration de vidéos tutorielles
- [ ] Formulaire de feedback intégré
- [ ] Barre de progression de lecture
- [ ] Estimation du temps de lecture par page

### Version 1.3.0 (Prévu T2 2026)
- [ ] Blog intégré pour actualités Systeme.io
- [ ] Glossaire avec tooltips interactifs
- [ ] Quiz interactifs par module
- [ ] Tracker de progression (localStorage)
- [ ] Certificat de complétion téléchargeable

### Version 2.0.0 (Prévu T3 2026)
- [ ] Progressive Web App (PWA) : accès offline
- [ ] Mode "formation guidée" avec parcours structuré
- [ ] Intégration commentaires et discussions
- [ ] Support multilingue (anglais)
- [ ] Tableau de bord utilisateur personnalisé

---

## Contribuer

Pour signaler un bug, une suggestion ou une amélioration :

1. **Issues GitHub** : [github.com/Mehdisback/formation-systemio/issues](https://github.com/Mehdisback/formation-systemio/issues)
2. **Email** : Via le site L'Essentiel en Soi
3. **Pull Requests** : Contributions bienvenues !

---

## Remerciements

Un grand merci à tous ceux qui ont contribué à cette documentation :

- **A-Tek Universe** : Développement et intégration technique
- **Coaching au Féminin** : Expertise métier et validation du contenu
- **L'Essentiel en Soi** : Vision et objectifs de la formation
- **Communauté MkDocs** : Pour l'excellent framework de documentation

---

<div style="text-align: center; margin-top: 3rem; padding: 2rem; background: linear-gradient(135deg, #2C3A8F 0%, #6843A8 100%); border-radius: 0.75rem;">
  <p style="color: white; font-size: 1.1rem; font-weight: 600; margin: 0;">
    ⚡ Propulsé par <strong>A-Tek Universe</strong>
  </p>
  <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem; margin-top: 0.5rem;">
    Formation créée avec passion pour <strong>L'Essentiel en Soi</strong>
  </p>
</div>
