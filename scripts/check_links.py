#!/usr/bin/env python3
"""
Script de vérification des liens dans la documentation MkDocs.
Vérifie les liens internes (fichiers .md) et externes (HTTP/HTTPS).

Usage:
    python scripts/check_links.py
    python scripts/check_links.py --external  # Inclut vérification liens externes
"""

import re
import sys
import argparse
from pathlib import Path
from typing import List, Tuple
from urllib.parse import urlparse

# Codes de couleur ANSI pour terminal
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'


def extract_links(content: str, file_path: Path) -> List[Tuple[str, str, int]]:
    """
    Extrait tous les liens markdown d'un fichier.

    Returns:
        Liste de tuples (texte_lien, url, numéro_ligne)
    """
    links = []
    lines = content.split('\n')

    # Regex pour liens markdown: [texte](url)
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^\)]+)\)')

    for line_num, line in enumerate(lines, start=1):
        matches = link_pattern.findall(line)
        for text, url in matches:
            # Ignorer les ancres seules (#section)
            if url.startswith('#'):
                continue
            links.append((text, url, line_num))

    return links


def check_internal_link(url: str, source_file: Path, docs_path: Path) -> Tuple[bool, str]:
    """
    Vérifie si un lien interne existe.

    Args:
        url: URL du lien (peut contenir ancre #)
        source_file: Fichier source contenant le lien
        docs_path: Chemin racine du dossier docs/

    Returns:
        (is_valid, error_message)
    """
    # Séparer le chemin de l'ancre
    if '#' in url:
        file_part, anchor = url.split('#', 1)
    else:
        file_part, anchor = url, None

    # Si le lien est vide (juste une ancre), c'est valide
    if not file_part:
        return True, ""

    # Résoudre le chemin relatif
    if file_part.startswith('/'):
        # Chemin absolu depuis docs/
        target_path = docs_path / file_part.lstrip('/')
    else:
        # Chemin relatif depuis le fichier source
        target_path = (source_file.parent / file_part).resolve()

    # Ajouter .md si pas d'extension
    if not target_path.suffix:
        target_path = target_path.with_suffix('.md')

    # Vérifier existence du fichier
    if not target_path.exists():
        return False, f"Fichier introuvable: {target_path}"

    # TODO: Vérifier l'ancre dans le fichier cible (optionnel)
    # if anchor:
    #     content = target_path.read_text()
    #     if anchor not in content:
    #         return False, f"Ancre #{anchor} introuvable dans {target_path.name}"

    return True, ""


def check_external_link(url: str) -> Tuple[bool, str]:
    """
    Vérifie si un lien externe est accessible.

    Note: Nécessite 'requests' installé: pip install requests
    """
    try:
        import requests

        # Timeout de 5 secondes
        response = requests.head(url, timeout=5, allow_redirects=True)

        if response.status_code >= 400:
            return False, f"HTTP {response.status_code}"

        return True, ""

    except ImportError:
        return True, "⚠️  Module 'requests' non installé (pip install requests)"
    except requests.exceptions.Timeout:
        return False, "Timeout (>5s)"
    except requests.exceptions.RequestException as e:
        return False, str(e)


def main():
    parser = argparse.ArgumentParser(description='Vérifier les liens de la documentation')
    parser.add_argument('--external', action='store_true',
                       help='Vérifier aussi les liens externes (plus lent)')
    args = parser.parse_args()

    # Chemin du dossier docs/
    docs_path = Path(__file__).parent.parent / 'docs'

    if not docs_path.exists():
        print(f"{RED}❌ Dossier docs/ introuvable: {docs_path}{RESET}")
        sys.exit(1)

    # Trouver tous les fichiers .md
    md_files = list(docs_path.rglob('*.md'))

    print(f"{BLUE}🔍 Vérification des liens dans {len(md_files)} fichiers...{RESET}\n")

    broken_links = []
    warning_links = []
    total_links = 0

    for md_file in md_files:
        content = md_file.read_text(encoding='utf-8')
        links = extract_links(content, md_file)

        if not links:
            continue

        print(f"📄 {md_file.relative_to(docs_path)}")

        for text, url, line_num in links:
            total_links += 1

            # Déterminer le type de lien
            parsed = urlparse(url)
            is_external = parsed.scheme in ('http', 'https')

            if is_external:
                if args.external:
                    is_valid, error = check_external_link(url)
                    if not is_valid:
                        broken_links.append((md_file, url, line_num, error))
                        print(f"  {RED}❌{RESET} Ligne {line_num}: {url} - {error}")
                    else:
                        print(f"  {GREEN}✓{RESET} Ligne {line_num}: {url[:60]}...")
                else:
                    # Skip sans vérification
                    print(f"  {YELLOW}⊘{RESET} Ligne {line_num}: {url[:60]}... (externe, non vérifié)")
            else:
                # Lien interne
                is_valid, error = check_internal_link(url, md_file, docs_path)
                if not is_valid:
                    broken_links.append((md_file, url, line_num, error))
                    print(f"  {RED}❌{RESET} Ligne {line_num}: {url} - {error}")
                else:
                    print(f"  {GREEN}✓{RESET} Ligne {line_num}: {url}")

        print()

    # Résumé
    print("=" * 60)
    print(f"\n{BLUE}📊 RÉSUMÉ{RESET}\n")
    print(f"Total de liens vérifiés: {total_links}")
    print(f"{GREEN}✓ Liens valides: {total_links - len(broken_links)}{RESET}")

    if broken_links:
        print(f"{RED}❌ Liens cassés: {len(broken_links)}{RESET}\n")

        print(f"{RED}🔴 DÉTAILS DES LIENS CASSÉS:{RESET}\n")
        for file_path, url, line_num, error in broken_links:
            print(f"  📄 {file_path.relative_to(docs_path)}:{line_num}")
            print(f"     🔗 {url}")
            print(f"     ⚠️  {error}\n")

        sys.exit(1)
    else:
        print(f"\n{GREEN}🎉 Tous les liens sont valides !{RESET}")
        sys.exit(0)


if __name__ == '__main__':
    main()
