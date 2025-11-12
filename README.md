# Template MkDocs Material Documentation

Template optimisé pour projets de documentation MkDocs Material avec Claude Code.

## 🎯 À qui s'adresse ce template ?

Projets de documentation technique ou de formation utilisant :
- **MkDocs Material** comme générateur
- **GitHub Pages** pour l'hébergement
- **Markdown** pour le contenu
- **Public francophone** (ou autre langue unique)
- **Audience non-technique** (documentation utilisateur, guides de formation)

## ✨ Caractéristiques

### 🚀 Commandes slash incluses
- `/serve` - Serveur de développement avec live reload
- `/build` - Build de la documentation
- `/deploy` - Déploiement GitHub Pages (avec confirmation)
- `/add-guide` - Création de nouveau guide avec template
- `/validate-docs` - Validation complète de la documentation
- `/check-links` - Vérification des liens internes/externes

### 🤖 Agents spécialisés
- `@content-reviewer` - Review de contenu (français, clarté, ton)
- `@accessibility-checker` - Audit accessibilité WCAG 2.1

### ⚙️ Configuration optimisée
- **Permissions** : MkDocs, Git, Python/pip
- **Auto-compact** : Activé à 95%
- **Références** : mkdocs.yml, docs/, styles, CI/CD
- **Sécurité** : Déploiement nécessite confirmation

## 📦 Contenu du template

```
mkdocs-documentation/
├── CLAUDE.md                    # Mémoire projet complète
├── README.md                    # Ce fichier
└── .claude/
    ├── settings.json            # Configuration Claude Code
    ├── CHANGELOG.md             # Historique des modifications
    ├── README.md                # Documentation de configuration
    ├── commands/
    │   ├── README.md
    │   ├── serve.md             # /serve
    │   ├── build.md             # /build
    │   ├── deploy.md            # /deploy
    │   ├── add-guide.md         # /add-guide
    │   ├── validate-docs.md     # /validate-docs
    │   └── check-links.md       # /check-links
    └── agents/
        ├── README.md
        ├── content-reviewer.md       # @content-reviewer
        └── accessibility-checker.md  # @accessibility-checker
```

## 🚀 Utilisation

### Installation avec init-env.sh

```bash
cd claude-env-manager
./scripts/init-env.sh mon-projet-docs mkdocs-documentation
```

### Installation manuelle

```bash
# Copier le template
cp -r templates/mkdocs-documentation/.claude /chemin/vers/mon-projet/

# Copier CLAUDE.md et personnaliser
cp templates/mkdocs-documentation/CLAUDE.md /chemin/vers/mon-projet/
```

### Personnalisation post-installation

1. **CLAUDE.md** : Adapter au contexte de votre projet
   - Remplacer les URLs et noms de domaine
   - Ajuster la structure de navigation
   - Adapter le public cible et le ton

2. **mkdocs.yml** : Vérifier qu'il correspond à votre config
   ```yaml
   site_name: Votre Documentation
   site_url: https://votreuser.github.io/votreprojet/
   theme:
     name: material
     language: fr  # ou autre langue
   ```

3. **settings.json** : Ajuster les permissions si nécessaire
   ```json
   "references": [
     "mkdocs.yml",
     "docs/",
     "votre-fichier-specifique.md"
   ]
   ```

4. **Commandes** : Personnaliser pour votre workflow
   - Ajouter des commandes spécifiques
   - Modifier les templates de guides

## 📋 Workflow typique

### Premier lancement
```bash
# 1. Vérifier que MkDocs est installé
pip install mkdocs-material mkdocs-minify-plugin

# 2. Lancer le serveur de développement
/serve

# 3. Créer votre premier guide
/add-guide 01 "Guide de démarrage"

# 4. Valider
/validate-docs
```

### Développement quotidien
```bash
# Édition de contenu
/serve                    # Une fois au début
# Éditer les .md
# Vérifier dans le navigateur en temps réel

# Avant commit
/validate-docs
/build

# Commit et push
git add . && git commit -m "feat: nouveau guide"
git push  # Déploiement auto via GitHub Actions
```

### Maintenance périodique
```bash
# Hebdomadaire
/check-links              # Vérifier liens externes

# Mensuel
@content-reviewer review-all           # Review complète
@accessibility-checker full-report     # Audit accessibilité
```

## 🎨 Customisation

### Ajouter une commande

1. Créer `.claude/commands/ma-commande.md`
2. Suivre le format des commandes existantes
3. Tester avec `/ma-commande`
4. Documenter dans `.claude/commands/README.md`

### Créer un agent

1. Créer `.claude/agents/mon-agent.md`
2. Définir mission, expertise, vérifications
3. Ajouter dans `settings.json` :
   ```json
   "agents": {
     "allow": [
       "@content-reviewer",
       "@accessibility-checker",
       "@mon-agent"
     ]
   }
   ```
4. Documenter dans `.claude/agents/README.md`

### Modifier le branding

Dans `CLAUDE.md`, adapter :
- Noms et URLs du projet
- Palette de couleurs
- Ton et style de communication
- Public cible

## 🔧 Prérequis projet MkDocs

### Structure minimale requise
```
mon-projet/
├── mkdocs.yml           # Configuration MkDocs
├── docs/
│   ├── index.md         # Page d'accueil
│   └── ...              # Autres guides
├── CLAUDE.md            # Du template
└── .claude/             # Du template
```

### Dépendances Python
```bash
pip install mkdocs-material>=9.0.0
pip install mkdocs-minify-plugin  # Si utilisé
```

### GitHub Pages (optionnel mais recommandé)
- Repository GitHub avec Pages activé
- Branche `gh-pages` créée (auto par mkdocs gh-deploy)
- Workflow `.github/workflows/ci.yml` pour auto-deploy

## ✅ Checklist après installation

- [ ] Template copié dans le projet
- [ ] CLAUDE.md personnalisé
- [ ] settings.json ajusté
- [ ] MkDocs installé (`pip install mkdocs-material`)
- [ ] `/serve` fonctionne
- [ ] `/build` passe sans erreur
- [ ] GitHub Pages configuré (si applicable)
- [ ] CI/CD workflow testé
- [ ] Équipe formée aux commandes

## 💡 Bonnes pratiques

### Contenu
- ✍️ Français clair et simple (ou langue cible)
- 🎯 Public non-technique → éviter jargon
- 📸 Captures d'écran annotées
- ⚠️ Admonitions pour points importants
- 🔗 Navigation précédent/suivant entre guides

### Technique
- 🧪 Toujours tester avec `/serve` avant commit
- ✅ Lancer `/validate-docs` avant chaque push
- 🔗 Vérifier `/check-links` hebdomadairement
- 🤖 Utiliser agents pour reviews approfondies
- 🚀 CI/CD pour déploiement automatique

### Accessibilité
- ♿ WCAG 2.1 AA minimum
- 🎨 Contraste ≥ 4.5:1
- 🖼️ Alt text pour toutes les images
- ⌨️ Navigation au clavier complète
- 📱 Responsive design testé

## 📊 Métriques de réussite

Un projet MkDocs sain avec ce template :
- ✅ `/serve` et `/build` sans erreur
- ✅ `/validate-docs` 100% OK
- ✅ `/check-links` 0 lien cassé
- ✅ @content-reviewer score ≥ 95%
- ✅ @accessibility-checker WCAG AA conforme
- ✅ Lighthouse Accessibility ≥ 90
- ✅ CI/CD déploiement automatique fonctionnel

## 🆘 Dépannage

### `/serve` ne démarre pas
```bash
# Vérifier installation
pip list | grep mkdocs

# Réinstaller si nécessaire
pip install --upgrade mkdocs-material
```

### `/build` échoue
```bash
# Identifier le problème
/validate-docs

# Vérifier mkdocs.yml
python -m mkdocs build --verbose
```

### Liens cassés après `/check-links`
```bash
# Identifier les liens
/check-links

# Corriger dans les fichiers .md
# Revalider
/check-links
```

## 📚 Ressources

### MkDocs Material
- [Documentation officielle](https://squidfunk.github.io/mkdocs-material/)
- [Guide de référence](https://squidfunk.github.io/mkdocs-material/reference/)
- [Exemples](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)

### Accessibilité
- [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)

### Claude Code
- [Documentation Claude Code](https://docs.anthropic.com/claude/docs)
- [Guide des templates](../../docs/template-guide.md)

## 🔮 Évolutions futures

Améliorations prévues :
- [ ] Agent `@seo-optimizer` pour optimisation SEO
- [ ] Agent `@image-optimizer` pour compression images
- [ ] Commande `/generate-pdf` pour export PDF
- [ ] Commande `/translate` pour support multilingue
- [ ] Templates de guides spécialisés (API, tutoriel, FAQ)

## 🤝 Contribution

Pour améliorer ce template :
1. Tester sur votre projet MkDocs
2. Proposer des améliorations dans IMPROVEMENTS.md
3. Partager vos commandes/agents personnalisés
4. Documenter vos cas d'usage

## 📝 License

Ce template fait partie de claude-env-manager.
Voir LICENSE du projet principal.
