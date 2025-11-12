# 📁 Assets - Organisation des médias

Ce dossier contient tous les assets (images, documents, médias) de la documentation.

## 📂 Structure

```
assets/
├── branding/          # Identité visuelle et branding
│   ├── logo.svg       # Logo principal (à créer)
│   ├── logo.png       # Logo PNG (fallback)
│   ├── favicon.png    # Favicon 32x32
│   ├── favicon.ico    # Favicon multi-tailles
│   ├── og-image.png   # Image Open Graph 1200x630px (à créer)
│   └── apple-touch-icon.png  # Icône iOS 180x180
│
├── screenshots/       # Captures d'écran Systeme.io
│   ├── 01-connexion/
│   ├── 02-dashboard/
│   ├── 03-editeur/
│   ├── 04-cta/
│   └── ...
│
├── diagrams/          # Diagrammes et schémas
│   ├── architecture.svg
│   ├── workflow.svg
│   └── ...
│
└── downloads/         # Fichiers téléchargeables
    ├── checklists/
    ├── templates/
    └── pdfs/

```

## 🎨 Guidelines images

### Screenshots Systeme.io

**Format** : PNG ou WebP
**Taille max** : 1920x1080px
**Optimisation** : Compresser avec TinyPNG (70% réduction)
**Annotations** : Flèches rouges, encadrés, textes explicatifs
**Nommage** : `XX-nom-descriptif.png` (ex: `01-bouton-connexion.png`)

**Alt text requis** :
```markdown
![Description précise de ce que montre la capture : action, localisation, éléments importants](chemin/image.png)
```

### Images branding

**Logo** :
- Format vectoriel SVG (prioritaire)
- PNG transparent en fallback
- Dimensions: 200x50px (ratio 4:1)

**Favicon** :
- 32x32px, 16x16px, 48x48px dans .ico
- PNG fallback 32x32px
- Générateur recommandé : [RealFaviconGenerator](https://realfavicongenerator.net/)

**Open Graph image** :
- Dimensions exactes : 1200x630px
- Format : PNG ou JPG
- Poids max : 300 KB
- Contenu : Titre + sous-titre + branding

## 📝 Checklist avant ajout image

- [ ] Image optimisée (TinyPNG ou ImageOptim)
- [ ] Format adapté (WebP > PNG > JPG)
- [ ] Taille raisonnable (< 500 KB par image)
- [ ] Alt text descriptif rédigé
- [ ] Nom de fichier explicite (kebab-case)
- [ ] Responsive testé (320px → 2560px)

## 🔗 Liens utiles

- [TinyPNG](https://tinypng.com/) - Compression images
- [Squoosh](https://squoosh.app/) - Conversion WebP
- [RealFaviconGenerator](https://realfavicongenerator.net/) - Générer favicons
- [Canva](https://canva.com/) - Créer visuels Open Graph
- [SVGOMG](https://jakearchibald.github.io/svgomg/) - Optimiser SVG

## 📊 Status actuel

- [x] Structure créée
- [ ] Logo créé (TODO)
- [ ] Favicon généré (TODO)
- [ ] OG image créée (TODO)
- [ ] Screenshots ajoutés (0/25 TODO)
- [ ] Diagrammes créés (TODO)
- [ ] PDFs téléchargeables (TODO)
