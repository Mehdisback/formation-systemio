#!/usr/bin/env python3
"""
Script d'optimisation d'images pour Formation Systeme.io

Fonctionnalités :
- Compression d'images PNG/JPG
- Conversion vers WebP (optionnel)
- Génération de versions responsive
- Rapport d'optimisation avec gains

Usage :
    python scripts/optimize_images.py
    python scripts/optimize_images.py --webp
    python scripts/optimize_images.py --quality 85
"""

import os
import sys
from pathlib import Path
from typing import List, Tuple

try:
    from PIL import Image
except ImportError:
    print("❌ Erreur : Pillow n'est pas installé")
    print("Installation : pip install Pillow")
    sys.exit(1)

# Configuration
DOCS_DIR = Path("docs")
ASSETS_DIR = DOCS_DIR / "assets"
MAX_SIZE_KB = 100  # Taille max cible en KB
QUALITY = 85  # Qualité JPEG/WebP (1-100)
RESPONSIVE_WIDTHS = [320, 640, 1024, 1920]  # Largeurs responsive


class ImageOptimizer:
    """Optimiseur d'images pour documentation MkDocs"""

    def __init__(self, quality: int = QUALITY, max_size_kb: int = MAX_SIZE_KB):
        self.quality = quality
        self.max_size_kb = max_size_kb
        self.total_original = 0
        self.total_optimized = 0
        self.files_processed = 0

    def get_file_size_kb(self, file_path: Path) -> float:
        """Retourne la taille du fichier en KB"""
        return file_path.stat().st_size / 1024

    def optimize_image(self, image_path: Path, convert_webp: bool = False) -> Tuple[bool, str]:
        """
        Optimise une image (compression, redimensionnement si nécessaire)

        Args:
            image_path: Chemin vers l'image
            convert_webp: Convertir en WebP

        Returns:
            (success, message)
        """
        try:
            original_size = self.get_file_size_kb(image_path)
            self.total_original += original_size

            # Ouvrir l'image
            img = Image.open(image_path)

            # Convertir RGBA en RGB si nécessaire (pour JPEG)
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background

            # Sauvegarder avec optimisation
            if convert_webp:
                webp_path = image_path.with_suffix('.webp')
                img.save(webp_path, 'WebP', quality=self.quality, method=6)
                optimized_size = self.get_file_size_kb(webp_path)
                message = f"✓ Converti en WebP : {original_size:.1f} KB → {optimized_size:.1f} KB"
            else:
                # Optimiser en place
                if image_path.suffix.lower() in ['.jpg', '.jpeg']:
                    img.save(image_path, 'JPEG', quality=self.quality, optimize=True, progressive=True)
                elif image_path.suffix.lower() == '.png':
                    img.save(image_path, 'PNG', optimize=True)

                optimized_size = self.get_file_size_kb(image_path)

                # Redimensionner si toujours trop gros
                if optimized_size > self.max_size_kb and max(img.size) > 1920:
                    ratio = (1920 / max(img.size)) ** 0.5
                    new_size = tuple(int(dim * ratio) for dim in img.size)
                    img = img.resize(new_size, Image.Resampling.LANCZOS)

                    if image_path.suffix.lower() in ['.jpg', '.jpeg']:
                        img.save(image_path, 'JPEG', quality=self.quality, optimize=True)
                    else:
                        img.save(image_path, 'PNG', optimize=True)

                    optimized_size = self.get_file_size_kb(image_path)

                message = f"✓ Optimisé : {original_size:.1f} KB → {optimized_size:.1f} KB"

            self.total_optimized += optimized_size
            self.files_processed += 1

            # Avertissement si toujours trop gros
            if optimized_size > self.max_size_kb:
                message += f" ⚠️  Dépasse {self.max_size_kb} KB"

            return True, message

        except Exception as e:
            return False, f"❌ Erreur : {str(e)}"

    def generate_responsive_versions(self, image_path: Path) -> List[str]:
        """Génère des versions responsive de l'image"""
        messages = []

        try:
            img = Image.open(image_path)
            original_width = img.width

            # Créer dossier responsive
            responsive_dir = image_path.parent / "responsive"
            responsive_dir.mkdir(exist_ok=True)

            for width in RESPONSIVE_WIDTHS:
                if width >= original_width:
                    continue  # Ne pas upscale

                ratio = width / original_width
                new_height = int(img.height * ratio)

                resized = img.resize((width, new_height), Image.Resampling.LANCZOS)

                output_name = f"{image_path.stem}_{width}w{image_path.suffix}"
                output_path = responsive_dir / output_name

                if image_path.suffix.lower() in ['.jpg', '.jpeg']:
                    resized.save(output_path, 'JPEG', quality=self.quality, optimize=True)
                else:
                    resized.save(output_path, 'PNG', optimize=True)

                size = self.get_file_size_kb(output_path)
                messages.append(f"  → {width}px : {size:.1f} KB")

            return messages

        except Exception as e:
            return [f"❌ Erreur génération responsive : {str(e)}"]

    def scan_and_optimize(self, directory: Path, convert_webp: bool = False, responsive: bool = False):
        """Scanne et optimise toutes les images d'un répertoire"""
        print(f"\n🔍 Scan du répertoire : {directory}")
        print(f"📊 Configuration : quality={self.quality}, max_size={self.max_size_kb}KB\n")

        image_extensions = {'.jpg', '.jpeg', '.png'}
        images = [
            f for f in directory.rglob('*')
            if f.suffix.lower() in image_extensions and 'responsive' not in f.parts
        ]

        if not images:
            print(f"⚠️  Aucune image trouvée dans {directory}")
            return

        print(f"📸 {len(images)} images trouvées\n")

        for image_path in images:
            print(f"Processing : {image_path.relative_to(DOCS_DIR)}")

            success, message = self.optimize_image(image_path, convert_webp)
            print(f"  {message}")

            if responsive and success:
                resp_messages = self.generate_responsive_versions(image_path)
                for msg in resp_messages:
                    print(msg)

        # Rapport final
        print("\n" + "="*60)
        print("📊 RAPPORT D'OPTIMISATION")
        print("="*60)
        print(f"Fichiers traités : {self.files_processed}")
        print(f"Taille originale : {self.total_original:.2f} KB")
        print(f"Taille optimisée : {self.total_optimized:.2f} KB")

        if self.total_original > 0:
            gain_percent = ((self.total_original - self.total_optimized) / self.total_original) * 100
            gain_kb = self.total_original - self.total_optimized
            print(f"Gain : {gain_kb:.2f} KB ({gain_percent:.1f}%)")

        print("="*60 + "\n")


def main():
    """Point d'entrée principal"""
    import argparse

    parser = argparse.ArgumentParser(description="Optimise les images de la documentation")
    parser.add_argument('--quality', type=int, default=QUALITY, help='Qualité JPEG/WebP (1-100)')
    parser.add_argument('--max-size', type=int, default=MAX_SIZE_KB, help='Taille max en KB')
    parser.add_argument('--webp', action='store_true', help='Convertir en WebP')
    parser.add_argument('--responsive', action='store_true', help='Générer versions responsive')
    parser.add_argument('--dir', type=str, default=str(ASSETS_DIR), help='Répertoire à scanner')

    args = parser.parse_args()

    target_dir = Path(args.dir)

    if not target_dir.exists():
        print(f"❌ Erreur : Le répertoire {target_dir} n'existe pas")
        sys.exit(1)

    optimizer = ImageOptimizer(quality=args.quality, max_size_kb=args.max_size)
    optimizer.scan_and_optimize(target_dir, convert_webp=args.webp, responsive=args.responsive)

    print("✅ Optimisation terminée !")


if __name__ == "__main__":
    main()
