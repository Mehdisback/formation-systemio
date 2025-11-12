#!/usr/bin/env python3
"""
Script de validation du frontmatter YAML pour Formation Systeme.io

Valide :
- Syntaxe YAML correcte
- Présence des champs requis (title, description)
- Longueur des descriptions (SEO)
- Meta tags recommandés

Usage :
    python scripts/validate_frontmatter.py
    python scripts/validate_frontmatter.py --strict
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

try:
    import yaml
except ImportError:
    print("❌ Erreur : PyYAML n'est pas installé")
    print("Installation : pip install PyYAML")
    sys.exit(1)

# Configuration
DOCS_DIR = Path("docs")
REQUIRED_FIELDS = ['title']  # Champs obligatoires
RECOMMENDED_FIELDS = ['description']  # Champs recommandés
MIN_DESCRIPTION_LENGTH = 50
MAX_DESCRIPTION_LENGTH = 160


class FrontmatterValidator:
    """Validateur de frontmatter YAML pour documentation MkDocs"""

    def __init__(self, strict: bool = False):
        self.strict = strict
        self.files_checked = 0
        self.files_with_errors = 0
        self.files_with_warnings = 0
        self.errors = []
        self.warnings = []

    def extract_frontmatter(self, content: str) -> Tuple[Dict, bool]:
        """
        Extrait le frontmatter YAML d'un fichier Markdown

        Returns:
            (frontmatter_dict, has_frontmatter)
        """
        frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n'
        match = re.match(frontmatter_pattern, content, re.DOTALL)

        if not match:
            return {}, False

        yaml_content = match.group(1)

        try:
            frontmatter = yaml.safe_load(yaml_content)
            return frontmatter or {}, True
        except yaml.YAMLError as e:
            return {'_parse_error': str(e)}, True

    def validate_file(self, file_path: Path) -> Tuple[List[str], List[str]]:
        """
        Valide le frontmatter d'un fichier

        Returns:
            (errors, warnings)
        """
        errors = []
        warnings = []

        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            errors.append(f"❌ Impossible de lire le fichier : {e}")
            return errors, warnings

        frontmatter, has_frontmatter = self.extract_frontmatter(content)

        # Vérifier erreur de parsing
        if '_parse_error' in frontmatter:
            errors.append(f"❌ Erreur YAML : {frontmatter['_parse_error']}")
            return errors, warnings

        # Pas de frontmatter
        if not has_frontmatter:
            if self.strict:
                errors.append("❌ Pas de frontmatter YAML")
            else:
                warnings.append("⚠️  Pas de frontmatter (recommandé pour SEO)")
            return errors, warnings

        # Vérifier champs requis
        for field in REQUIRED_FIELDS:
            if field not in frontmatter:
                errors.append(f"❌ Champ requis manquant : '{field}'")

        # Vérifier champs recommandés
        for field in RECOMMENDED_FIELDS:
            if field not in frontmatter:
                warnings.append(f"⚠️  Champ recommandé manquant : '{field}'")

        # Valider la description (SEO)
        if 'description' in frontmatter:
            desc = frontmatter['description']
            if isinstance(desc, str):
                desc_length = len(desc)

                if desc_length < MIN_DESCRIPTION_LENGTH:
                    warnings.append(
                        f"⚠️  Description trop courte : {desc_length} car. "
                        f"(min {MIN_DESCRIPTION_LENGTH} recommandé)"
                    )
                elif desc_length > MAX_DESCRIPTION_LENGTH:
                    warnings.append(
                        f"⚠️  Description trop longue : {desc_length} car. "
                        f"(max {MAX_DESCRIPTION_LENGTH} recommandé)"
                    )
            else:
                warnings.append("⚠️  'description' devrait être une chaîne de caractères")

        # Vérifier autres champs utiles
        useful_fields = {
            'keywords': 'Mots-clés SEO',
            'author': 'Auteur du contenu',
            'date': 'Date de création',
        }

        for field, desc in useful_fields.items():
            if field not in frontmatter:
                # Ne pas afficher ces warnings par défaut (trop verbeux)
                pass

        return errors, warnings

    def validate_directory(self, directory: Path):
        """Valide tous les fichiers Markdown d'un répertoire"""
        print(f"\n🔍 Validation du frontmatter : {directory}")
        print(f"📊 Mode : {'STRICT' if self.strict else 'NORMAL'}\n")

        md_files = list(directory.rglob('*.md'))

        # Exclure certains fichiers
        excluded_patterns = ['node_modules', '.venv', 'site', 'CHANGELOG', 'README']
        md_files = [
            f for f in md_files
            if not any(pattern in str(f) for pattern in excluded_patterns)
        ]

        if not md_files:
            print(f"⚠️  Aucun fichier Markdown trouvé dans {directory}")
            return

        print(f"📄 {len(md_files)} fichiers trouvés\n")

        for file_path in sorted(md_files):
            self.files_checked += 1
            relative_path = file_path.relative_to(directory)

            errors, warnings = self.validate_file(file_path)

            if errors:
                self.files_with_errors += 1
                print(f"❌ {relative_path}")
                for error in errors:
                    print(f"   {error}")
                self.errors.extend([(relative_path, e) for e in errors])

            elif warnings:
                self.files_with_warnings += 1
                if not self.strict:  # N'afficher les warnings qu'en mode normal
                    print(f"⚠️  {relative_path}")
                    for warning in warnings:
                        print(f"   {warning}")
                self.warnings.extend([(relative_path, w) for w in warnings])

            else:
                print(f"✅ {relative_path}")

        # Rapport final
        self.print_report()

    def print_report(self):
        """Affiche le rapport de validation"""
        print("\n" + "="*60)
        print("📊 RAPPORT DE VALIDATION")
        print("="*60)
        print(f"Fichiers vérifiés : {self.files_checked}")
        print(f"✅ OK : {self.files_checked - self.files_with_errors - self.files_with_warnings}")
        print(f"⚠️  Warnings : {self.files_with_warnings}")
        print(f"❌ Erreurs : {self.files_with_errors}")

        if self.files_with_errors > 0:
            print("\n⚠️  Des erreurs ont été détectées !")
            print("="*60)

            # Résumé des erreurs
            error_summary = {}
            for _, error in self.errors:
                error_type = error.split(':')[0] if ':' in error else error
                error_summary[error_type] = error_summary.get(error_type, 0) + 1

            print("\nTypes d'erreurs :")
            for error_type, count in sorted(error_summary.items(), key=lambda x: -x[1]):
                print(f"  {error_type} : {count}x")

        print("="*60 + "\n")

        # Code de sortie
        if self.files_with_errors > 0:
            sys.exit(1)


def main():
    """Point d'entrée principal"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Valide le frontmatter YAML des fichiers Markdown"
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Mode strict : erreur si pas de frontmatter'
    )
    parser.add_argument(
        '--dir',
        type=str,
        default=str(DOCS_DIR),
        help='Répertoire à valider'
    )

    args = parser.parse_args()

    target_dir = Path(args.dir)

    if not target_dir.exists():
        print(f"❌ Erreur : Le répertoire {target_dir} n'existe pas")
        sys.exit(1)

    validator = FrontmatterValidator(strict=args.strict)
    validator.validate_directory(target_dir)

    if validator.files_with_errors == 0:
        print("✅ Validation réussie !")
    else:
        print("❌ Validation échouée")
        sys.exit(1)


if __name__ == "__main__":
    main()
