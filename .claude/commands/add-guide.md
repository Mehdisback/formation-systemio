# `/add-guide`

Crée un nouveau guide de formation avec le template approprié.

```
/add-guide <numero> <titre>
```

## Ce que fait cette commande
1. Crée un nouveau fichier `.md` dans `docs/`
2. Applique le template standard avec structure
3. Met à jour `mkdocs.yml` avec la navigation
4. Configure l'emoji et le numéro appropriés

## Arguments
- `numero` : Numéro du guide (ex: 11)
- `titre` : Titre du guide (ex: "Configuration avancée")

## Exemples
```
/add-guide 11 "Configuration avancée"
/add-guide 12 "Intégrations externes"
```

## Structure générée
Le nouveau guide contient :
- 📋 Entête avec emoji et titre
- ⏱️ Durée estimée et niveau
- 🎯 Objectifs d'apprentissage
- 📝 Sections de contenu
- ✅ Checklist de validation
- 🔗 Liens vers guides précédent/suivant

## Après création
1. Éditer le contenu du guide
2. Ajuster la durée estimée
3. Définir le niveau de difficulté
4. Ajouter les captures d'écran si nécessaire
5. Tester avec `/serve`
6. Valider avec `/validate-docs`

## Template de guide
```markdown
# 🎯 [Numéro] - [Titre]

⏱️ **Durée estimée** : [X] minutes
📊 **Niveau** : [Débutant/Intermédiaire/Avancé]

## 🎯 Objectifs

À la fin de ce guide, vous saurez :

- [ ] Objectif 1
- [ ] Objectif 2
- [ ] Objectif 3

## 📝 Contenu

### Section 1

!!! tip "Conseil"
    Votre conseil ici

### Section 2

!!! warning "Attention"
    Votre avertissement ici

## ✅ Checklist de validation

- [ ] Action 1 effectuée
- [ ] Action 2 effectuée

## 🔗 Navigation

- ⬅️ [Guide précédent](XX-GUIDE-PRECEDENT.md)
- ➡️ [Guide suivant](XX-GUIDE-SUIVANT.md)
```

## Bonnes pratiques
- 📝 Utilisez un français clair et simple
- 🎨 Ajoutez des emojis pour la lisibilité
- 📸 Incluez des captures d'écran annotées
- ⚠️ Utilisez les admonitions (tip, warning, info, danger)
- 🔗 Créez des liens internes entre guides
