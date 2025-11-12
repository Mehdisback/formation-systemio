# `/check-links`

Vérifie tous les liens (internes et externes) dans la documentation.

```
/check-links [--external-only]
```

## Ce que fait cette commande
1. Scanne tous les fichiers Markdown
2. Extrait tous les liens
3. Vérifie les liens internes (fichiers, anchors)
4. Teste les liens externes (HTTP status)
5. Génère un rapport détaillé

## Arguments
- `--external-only` (optionnel) : Vérifie uniquement les liens externes

## Exemples
```
/check-links                    # Vérifie tous les liens
/check-links --external-only    # Vérifie seulement les liens externes
```

## Types de liens vérifiés

### Liens internes
- Liens relatifs entre guides (`[Guide suivant](02-GUIDE.md)`)
- Anchors dans le même fichier (`[Section](#ma-section)`)
- Anchors dans d'autres fichiers (`[Section](02-GUIDE.md#section)`)
- Images locales (`![Alt](images/screenshot.png)`)

### Liens externes
- URLs absolues (`https://systeme.io`)
- Liens Calendly
- Liens vers outils externes
- Liens de documentation

## Rapport généré
```
🔗 Vérification des liens - [Date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Statistiques:
- Fichiers scannés : 10
- Liens internes : 42 ✅
- Liens externes : 18 (15 ✅, 3 ⚠️)
- Images : 25 ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️  Problèmes détectés:

Liens externes cassés:
1. docs/06-SEO-REFERENCEMENT.md:78
   URL: https://example.com/tool
   Erreur: 404 Not Found

2. docs/09-FAQ-TROUBLESHOOTING.md:142
   URL: https://systeme.io/docs/old-feature
   Erreur: 301 Moved Permanently
   → Redirection vers: https://systeme.io/docs/new-feature

3. docs/03-GESTION-CTA-CALENDLY.md:56
   URL: https://calendly.com/invalid
   Erreur: Timeout (> 5s)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Actions recommandées:
1. Mettre à jour les URLs redirigées
2. Supprimer ou remplacer les liens 404
3. Vérifier manuellement les timeouts
```

## Codes de statut HTTP

| Code | Signification | Action |
|------|---------------|--------|
| 200 | ✅ OK | Rien à faire |
| 301 | ⚠️ Redirection permanente | Mettre à jour l'URL |
| 302 | ⚠️ Redirection temporaire | Surveiller |
| 404 | ❌ Non trouvé | Corriger ou supprimer |
| 403 | ❌ Accès refusé | Vérifier permissions |
| 500 | ❌ Erreur serveur | Réessayer plus tard |

## Conseils
- Lancez cette vérification hebdomadairement
- Les liens externes peuvent changer sans préavis
- Conservez une liste de liens critiques
- Utilisez des versions archivées pour docs importantes
- Privilégiez les liens vers documentation officielle

## Exclusions
Certains liens sont volontairement ignorés :
- Exemples de syntaxe (`https://example.com`)
- Placeholders dans templates
- Liens vers localhost
- URLs de développement

## Performances
- Vérification rapide : ~5 secondes (liens internes)
- Vérification complète : ~30 secondes (avec externes)
- Timeout par URL : 5 secondes
- Parallélisation : 10 requêtes simultanées
