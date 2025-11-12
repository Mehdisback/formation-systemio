#!/usr/bin/env python3
"""
Script de vérification orthographique française pour Formation Systeme.io

Vérifie :
- Orthographe des mots français
- Dictionnaire personnalisé pour termes techniques
- Suggestions de corrections

Usage :
    python scripts/check_spelling.py
    python scripts/check_spelling.py --file docs/01-GUIDE-DEMARRAGE-RAPIDE.md
    python scripts/check_spelling.py --add-word "Systeme.io"
"""

import re
import sys
from pathlib import Path
from typing import List, Set, Dict, Tuple
from collections import defaultdict

try:
    from spellchecker import SpellChecker
except ImportError:
    print("❌ Erreur : pyspellchecker n'est pas installé")
    print("Installation : pip install pyspellchecker")
    sys.exit(1)

# Configuration
DOCS_DIR = Path("docs")
CUSTOM_DICT_PATH = Path("scripts/.custom_dictionary.txt")

# Dictionnaire personnalisé (termes techniques, noms propres)
DEFAULT_CUSTOM_WORDS = {
    # Noms de produits/services
    'systeme.io', 'systemio', 'calendly', 'google analytics', 'mkdocs',
    'github', 'markdown', 'html', 'css', 'javascript',

    # Termes techniques web
    'landing page', 'cta', 'call-to-action', 'seo', 'url', 'https',
    'pixel', 'tracking', 'analytics', 'dashboard', 'workflow',

    # Noms propres du projet
    'coaching au féminin', 'armelle', 'bodénès', 'mehdi', 'slayki',
    'atek universe', 'ennéagramme',

    # Termes marketing/coaching
    'webinaire', 'opt-in', 'lead magnet', 'funnel', 'storytelling',
    'branding', 'responsive',

    # Termes MkDocs
    'admonition', 'frontmatter', 'yaml', 'plugin', 'minify',

    # Acronymes
    'wcag', 'rgaa', 'ga4', 'pdf', 'png', 'jpg', 'gif', 'svg',
}


class FrenchSpellChecker:
    """Vérificateur orthographique pour documentation française"""

    def __init__(self):
        self.spell = SpellChecker(language='fr')
        self.custom_words = self.load_custom_dictionary()
        self.spell.word_frequency.load_words(self.custom_words)

        self.total_words_checked = 0
        self.errors_found = defaultdict(int)
        self.files_with_errors = 0

    def load_custom_dictionary(self) -> Set[str]:
        """Charge le dictionnaire personnalisé"""
        words = set(DEFAULT_CUSTOM_WORDS)

        if CUSTOM_DICT_PATH.exists():
            try:
                content = CUSTOM_DICT_PATH.read_text(encoding='utf-8')
                custom = {line.strip().lower() for line in content.split('\n') if line.strip()}
                words.update(custom)
            except Exception as e:
                print(f"⚠️  Erreur lecture dictionnaire personnalisé : {e}")

        return words

    def save_custom_dictionary(self):
        """Sauvegarde le dictionnaire personnalisé"""
        try:
            CUSTOM_DICT_PATH.parent.mkdir(exist_ok=True)
            content = '\n'.join(sorted(self.custom_words))
            CUSTOM_DICT_PATH.write_text(content, encoding='utf-8')
            print(f"✅ Dictionnaire personnalisé sauvegardé : {len(self.custom_words)} mots")
        except Exception as e:
            print(f"❌ Erreur sauvegarde dictionnaire : {e}")

    def add_word(self, word: str):
        """Ajoute un mot au dictionnaire personnalisé"""
        word_lower = word.lower()
        self.custom_words.add(word_lower)
        self.spell.word_frequency.load_words([word_lower])
        self.save_custom_dictionary()
        print(f"✅ Mot ajouté au dictionnaire : {word}")

    def clean_text(self, text: str) -> str:
        """Nettoie le texte avant vérification"""
        # Retirer le frontmatter YAML
        text = re.sub(r'^---.*?---\s*', '', text, flags=re.DOTALL)

        # Retirer les blocs de code
        text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
        text = re.sub(r'`[^`]+`', '', text)

        # Retirer les URLs
        text = re.sub(r'https?://[^\s]+', '', text)

        # Retirer les balises HTML
        text = re.sub(r'<[^>]+>', '', text)

        # Retirer les images et liens Markdown
        text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
        text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)

        # Retirer les titres Markdown (garder le texte)
        text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)

        # Retirer les admonitions
        text = re.sub(r'!!! \w+.*?\n', '', text)

        return text

    def extract_words(self, text: str) -> List[str]:
        """Extrait les mots du texte"""
        # Mots français : lettres (y compris accents), apostrophes, tirets
        words = re.findall(r"[a-zA-ZÀ-ÿ]+(?:[-'][a-zA-ZÀ-ÿ]+)*", text)
        return [w for w in words if len(w) > 1]  # Ignorer lettres seules

    def check_file(self, file_path: Path) -> Dict[str, List[Tuple[str, List[str]]]]:
        """
        Vérifie l'orthographe d'un fichier

        Returns:
            Dict avec les erreurs trouvées et suggestions
        """
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            return {'error': str(e)}

        cleaned_text = self.clean_text(content)
        words = self.extract_words(cleaned_text)

        self.total_words_checked += len(words)

        # Vérifier l'orthographe
        misspelled = self.spell.unknown(words)

        if not misspelled:
            return {}

        # Grouper les erreurs avec suggestions
        errors = {}
        for word in misspelled:
            if word.lower() in self.custom_words:
                continue  # Déjà dans le dictionnaire personnalisé

            # Obtenir suggestions
            suggestions = list(self.spell.candidates(word))[:3]  # Top 3
            errors[word] = suggestions
            self.errors_found[word.lower()] += 1

        return errors

    def check_directory(self, directory: Path, single_file: str = None):
        """Vérifie l'orthographe de tous les fichiers d'un répertoire"""
        print(f"\n🔍 Vérification orthographique : {directory}")
        print(f"📚 Dictionnaire : français + {len(self.custom_words)} mots personnalisés\n")

        if single_file:
            md_files = [Path(single_file)]
        else:
            md_files = list(directory.rglob('*.md'))
            # Exclure certains fichiers
            excluded_patterns = ['node_modules', '.venv', 'site', 'CHANGELOG']
            md_files = [
                f for f in md_files
                if not any(pattern in str(f) for pattern in excluded_patterns)
            ]

        if not md_files:
            print(f"⚠️  Aucun fichier Markdown trouvé")
            return

        print(f"📄 {len(md_files)} fichiers à vérifier\n")

        for file_path in sorted(md_files):
            relative_path = file_path.relative_to(directory) if not single_file else file_path.name

            errors = self.check_file(file_path)

            if 'error' in errors:
                print(f"❌ {relative_path} : {errors['error']}")
                continue

            if errors:
                self.files_with_errors += 1
                print(f"⚠️  {relative_path} ({len(errors)} erreur{'s' if len(errors) > 1 else ''})")

                # Afficher les erreurs (max 10 par fichier)
                for i, (word, suggestions) in enumerate(list(errors.items())[:10], 1):
                    sugg_str = ', '.join(suggestions) if suggestions else 'aucune suggestion'
                    print(f"   {i}. '{word}' → {sugg_str}")

                if len(errors) > 10:
                    print(f"   ... et {len(errors) - 10} autre{'s' if len(errors) > 10 else ''} erreur(s)")

            else:
                print(f"✅ {relative_path}")

        # Rapport final
        self.print_report()

    def print_report(self):
        """Affiche le rapport de vérification"""
        print("\n" + "="*70)
        print("📊 RAPPORT DE VÉRIFICATION ORTHOGRAPHIQUE")
        print("="*70)
        print(f"Mots vérifiés       : {self.total_words_checked:,}")
        print(f"Erreurs uniques     : {len(self.errors_found)}")
        print(f"Erreurs totales     : {sum(self.errors_found.values())}")
        print(f"Fichiers avec erreurs : {self.files_with_errors}")

        if self.errors_found:
            print(f"\n⚠️  Top 10 des erreurs fréquentes :")
            print("─"*70)

            sorted_errors = sorted(self.errors_found.items(), key=lambda x: -x[1])
            for i, (word, count) in enumerate(sorted_errors[:10], 1):
                suggestions = list(self.spell.candidates(word))[:3]
                sugg_str = ', '.join(suggestions) if suggestions else 'aucune suggestion'
                print(f"  {i}. '{word}' ({count}x) → {sugg_str}")

            print(f"\n💡 Pour ajouter un mot au dictionnaire personnalisé :")
            print(f"   python scripts/check_spelling.py --add-word \"votre_mot\"")

        print("="*70 + "\n")


def main():
    """Point d'entrée principal"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Vérification orthographique française de la documentation"
    )
    parser.add_argument(
        '--file',
        type=str,
        help='Vérifier un fichier spécifique'
    )
    parser.add_argument(
        '--dir',
        type=str,
        default=str(DOCS_DIR),
        help='Répertoire à vérifier'
    )
    parser.add_argument(
        '--add-word',
        type=str,
        help='Ajouter un mot au dictionnaire personnalisé'
    )

    args = parser.parse_args()

    checker = FrenchSpellChecker()

    # Ajouter un mot au dictionnaire
    if args.add_word:
        checker.add_word(args.add_word)
        return

    # Vérifier les fichiers
    target_dir = Path(args.dir) if not args.file else Path(args.file).parent

    if not target_dir.exists():
        print(f"❌ Erreur : Le répertoire {target_dir} n'existe pas")
        sys.exit(1)

    checker.check_directory(target_dir, single_file=args.file)

    if checker.files_with_errors > 0:
        print("⚠️  Des erreurs orthographiques ont été détectées")
        print("Vérifiez les suggestions ou ajoutez les mots techniques au dictionnaire\n")
    else:
        print("✅ Aucune erreur orthographique détectée !")


if __name__ == "__main__":
    main()
