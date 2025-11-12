#!/usr/bin/env python3
"""
Script de diagnostic Google Analytics
Vérifie que GA4 est correctement configuré dans MkDocs
"""

import re
from pathlib import Path

CONFIG_FILE = Path("mkdocs.yml")

print("🔍 Diagnostic Google Analytics - MkDocs Material\n")

# Lire mkdocs.yml comme texte brut (évite les problèmes avec les tags YAML personnalisés de Material)
try:
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
except Exception as e:
    print(f"❌ Erreur lecture mkdocs.yml : {e}")
    exit(1)

# Vérifier la présence de analytics avec regex
has_analytics = False
ga_id = None
provider = None

# Rechercher la section extra.analytics (Material 9.x)
analytics_section = re.search(r'extra:\s*\n.*?analytics:\s*\n(.*?)(?=\n\S|\Z)', content, re.DOTALL)

if analytics_section:
    has_analytics = True
    analytics_block = analytics_section.group(1)

    print("✅ Section 'extra.analytics' trouvée")

    # Extraire provider
    provider_match = re.search(r'provider:\s*(\S+)', analytics_block)
    if provider_match:
        provider = provider_match.group(1)
        print(f"   Provider : {provider}")
    else:
        print("   Provider : NON DÉFINI")

    # Extraire property (ID GA4)
    property_match = re.search(r'property:\s*(\S+)', analytics_block)
    if property_match:
        ga_id = property_match.group(1)
        print(f"   Property : {ga_id}")

        if ga_id == 'G-XXXXXXXXXX':
            print("   ⚠️  ID placeholder détecté - Remplacer par vrai ID GA4")
        elif ga_id.startswith('G-'):
            print("   ✅ ID GA4 valide détecté")
        elif ga_id.startswith('UA-'):
            print("   ❌ ID Universal Analytics (UA-) détecté - Utiliser GA4 (G-)")
        else:
            print("   ❌ ID GA4 invalide")
    else:
        print("   Property : NON DÉFINI")
        print("   ❌ ID GA4 manquant")

# Vérifier ancienne syntaxe (Material < 9.0)
old_analytics = re.search(r'google_analytics:\s*\n\s*-\s*(\S+)', content)
if old_analytics:
    print("\n⚠️  Ancienne syntaxe 'google_analytics' trouvée")
    print("   Migrer vers 'extra.analytics' pour Material 9.x+")
    print(f"   ID détecté : {old_analytics.group(1)}")

if not has_analytics and not old_analytics:
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
extra_js = re.findall(r'extra_javascript:\s*\n((?:\s*-\s*[^\n]+\n)+)', content)
if extra_js:
    scripts = re.findall(r'-\s*([^\n]+)', extra_js[0])
    for script in scripts:
        script = script.strip()
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
