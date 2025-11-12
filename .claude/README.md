# Configuration Claude Code - MkDocs Documentation

Configuration complète pour projets de documentation MkDocs Material.

## 📁 Structure

```
.claude/
├── settings.json           # Configuration principale
├── CHANGELOG.md            # Historique des modifications
├── README.md               # Ce fichier
├── commands/               # Commandes slash
│   ├── README.md
│   ├── serve.md            # /serve
│   ├── build.md            # /build
│   ├── deploy.md           # /deploy
│   ├── add-guide.md        # /add-guide
│   ├── validate-docs.md    # /validate-docs
│   └── check-links.md      # /check-links
└── agents/                 # Agents spécialisés
    ├── README.md
    ├── content-reviewer.md      # @content-reviewer
    └── accessibility-checker.md # @accessibility-checker
```

## ⚙️ Configuration (settings.json)

### Permissions définies

#### ✅ Autorisées (sans confirmation)
```json
"allow": [
  "Bash(git status:*)",      // Git lecture seule
  "Bash(git diff:*)",
  "Bash(git log:*)",
  "Bash(git branch:*)",
  "Bash(mkdocs serve:*)",    // Serveur dev
  "Bash(mkdocs build:*)",    // Build
  "Bash(ls:*)",              // Filesystem lecture
  "Bash(pwd:*)",
  "Bash(cat:*)"
]
```

#### ⚠️ Demandent confirmation
```json
"ask": [
  "Bash(git commit:*)",      // Modifications Git
  "Bash(git push:*)",
  "Bash(mkdocs gh-deploy:*)", // Déploiement
  "Bash(pip install:*)",      // Installation dépendances
  "Bash(mkdir:*)"
]
```

#### ❌ Bloquées
```json
"deny": [
  "Bash(rm -rf:*)",           // Suppressions destructives
  "Bash(git push --force:*)", // Force push
  "Bash(git reset --hard:*)"  // Reset dangereux
]
```

### Agents autorisés
```json
"agents": {
  "allow": [
    "@content-reviewer",      // Review contenu français
    "@accessibility-checker", // Audit accessibilité
    "@documentation-writer"   // Rédaction documentation
  ]
}
```

### Auto-compact
```json
"contextWindow": {
  "autoCompact": true,        // Activé
  "compactThreshold": 0.95    // À 95% du contexte
}
```

### Références prioritaires
```json
"references": [
  "mkdocs.yml",               // Config MkDocs
  "docs/",                    // Contenu documentation
  "docs/stylesheets/extra.css", // Styles custom
  ".github/workflows/ci.yml", // CI/CD
  "CLAUDE.md"                 // Mémoire projet
]
```

## 🎯 Commandes disponibles

### Développement
| Commande | Description | Confirmation |
|----------|-------------|--------------|
| `/serve` | Serveur dev + live reload | Non |
| `/build` | Build documentation | Non |

### Déploiement
| Commande | Description | Confirmation |
|----------|-------------|--------------|
| `/deploy` | Deploy GitHub Pages | **Oui** |

### Gestion contenu
| Commande | Description | Confirmation |
|----------|-------------|--------------|
| `/add-guide` | Créer nouveau guide | Non |
| `/validate-docs` | Valider documentation | Non |
| `/check-links` | Vérifier liens | Non |

## 🤖 Agents spécialisés

### @content-reviewer
**Expertise** : Contenu français pour public non-technique

**Quand l'utiliser** :
- Après rédaction de nouveau guide
- Pour uniformiser le ton
- Vérifier cohérence terminologique
- Review avant publication

**Compétences** :
- Grammaire et orthographe française
- Vulgarisation technique
- Ton adapté coaching/formation
- Utilisation appropriée admonitions

### @accessibility-checker
**Expertise** : Accessibilité WCAG 2.1 AA/AAA

**Quand l'utiliser** :
- Avant déploiement majeur
- Après modification CSS
- Audit trimestriel
- Validation conformité légale

**Compétences** :
- Conformité WCAG 2.1
- Contraste des couleurs
- Navigation au clavier
- Responsive design
- Alternatives textuelles

## 🔄 Workflows recommandés

### Édition quotidienne
```
/serve                      # Démarrer une fois
# Éditer .md dans docs/
# Vérifier dans navigateur
/validate-docs              # Avant commit
git commit && push
```

### Création de guide
```
/add-guide 11 "Titre"       # Créer avec template
# Rédiger contenu
@content-reviewer analyze   # Review contenu
/serve                      # Prévisualiser
/validate-docs              # Valider
```

### Maintenance périodique
```
/check-links                # Hebdomadaire
@content-reviewer review-all         # Mensuel
@accessibility-checker full-report   # Trimestriel
```

## 🎨 Personnalisation

### Ajouter une commande

1. **Créer le fichier**
```bash
touch .claude/commands/ma-commande.md
```

2. **Structure du fichier**
```markdown
# `/ma-commande`

Description courte de la commande.

## Ce que fait cette commande
1. Étape 1
2. Étape 2

## Exemples
\```
/ma-commande arg1 arg2
\```

## Conseils
- Conseil 1
- Conseil 2
```

3. **Tester**
```
/ma-commande
```

4. **Documenter**
Ajouter dans `commands/README.md`

### Créer un agent

1. **Créer le fichier**
```bash
touch .claude/agents/mon-agent.md
```

2. **Structure de l'agent**
```markdown
# Agent: @mon-agent

Spécialiste de [domaine].

## 🎯 Mission
Description de la mission

## 📋 Domaines d'expertise
- Expertise 1
- Expertise 2

## 🔍 Ce que cet agent vérifie
- [ ] Vérification 1
- [ ] Vérification 2

## 🔧 Invocation
\```
@mon-agent commande args
\```
```

3. **Ajouter dans settings.json**
```json
"agents": {
  "allow": [
    "@content-reviewer",
    "@accessibility-checker",
    "@mon-agent"
  ]
}
```

4. **Tester**
```
@mon-agent test
```

### Modifier les permissions

Éditer `settings.json` :

**Autoriser une nouvelle commande :**
```json
"allow": [
  "Bash(nouvelle-commande:*)"
]
```

**Demander confirmation :**
```json
"ask": [
  "Bash(commande-sensible:*)"
]
```

**Bloquer une commande :**
```json
"deny": [
  "Bash(commande-dangereuse:*)"
]
```

### Ajuster les références

Pour optimiser le contexte Claude Code :

```json
"references": [
  "fichier-important.md",
  "dossier-clé/",
  "config-specifique.yml"
]
```

**Bonnes pratiques** :
- Lister fichiers fréquemment consultés
- Éviter fichiers volumineux (> 1000 lignes)
- Privilégier fichiers de configuration
- Documenter pourquoi chaque référence

## 🔧 Maintenance

### Vérifier la configuration
```bash
# Valider settings.json (syntaxe JSON)
jq . .claude/settings.json

# Lister les commandes disponibles
ls .claude/commands/*.md

# Lister les agents disponibles
ls .claude/agents/*.md
```

### Nettoyer le contexte
Si la session devient lourde :
```
/compact              # Manuel
# ou automatique à 95% (configuré dans settings.json)
```

### Mettre à jour le template
```bash
# Sauvegarder votre config
cp .claude/settings.json .claude/settings.json.backup

# Copier nouvelle version du template
cp -r /path/to/template/.claude/ .

# Restaurer vos customisations
# Merger settings.json.backup dans settings.json
```

## 📊 Métriques de santé

### Configuration optimale
- ✅ settings.json valide (test avec `jq`)
- ✅ 4-8 commandes slash (pas trop, pas trop peu)
- ✅ 2-4 agents spécialisés
- ✅ Permissions cohérentes avec projet
- ✅ Auto-compact activé
- ✅ Références ciblées (< 10 fichiers/dossiers)

### Signes d'une config saine
- Commandes utilisées régulièrement
- Agents invoqués pour tâches complexes
- Pas de blocage intempestif
- Contexte reste gérable (< 40k tokens)
- Workflows fluides et répétables

### Signaux d'alerte
- ⚠️ Trop de commandes (> 15) → Complexité
- ⚠️ Aucun agent → Sous-utilisation
- ⚠️ Permissions trop restrictives → Blocages
- ⚠️ Références trop larges → Contexte gonflé
- ⚠️ Commandes jamais utilisées → Nettoyer

## 🆘 Dépannage

### Commande ne fonctionne pas
```bash
# 1. Vérifier que le fichier existe
ls .claude/commands/ma-commande.md

# 2. Vérifier le contenu
cat .claude/commands/ma-commande.md

# 3. Tester directement
/ma-commande
```

### Agent ne se déclenche pas
```bash
# 1. Vérifier fichier agent
ls .claude/agents/mon-agent.md

# 2. Vérifier permissions dans settings.json
jq '.agents.allow' .claude/settings.json

# 3. Invoquer explicitement
@mon-agent test
```

### settings.json invalide
```bash
# Valider syntaxe JSON
jq . .claude/settings.json

# Si erreur, corriger et revalider
# Restaurer backup si nécessaire
cp .claude/settings.json.backup .claude/settings.json
```

### Contexte saturé
```
# Option 1 : Compact manuel
/compact

# Option 2 : Nouvelle session
# Relancer Claude Code

# Option 3 : Réduire références
# Éditer settings.json → "references"
```

## 📚 Ressources

### Documentation officielle
- [Claude Code Settings](https://docs.anthropic.com/claude/docs/settings)
- [Slash Commands](https://docs.anthropic.com/claude/docs/commands)
- [Agents](https://docs.anthropic.com/claude/docs/agents)

### Templates connexes
- [Base Template](../base/README.md)
- [Marketplace Template](../marketplace/README.md)

### Communauté
- [Issues GitHub](https://github.com/Mehdisback/Claude-test/issues)
- [Discussions](https://github.com/Mehdisback/Claude-test/discussions)

## 🔄 Changelog

Voir [CHANGELOG.md](CHANGELOG.md) pour l'historique complet des modifications.

## 💡 Conseils d'utilisation

### Pour débuter
1. Utilisez les commandes existantes sans modification
2. Invoquez les agents pour comprendre leur fonctionnement
3. Lisez les README des commandes et agents
4. Personnalisez progressivement selon vos besoins

### Pour utilisateurs avancés
1. Créez des commandes pour vos workflows répétitifs
2. Développez des agents pour votre domaine spécifique
3. Optimisez les permissions selon votre sécurité
4. Partagez vos améliorations avec la communauté

### Discipline de tokens
- Privilégier commandes pour workflows standards
- Réserver agents pour analyses approfondies
- Maintenir références ciblées
- Nettoyer commandes inutilisées
- Documenter externes plutôt que dupliquer dans contexte

---

**Version** : 1.0.0
**Dernière mise à jour** : 2024-01-XX
**Compatibilité** : Claude Code ≥ 1.0.0, MkDocs Material ≥ 9.0.0
