# Boutons de partage social

## Utilisation

Pour ajouter des boutons de partage à la fin d'un guide, copiez-collez le code HTML suivant :

```html
<div class="share-buttons">
  <span class="share-buttons-title">Partager ce guide</span>
  <a href="https://twitter.com/intent/tweet?url=https://mehdisback.github.io/formation-systemio/XX-VOTRE-GUIDE/&text=Formation%20Systeme.io%20-%20[TITRE DU GUIDE]" class="share-button twitter" target="_blank" rel="noopener noreferrer">
    🐦 Twitter
  </a>
  <a href="https://www.facebook.com/sharer/sharer.php?u=https://mehdisback.github.io/formation-systemio/XX-VOTRE-GUIDE/" class="share-button facebook" target="_blank" rel="noopener noreferrer">
    📘 Facebook
  </a>
  <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://mehdisback.github.io/formation-systemio/XX-VOTRE-GUIDE/" class="share-button linkedin" target="_blank" rel="noopener noreferrer">
    💼 LinkedIn
  </a>
  <a href="mailto:?subject=Formation%20Systeme.io%20-%20[TITRE]&body=Je%20partage%20avec%20toi%20ce%20guide%20:%20https://mehdisback.github.io/formation-systemio/XX-VOTRE-GUIDE/" class="share-button email">
    ✉️ Email
  </a>
</div>
```

## Personnalisation

Remplacez :
- `XX-VOTRE-GUIDE` par le nom du fichier (ex: `01-GUIDE-DEMARRAGE-RAPIDE`)
- `[TITRE DU GUIDE]` par le titre complet

## Exemple concret

Pour le guide de démarrage rapide :

```html
<div class="share-buttons">
  <span class="share-buttons-title">Partager ce guide</span>
  <a href="https://twitter.com/intent/tweet?url=https://mehdisback.github.io/formation-systemio/01-GUIDE-DEMARRAGE-RAPIDE/&text=Formation%20Systeme.io%20-%20Guide%20de%20Démarrage%20Rapide" class="share-button twitter" target="_blank" rel="noopener noreferrer">
    🐦 Twitter
  </a>
  <a href="https://www.facebook.com/sharer/sharer.php?u=https://mehdisback.github.io/formation-systemio/01-GUIDE-DEMARRAGE-RAPIDE/" class="share-button facebook" target="_blank" rel="noopener noreferrer">
    📘 Facebook
  </a>
  <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://mehdisback.github.io/formation-systemio/01-GUIDE-DEMARRAGE-RAPIDE/" class="share-button linkedin" target="_blank" rel="noopener noreferrer">
    💼 LinkedIn
  </a>
  <a href="mailto:?subject=Formation%20Systeme.io%20-%20Guide%20de%20Démarrage%20Rapide&body=Je%20partage%20avec%20toi%20ce%20guide%20:%20https://mehdisback.github.io/formation-systemio/01-GUIDE-DEMARRAGE-RAPIDE/" class="share-button email">
    ✉️ Email
  </a>
</div>
```

## Position recommandée

Placez ce code juste avant la section "🔗 Navigation" à la fin de chaque guide.
