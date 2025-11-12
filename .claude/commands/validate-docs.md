# `/validate-docs`

Valide l'intégrité et la qualité de la documentation.

```
/validate-docs [--full]
```

## Ce que fait cette commande
1. ✅ Vérifie la syntaxe Markdown
2. ✅ Valide les liens internes
3. ✅ Contrôle la cohérence de navigation
4. ✅ Vérifie les admonitions
5. ✅ Teste la configuration MkDocs
6. ✅ Analyse le français (grammaire basique)

## Arguments
- `--full` (optionnel) : Validation exhaustive avec vérification des liens externes

## Exemples
```
/validate-docs           # Validation standard
/validate-docs --full    # Validation complète avec liens externes
```

## Vérifications effectuées

### Structure
- [x] Tous les guides sont numérotés correctement
- [x] Fichiers suivent la convention de nommage `XX-NOM-GUIDE.md`
- [x] Navigation dans `mkdocs.yml` est cohérente
- [x] Emojis présents dans les titres

### Contenu
- [x] Syntaxe Markdown valide
- [x] Admonitions bien formatées (tip, warning, info, danger)
- [x] Checklists avec syntaxe correcte
- [x] Blocs de code avec langage spécifié

### Liens
- [x] Liens internes pointent vers fichiers existants
- [x] Anchors dans liens sont valides
- [x] Pas de liens cassés
- [x] Navigation précédent/suivant cohérente

### Langue française
- [x] Pas de texte en anglais (sauf termes techniques)
- [x] Guillemets français « » utilisés
- [x] Ponctuation correcte
- [x] Ton adapté au public non-technique

### Accessibilité
- [x] Images ont un texte alternatif
- [x] Titres hiérarchiques (pas de saut de niveau)
- [x] Contraste suffisant dans les styles
- [x] Liens descriptifs (pas "cliquez ici")

## Rapport généré
```
📊 Rapport de validation - [Date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Structure : OK
✅ Contenu : OK
⚠️  Liens : 2 warnings
✅ Langue : OK
✅ Accessibilité : OK

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Détails des warnings:
- docs/05-FORMULAIRES-DONNEES.md:42 : Lien externe sans https
- docs/08-MAINTENANCE-BONNES-PRATIQUES.md:15 : Anchor #section-2 non trouvé

Recommandations:
1. Corriger les 2 liens identifiés
2. Relancer /validate-docs pour confirmation
```

## Conseils
- Lancez cette commande avant chaque commit
- Corrigez tous les warnings avant déploiement
- Utilisez avec `/build` pour validation complète
- Conservez les rapports dans `.claude/reports/`

## Intégration CI/CD
Cette commande peut être ajoutée au workflow GitHub Actions :
```yaml
- name: Validate documentation
  run: mkdocs build --strict
```
