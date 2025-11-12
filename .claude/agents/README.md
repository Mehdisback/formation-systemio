# Agents MkDocs Documentation

Agents spécialisés pour l'optimisation de documentation MkDocs Material.

## 🎯 Agents disponibles

### @content-reviewer
**Spécialité** : Review de contenu français pour public non-technique

**Quand l'utiliser** :
- Après rédaction d'un nouveau guide
- Avant commit de modifications importantes
- Pour uniformiser le ton et le style
- Vérifier la cohérence terminologique

**Compétences** :
- ✍️ Grammaire et orthographe française
- 📝 Rédaction technique vulgarisée
- 🎨 Ton adapté au coaching
- 🔄 Cohérence entre guides

### @accessibility-checker
**Spécialité** : Audit d'accessibilité WCAG 2.1

**Quand l'utiliser** :
- Avant chaque déploiement majeur
- Après modification de styles CSS
- Pour validation conformité légale
- Audit trimestriel de maintenance

**Compétences** :
- ♿ Conformité WCAG 2.1 AA/AAA
- 🎨 Contraste des couleurs
- ⌨️ Navigation au clavier
- 📱 Responsive design

## 🔄 Workflows recommandés

### Création d'un nouveau guide
```
1. /add-guide 11 "Titre"         # Créer le guide
2. Rédiger le contenu
3. @content-reviewer analyze     # Review contenu
4. Appliquer corrections
5. @accessibility-checker audit  # Vérifier accessibilité
6. /validate-docs                # Validation technique
7. Commit
```

### Modification de styles
```
1. Modifier docs/stylesheets/extra.css
2. @accessibility-checker check-contrast
3. Tester avec /serve
4. @accessibility-checker test-responsive
5. Valider avec outils DevTools
6. /build && /deploy
```

### Audit complet de qualité
```
@content-reviewer review-all
@accessibility-checker full-report
/validate-docs --full
/check-links
```

## 📊 Fréquence d'utilisation

| Agent | Fréquence | Durée estimée |
|-------|-----------|---------------|
| @content-reviewer | Par guide créé/modifié | 5-10 min |
| @accessibility-checker | Hebdomadaire | 10-15 min |
| Audit complet | Mensuel | 30-45 min |

## 💡 Complémentarité avec commandes

| Besoin | Outil |
|--------|-------|
| Syntaxe Markdown | `/validate-docs` |
| Contenu français | `@content-reviewer` |
| Accessibilité | `@accessibility-checker` |
| Liens cassés | `/check-links` |
| Preview | `/serve` |

## 🎯 Objectifs de qualité

### Contenu (via @content-reviewer)
- ✅ 100% français correct
- ✅ 0 jargon non expliqué
- ✅ Ton professionnel et bienveillant
- ✅ Cohérence terminologique

### Accessibilité (via @accessibility-checker)
- ✅ WCAG 2.1 AA minimum
- ✅ Contraste ≥ 4.5:1
- ✅ Navigation clavier complète
- ✅ Responsive 320px → 2560px

## 🔧 Personnalisation

### Créer un nouvel agent

1. Créer `nouvel-agent.md` dans ce dossier
2. Suivre la structure des agents existants
3. Ajouter dans `settings.json` :
```json
"agents": {
  "allow": [
    "@content-reviewer",
    "@accessibility-checker",
    "@nouvel-agent"
  ]
}
```
4. Documenter ici

### Modifier un agent existant

1. Éditer le fichier `.md` de l'agent
2. Ajuster les prompts et vérifications
3. Tester avec un cas réel
4. Mettre à jour cette documentation

## 📚 Ressources

### Pour @content-reviewer
- [Guide de style français](https://www.quebec.ca/gouvernement/politiques-orientations/vitrine-linguistique/redaction-communications/modeles-formats-communicationnels/redaction-contenu-web)
- [Écriture inclusive](https://www.ecriture-inclusive.fr/)
- [Vulgarisation technique](https://www.redactiontechnique.com/)

### Pour @accessibility-checker
- [WCAG 2.1](https://www.w3.org/WAI/WCAG21/quickref/)
- [RGAA 4.1](https://www.numerique.gouv.fr/publications/rgaa-accessibilite/)
- [Material Accessibility](https://material.io/design/usability/accessibility.html)
- [WebAIM](https://webaim.org/)

## 🚀 Prochaines étapes

Agents potentiels à créer :
- `@seo-optimizer` - Optimisation SEO des guides
- `@image-optimizer` - Compression et optimisation images
- `@translation-helper` - Assistance traduction multilingue
- `@performance-auditor` - Audit performances site
