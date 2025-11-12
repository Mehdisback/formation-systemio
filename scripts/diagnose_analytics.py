#!/usr/bin/env python3
"""
Script de diagnostic Google Analytics
Vérifie que GA4 est correctement configuré dans MkDocs
"""

import yaml
from pathlib import Path

CONFIG_FILE = Path("mkdocs.yml")

print("🔍 Diagnostic Google Analytics - MkDocs Material\n")

# Lire mkdocs.yml
try:
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
except Exception as e:
    print(f"❌ Erreur lecture mkdocs.yml : {e}")
    exit(1)

# Vérifier la présence de analytics
has_analytics = False
ga_id = None

# Vérifier nouvelle syntaxe (Material 9.x)
if 'extra' in config and 'analytics' in config['extra']:
    has_analytics = True
    analytics = config['extra']['analytics']

    print("✅ Section 'extra.analytics' trouvée")
    print(f"   Provider : {analytics.get('provider', 'NON DÉFINI')}")

    ga_id = analytics.get('property')
    print(f"   Property : {ga_id}")

    if ga_id == 'G-XXXXXXXXXX':
        print("   ⚠️  ID placeholder détecté - Remplacer par vrai ID GA4")
    elif ga_id and ga_id.startswith('G-'):
        print("   ✅ ID GA4 valide détecté")
    elif ga_id and ga_id.startswith('UA-'):
        print("   ❌ ID Universal Analytics (UA-) détecté - Utiliser GA4 (G-)")
    else:
        print("   ❌ ID GA4 invalide ou manquant")

# Vérifier ancienne syntaxe (Material < 9.0)
if 'google_analytics' in config:
    print("\n⚠️  Ancienne syntaxe 'google_analytics' trouvée")
    print("   Migrer vers 'extra.analytics' pour Material 9.x+")

    old_ga = config['google_analytics']
    if isinstance(old_ga, list) and len(old_ga) > 0:
        print(f"   ID détecté : {old_ga[0]}")

if not has_analytics and 'google_analytics' not in config:
    print("❌ Aucune configuration Google Analytics trouvée")
    print("   Ajouter dans mkdocs.yml :")
    print("""
extra:
  analytics:
    provider: google
    property: G-VOTRE-ID
""")

# Vérifier extra_javascript
print("\n📜 Scripts JavaScript personnalisés :")
if 'extra_javascript' in config:
    for script in config['extra_javascript']:
        print(f"   - {script}")
        if 'analytics' in script:
            print("     ✅ Script analytics détecté")
else:
    print("   ℹ️  Aucun script personnalisé")

# Vérifier version Material (si requirements.txt existe)
print("\n📦 Vérification dépendances :")
req_file = Path("requirements.txt")
if req_file.exists():
    content = req_file.read_text()
    for line in content.split('\n'):
        if 'mkdocs-material' in line.lower():
            print(f"   {line.strip()}")
else:
    print("   ⚠️  requirements.txt non trouvé")

# Recommandations
print("\n💡 Recommandations :")

if ga_id == 'G-XXXXXXXXXX':
    print("   1. Remplacer G-XXXXXXXXXX par votre vrai ID GA4")
    print("   2. Obtenir un ID : https://analytics.google.com")

if ga_id and ga_id.startswith('G-') and ga_id != 'G-XXXXXXXXXX':
    print("   1. ID GA4 semble valide")
    print("   2. Vérifier que le site est déployé (pas localhost)")
    print("   3. Désactiver bloqueurs de pub pour tester")
    print("   4. Attendre 5-10 secondes après chargement page")
    print("   5. Vérifier console : [Analytics] ✅ gtag chargé")

print("\n🧪 Test après déploiement :")
print("   1. mkdocs build")
print("   2. grep -r 'googletagmanager' site/index.html")
print("   3. Si vide : Material ne charge pas GA4")
print("   4. Vérifier version Material ≥ 9.0.0")

print("\n✅ Diagnostic terminé")
