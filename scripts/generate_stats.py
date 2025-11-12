#!/usr/bin/env python3
"""
Script de génération de statistiques pour Formation Systeme.io

Génère :
- Nombre total de pages/guides
- Nombre de mots total et par page
- Temps de lecture estimé
- Couverture des assets (images, screenshots)
- Statistiques de documentation

Usage :
    python scripts/generate_stats.py
    python scripts/generate_stats.py --export stats.json
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List
from datetime import datetime

# Configuration
DOCS_DIR = Path("docs")
WORDS_PER_MINUTE = 200  # Vitesse de lecture moyenne (français)


class DocumentationStats:
    """Générateur de statistiques pour documentation MkDocs"""

    def __init__(self):
        self.pages = []
        self.total_words = 0
        self.total_lines = 0
        self.total_code_blocks = 0
        self.total_images = 0
        self.total_links = 0
        self.total_admonitions = 0

    def count_words(self, text: str) -> int:
        """Compte les mots dans un texte (hors code et frontmatter)"""
        # Retirer le frontmatter
        text = re.sub(r'^---.*?---\s*', '', text, flags=re.DOTALL)

        # Retirer les blocs de code
        text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
        text = re.sub(r'`[^`]+`', '', text)

        # Retirer les URLs
        text = re.sub(r'https?://[^\s]+', '', text)

        # Retirer les balises HTML
        text = re.sub(r'<[^>]+>', '', text)

        # Compter les mots (français : lettres, chiffres, tirets, apostrophes)
        words = re.findall(r"[a-zA-ZÀ-ÿ0-9'-]+", text)
        return len(words)

    def analyze_file(self, file_path: Path) -> Dict:
        """Analyse un fichier Markdown et retourne ses statistiques"""
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            return {'error': str(e)}

        # Statistiques de base
        lines = content.split('\n')
        words = self.count_words(content)
        reading_time = words / WORDS_PER_MINUTE

        # Compter les éléments
        code_blocks = len(re.findall(r'```', content)) // 2
        images = len(re.findall(r'!\[.*?\]\(.*?\)', content))
        links = len(re.findall(r'\[.*?\]\(.*?\)', content)) - images
        admonitions = len(re.findall(r'!!! \w+', content))
        headings = len(re.findall(r'^#{1,6} ', content, re.MULTILINE))

        # Extraire le titre
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else file_path.stem

        stats = {
            'file': str(file_path.relative_to(DOCS_DIR)),
            'title': title,
            'lines': len(lines),
            'words': words,
            'reading_time_minutes': round(reading_time, 1),
            'code_blocks': code_blocks,
            'images': images,
            'links': links,
            'admonitions': admonitions,
            'headings': headings,
        }

        # Mettre à jour les totaux
        self.total_words += words
        self.total_lines += len(lines)
        self.total_code_blocks += code_blocks
        self.total_images += images
        self.total_links += links
        self.total_admonitions += admonitions

        return stats

    def scan_directory(self, directory: Path) -> List[Dict]:
        """Scanne tous les fichiers Markdown d'un répertoire"""
        md_files = list(directory.rglob('*.md'))

        # Exclure certains fichiers
        excluded_patterns = ['node_modules', '.venv', 'site', 'snippets']
        md_files = [
            f for f in md_files
            if not any(pattern in str(f) for pattern in excluded_patterns)
        ]

        pages = []
        for file_path in sorted(md_files):
            stats = self.analyze_file(file_path)
            if 'error' not in stats:
                pages.append(stats)
                self.pages.append(stats)

        return pages

    def check_assets_coverage(self) -> Dict:
        """Vérifie la couverture des assets (images, screenshots)"""
        assets_dir = DOCS_DIR / "assets"

        if not assets_dir.exists():
            return {'error': 'Dossier assets/ non trouvé'}

        # Compter les fichiers
        images = list(assets_dir.rglob('*.png')) + \
                 list(assets_dir.rglob('*.jpg')) + \
                 list(assets_dir.rglob('*.jpeg'))

        screenshots_dir = assets_dir / "screenshots"
        screenshots = list(screenshots_dir.rglob('*')) if screenshots_dir.exists() else []

        return {
            'total_images': len(images),
            'screenshots': len(screenshots),
            'assets_size_mb': sum(f.stat().st_size for f in images) / (1024 * 1024)
        }

    def generate_report(self, export_path: str = None):
        """Génère et affiche le rapport de statistiques"""
        print("\n" + "="*70)
        print("📊 STATISTIQUES DE LA DOCUMENTATION")
        print("="*70)

        # Statistiques globales
        total_reading_time = self.total_words / WORDS_PER_MINUTE
        hours = int(total_reading_time // 60)
        minutes = int(total_reading_time % 60)

        print(f"\n📚 Vue d'ensemble")
        print(f"{'─'*70}")
        print(f"  Pages de documentation : {len(self.pages)}")
        print(f"  Lignes totales         : {self.total_lines:,}")
        print(f"  Mots totaux            : {self.total_words:,}")
        print(f"  Temps de lecture       : {hours}h {minutes}min")

        print(f"\n📝 Éléments de contenu")
        print(f"{'─'*70}")
        print(f"  Blocs de code          : {self.total_code_blocks}")
        print(f"  Images                 : {self.total_images}")
        print(f"  Liens                  : {self.total_links}")
        print(f"  Admonitions (tips/warnings) : {self.total_admonitions}")

        # Assets
        assets = self.check_assets_coverage()
        if 'error' not in assets:
            print(f"\n🖼️  Assets")
            print(f"{'─'*70}")
            print(f"  Images totales         : {assets['total_images']}")
            print(f"  Screenshots            : {assets['screenshots']}")
            print(f"  Taille totale          : {assets['assets_size_mb']:.2f} MB")

        # Top 5 pages les plus longues
        sorted_pages = sorted(self.pages, key=lambda x: x['words'], reverse=True)
        print(f"\n📖 Top 5 des pages les plus longues")
        print(f"{'─'*70}")
        for i, page in enumerate(sorted_pages[:5], 1):
            print(f"  {i}. {page['title'][:50]:<50} {page['words']:>5} mots ({page['reading_time_minutes']}min)")

        # Pages par catégorie (guides numérotés)
        guides = [p for p in self.pages if re.match(r'\d{2}-', p['file'])]
        autres = [p for p in self.pages if not re.match(r'\d{2}-', p['file'])]

        print(f"\n📂 Répartition du contenu")
        print(f"{'─'*70}")
        print(f"  Guides numérotés       : {len(guides)}")
        print(f"  Autres pages           : {len(autres)}")

        # Statistiques moyennes
        if self.pages:
            avg_words = self.total_words / len(self.pages)
            avg_time = avg_words / WORDS_PER_MINUTE
            print(f"\n📊 Moyennes par page")
            print(f"{'─'*70}")
            print(f"  Mots moyens            : {int(avg_words)}")
            print(f"  Temps de lecture moyen : {avg_time:.1f} min")

        print("\n" + "="*70)

        # Export JSON
        if export_path:
            report_data = {
                'generated_at': datetime.now().isoformat(),
                'summary': {
                    'total_pages': len(self.pages),
                    'total_words': self.total_words,
                    'total_lines': self.total_lines,
                    'reading_time_hours': hours,
                    'reading_time_minutes': minutes,
                    'code_blocks': self.total_code_blocks,
                    'images': self.total_images,
                    'links': self.total_links,
                    'admonitions': self.total_admonitions,
                },
                'assets': assets,
                'pages': self.pages,
            }

            try:
                with open(export_path, 'w', encoding='utf-8') as f:
                    json.dump(report_data, f, indent=2, ensure_ascii=False)
                print(f"\n✅ Rapport exporté vers : {export_path}")
            except Exception as e:
                print(f"\n❌ Erreur lors de l'export : {e}")

        print()


def main():
    """Point d'entrée principal"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Génère des statistiques sur la documentation"
    )
    parser.add_argument(
        '--export',
        type=str,
        help='Exporter les statistiques en JSON'
    )
    parser.add_argument(
        '--dir',
        type=str,
        default=str(DOCS_DIR),
        help='Répertoire à analyser'
    )

    args = parser.parse_args()

    target_dir = Path(args.dir)

    if not target_dir.exists():
        print(f"❌ Erreur : Le répertoire {target_dir} n'existe pas")
        sys.exit(1)

    print(f"\n🔍 Analyse de la documentation dans : {target_dir}")

    stats = DocumentationStats()
    stats.scan_directory(target_dir)
    stats.generate_report(export_path=args.export)

    print("✅ Analyse terminée !")


if __name__ == "__main__":
    main()
