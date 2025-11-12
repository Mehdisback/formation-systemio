# 🎨 Spécifications Image Open Graph

## 📐 Dimensions et format

- **Taille** : 1200 x 630 pixels (ratio 1.91:1)
- **Format** : PNG ou JPG
- **Poids max** : 300 KB
- **Fond** : Gradient indigo → purple (cohérent avec le site)

## 🎨 Contenu à inclure

### Texte principal
```
Formation Systeme.io
L'Essentiel en Soi
```

### Sous-titre
```
10 guides pratiques pour maîtriser votre landing page
Coaching au Féminin • 5 heures • Public non-technique
```

### Éléments visuels
- Logo A-Tek Universe (coin inférieur droit)
- Icônes : 📚 💻 🎯
- Gradient de fond : `linear-gradient(135deg, #3949AB 0%, #7E57C2 100%)`

## 🎨 Palette de couleurs

```css
/* À utiliser dans Canva ou Figma */
Indigo primary: #3949AB
Deep Purple accent: #7E57C2
Blanc texte: #FFFFFF
Ombre texte: rgba(0, 0, 0, 0.3)
```

## 📝 Typographie

- **Titre** : Police Roboto ou Inter, Bold, 72px
- **Sous-titre** : Police Inter, Regular, 32px
- **Alignement** : Centré vertical et horizontal

## 🛠️ Outils recommandés

### Canva (Gratuit et facile)
1. Créer un design personnalisé 1200x630px
2. Ajouter fond gradient (utiliser couleurs ci-dessus)
3. Ajouter textes avec police Roboto Bold
4. Exporter en PNG haute qualité

### Figma (Professionnel)
1. Créer frame 1200x630px
2. Ajouter rectangle avec gradient
3. Ajouter textes et icônes
4. Exporter PNG @2x pour netteté

### Photoshop
1. Nouveau document 1200x630px, 72 DPI
2. Gradient Overlay avec couleurs indigo → purple
3. Textes avec Roboto Bold
4. Exporter pour Web (PNG-24)

## ✅ Checklist avant export

- [ ] Dimensions exactes 1200x630px
- [ ] Texte lisible même en miniature
- [ ] Contraste suffisant (texte blanc sur fond sombre)
- [ ] Pas de texte coupé sur les bords
- [ ] Logo visible mais discret
- [ ] Poids < 300 KB
- [ ] Testé sur Facebook Debugger et Twitter Card Validator

## 🔗 Validation

Après création et upload, tester avec :

- **Facebook Sharing Debugger** : https://developers.facebook.com/tools/debug/
- **Twitter Card Validator** : https://cards-dev.twitter.com/validator
- **LinkedIn Post Inspector** : https://www.linkedin.com/post-inspector/

## 📄 Template Canva

Vous pouvez utiliser ce template prêt à l'emploi :
https://www.canva.com/design/DAFxxxxx/edit (TODO: créer template et ajouter lien)

## 💡 Exemple de rendu attendu

```
┌────────────────────────────────────────────────┐
│                                                │
│      FORMATION SYSTEME.IO                      │
│      L'Essentiel en Soi                        │
│                                                │
│   10 guides pratiques pour maîtriser          │
│        votre landing page                      │
│                                                │
│   📚 Coaching au Féminin • 💻 5h • 🎯         │
│              Public non-technique              │
│                                                │
│                          [Logo A-Tek] ⚡       │
└────────────────────────────────────────────────┘
```

---

**Note** : Une fois l'image créée, la placer dans ce dossier avec le nom `og-image.png`
