# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **MkDocs Material documentation site** for training Armelle Bodénès (Coaching au Féminin) on managing her Systeme.io landing page autonomously. The documentation is published to GitHub Pages and provides comprehensive guides for non-technical users.

**Live Site:** https://mehdisback.github.io/formation-systemeio/
**Landing Page:** https://bodenesgram.systeme.io/essentiel-en-soi

## Technology Stack

- **MkDocs Material** - Static site generator for documentation
- **Python 3.x** - Required for MkDocs
- **GitHub Actions** - CI/CD pipeline for automatic deployment
- **GitHub Pages** - Hosting platform

## Development Commands

### Local Development

```bash
# Install dependencies
pip install mkdocs-material
pip install mkdocs-minify-plugin

# Serve documentation locally with live reload
mkdocs serve

# Build the documentation site
mkdocs build

# Deploy to GitHub Pages manually
mkdocs gh-deploy --force
```

The site will be available at `http://127.0.0.1:8000` when running locally.

### Testing Changes

Always preview changes locally with `mkdocs serve` before committing, especially:
- Navigation structure changes in `mkdocs.yml`
- Custom CSS modifications in `docs/stylesheets/extra.css`
- New markdown features or extensions

## Project Structure

```
formation-systemeio/
├── docs/                           # All documentation content
│   ├── index.md                    # Homepage/welcome page
│   ├── 01-GUIDE-DEMARRAGE-RAPIDE.md
│   ├── 02-MODIFICATION-CONTENU.md
│   ├── ... (guides 03-10)
│   └── stylesheets/
│       └── extra.css              # Custom A-Tek Universe branding
├── mkdocs.yml                     # MkDocs configuration
├── .github/workflows/ci.yml       # Auto-deploy on push to main
└── .gitignore
```

## MkDocs Configuration Architecture

### Key Configuration (`mkdocs.yml`)

- **Theme:** Material for MkDocs with custom color palette (Indigo/Deep Purple)
- **Language:** French (`fr`)
- **Navigation:** 10 structured training guides with emoji prefixes
- **Plugins:**
  - `search` with French language support
  - `minify` for HTML/CSS/JS optimization
- **Markdown Extensions:**
  - Admonitions for callout boxes (tip, warning, info, danger)
  - Code highlighting with syntax support
  - Task lists with clickable checkboxes
  - Emoji support via Material extensions
  - Tabs, tables, and tooltips

### Custom Styling

The `docs/stylesheets/extra.css` file contains A-Tek Universe branding:
- CSS variables for consistent color palette
- Gradient headers and navigation
- Custom admonition styling
- Enhanced tables, buttons, and cards
- Print-friendly styles
- Responsive design for mobile/tablet/desktop

## Documentation Structure

All documentation is written in **French** and follows a progressive learning path:

1. **01-GUIDE-DEMARRAGE-RAPIDE.md** - Login and basic navigation
2. **02-MODIFICATION-CONTENU.md** - Content editing (text, images, testimonials)
3. **03-GESTION-CTA-CALENDLY.md** - CTA button and Calendly management
4. **04-DESIGN-MISE-EN-PAGE.md** - Visual customization
5. **05-FORMULAIRES-DONNEES.md** - Form and data management
6. **06-SEO-REFERENCEMENT.md** - SEO optimization
7. **07-SUIVI-ANALYTICS.md** - Analytics tracking
8. **08-MAINTENANCE-BONNES-PRATIQUES.md** - Maintenance best practices
9. **09-FAQ-TROUBLESHOOTING.md** - FAQ and troubleshooting
10. **10-GLOSSAIRE.md** - Terminology glossary

## Deployment

### Automatic Deployment

- **Triggers:** Push to `main` branch or pull request
- **Workflow:** `.github/workflows/ci.yml`
- **Process:**
  1. Checks out code
  2. Sets up Python 3.x
  3. Installs `mkdocs-material` and `mkdocs-minify-plugin`
  4. Runs `mkdocs gh-deploy --force`
- **Result:** Published to GitHub Pages at https://mehdisback.github.io/formation-systemeio/

### Manual Deployment

If needed, deploy manually with:
```bash
mkdocs gh-deploy --force
```

## Content Guidelines

### Markdown Style

- Use **French language** for all content
- Include emoji icons in headers for visual appeal
- Use admonitions extensively for important information:
  - `!!! success` - Welcome messages, achievements
  - `!!! tip` - Helpful advice, pro tips
  - `!!! warning` - Caution, important notes
  - `!!! danger` - Security warnings, critical information
  - `!!! info` - Additional context, advanced features

### Navigation and Links

- All guide files use capitalized filenames (e.g., `01-GUIDE-DEMARRAGE-RAPIDE.md`)
- Internal links reference the `.md` extension
- External links include full URLs with target site
- Navigation in `mkdocs.yml` uses emoji prefixes for visual hierarchy

### Branding

- **Client:** Armelle Bodénès - Coaching au Féminin
- **Developer:** A-Tek Universe (https://a-tek-universe.fr)
- **Color Scheme:** Indigo (#3949AB) and Deep Purple (#7E57C2)
- Maintain professional, supportive tone suitable for non-technical coaching clients

## Common Modifications

### Adding a New Guide

1. Create new `.md` file in `docs/` (e.g., `11-NEW-GUIDE.md`)
2. Add to navigation in `mkdocs.yml` under `nav` section
3. Follow existing structure with emoji prefix
4. Include estimated duration and difficulty level
5. Test locally with `mkdocs serve`

### Updating Navigation

Edit the `nav` section in `mkdocs.yml`. Structure follows:
```yaml
nav:
  - 🏠 Accueil: "index.md"
  - 📚 Guides de formation:
    - 🚀 01 - Démarrage rapide: "01-GUIDE-DEMARRAGE-RAPIDE.md"
    # ... additional guides
```

### Modifying Styles

Edit `docs/stylesheets/extra.css`. Key sections:
- `:root` variables for color palette
- Header/navigation gradients
- Admonition border colors
- Table styling
- Button/CTA styling

## Validation

Before committing changes:

- [ ] Test locally with `mkdocs serve`
- [ ] Check all internal links work
- [ ] Verify responsive design (desktop, tablet, mobile views in browser)
- [ ] Ensure French language content is grammatically correct
- [ ] Confirm admonitions render properly
- [ ] Check code blocks and syntax highlighting
- [ ] Verify emoji icons display correctly

## Important Notes

- **No code/scripts:** This is a pure documentation project with no application code
- **Static site:** All content is pre-rendered Markdown to HTML
- **French-first:** All user-facing content must be in French
- **Non-technical audience:** Write for coaching professionals, not developers
- **GitHub Pages:** Changes to `main` branch auto-deploy within ~2 minutes
