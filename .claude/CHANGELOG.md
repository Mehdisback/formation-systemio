# Changelog - MkDocs Documentation Template

Toutes les modifications notables de ce template seront documentées ici.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/).

## [1.0.0] - 2024-01-XX

### ✨ Ajouté
- Template initial pour projets MkDocs Material
- Configuration `settings.json` optimisée pour documentation
- 6 commandes slash essentielles :
  - `/serve` - Serveur de développement
  - `/build` - Build de la documentation
  - `/deploy` - Déploiement GitHub Pages
  - `/add-guide` - Création de guide avec template
  - `/validate-docs` - Validation complète
  - `/check-links` - Vérification des liens
- 2 agents spécialisés :
  - `@content-reviewer` - Review de contenu français
  - `@accessibility-checker` - Audit accessibilité WCAG 2.1
- Permissions adaptées : MkDocs, Python/pip, Git
- Auto-compact activé à 95%
- Documentation complète (CLAUDE.md, README.md)
- Templates de guides de formation
- Support du français comme langue principale

### 🎨 Configuration
- Références ciblées : mkdocs.yml, docs/, extra.css, ci.yml
- Permissions `ask` pour déploiement (sécurité)
- Support MkDocs Material avec extensions courantes
- Workflow GitHub Actions pour CI/CD

### 📚 Documentation
- Guide d'utilisation complet
- Workflows recommandés
- Bonnes pratiques de rédaction
- Checklist de validation
- Guide de personnalisation

---

## Template pour futures versions

## [X.Y.Z] - YYYY-MM-DD

### ✨ Ajouté
- Nouvelles fonctionnalités

### 🔄 Modifié
- Changements dans fonctionnalités existantes

### 🐛 Corrigé
- Bugs corrigés

### 🗑️ Supprimé
- Fonctionnalités retirées

### ⚠️ Déprécié
- Fonctionnalités bientôt retirées

### 🔒 Sécurité
- Changements de sécurité

---

## Roadmap - Versions futures

### [1.1.0] - Prévu Q1 2024
- [ ] Agent `@seo-optimizer` pour optimisation SEO
- [ ] Commande `/generate-pdf` pour export PDF
- [ ] Support multilingue avec `/translate`
- [ ] Templates de guides spécialisés (API, FAQ, tutoriel)

### [1.2.0] - Prévu Q2 2024
- [ ] Agent `@image-optimizer` pour compression
- [ ] Commande `/analyze-performance` (Lighthouse)
- [ ] Integration tests automatisés
- [ ] Support MkDocs plugins additionnels

### [2.0.0] - Prévu Q3 2024
- [ ] Support multi-projets documentation
- [ ] Dashboard de métriques qualité
- [ ] Templates par industrie (tech, coaching, education)
- [ ] Export multi-formats (PDF, ePub, etc.)

---

## Notes de version

### Philosophie des versions
- **Majeure (X.0.0)** : Changements breaking, restructuration
- **Mineure (x.Y.0)** : Nouvelles fonctionnalités, commandes, agents
- **Patch (x.y.Z)** : Corrections bugs, améliorations mineures

### Comment contribuer au changelog
Lors de modifications du template :
1. Ajouter entrée dans section appropriée (Ajouté, Modifié, etc.)
2. Dater avec format ISO (YYYY-MM-DD)
3. Décrire changement clairement
4. Mentionner breaking changes si applicable

### Compatibilité
- **MkDocs Material** : ≥ 9.0.0
- **MkDocs** : ≥ 1.5.0
- **Python** : ≥ 3.8
- **Claude Code** : ≥ 1.0.0

---

## Historique de développement

### Inspiration et contexte
Ce template a été créé pour répondre au besoin de :
- Documentation technique accessible à public non-technique
- Formation utilisateur sur outils SaaS (type Systeme.io)
- Support multilingue (français prioritaire)
- Conformité accessibilité WCAG 2.1
- Automatisation du workflow documentation

### Cas d'usage testés
- ✅ Formation Systeme.io (public coaching)
- ✅ Documentation produit SaaS
- ✅ Guides utilisateur non-techniques
- ✅ Centre d'aide / Knowledge base
- ✅ Onboarding clients

### Retours utilisateurs
À mesure que le template sera utilisé, cette section documentera :
- Améliorations suggérées par la communauté
- Cas d'usage non prévus
- Personnalisations courantes
- Points de friction identifiés
