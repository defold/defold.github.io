# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## About This Codebase

This is the Jekyll-powered static website for Defold (defold.com), a cross-platform game engine. The site aggregates content from multiple external repositories and serves as the main documentation hub, showcase, and community portal.

## Architecture Overview

### Core Structure
- **Jekyll Static Site Generator**: Uses Jekyll with GitHub Pages gems for site generation
- **Multi-Repository Content System**: The main site pulls content from several external repositories via `update.py`
- **Liquid Templating**: Extensive use of Jekyll Liquid templates for dynamic content generation
- **JSON Data Files**: All dynamic content (games, assets, API documentation) is stored as JSON in `_data/`

### External Content Sources
The site aggregates content from these repositories (managed by `update.py`):
- **Docs**: github.com/defold/doc → manuals, tutorials, FAQ
- **Examples**: github.com/defold/examples → code examples
- **Asset Portal**: github.com/defold/asset-portal → community assets/libraries
- **Games Showcase**: github.com/defold/games-showcase → featured games
- **CodePad**: github.com/defold/codepad → online code editor
- **API Reference**: Latest release from d.defold.com → API documentation

### Key Data Architecture
- `_data/games.json`: Game showcase data with placement fields (`frontpage`, `showcase`, etc.)
- `_data/assets/`: Individual JSON files for each asset/library
- `_data/ref/`: API reference documentation in JSON format (alpha/beta/stable versions)
- `_includes/`: Reusable template components for rendering games, assets, cards, etc.
- `_layouts/`: Page layouts for different content types

### Game Display Logic
Games are displayed using a sophisticated placement system:
- Games have placement fields like `"frontpage": "full"`, `"showcase": "half"`
- `games_full.html` filters by placement parameter and randomly shuffles results at build time
- Random selection happens during Jekyll build, not on page load (static site)

## Development Commands

### Local Development
```bash
# Install dependencies
bundle install

# Start development server (recommended)
# This builds the site, generates Pagefind search index, then serves
./serve.sh

# Alternative server start (if port 4000 is busy)
bundle exec jekyll build --drafts --future
npx -y pagefind --site _site --output-path _site/_pagefind
bundle exec jekyll serve --port 4001 --host 0.0.0.0 --skip-initial-build
```

### Content Updates
```bash
# Update all external content (requires Python dependencies)
python3 update.py [--download] docs codepad refdoc examples asset-portal games-showcase

# Install Python dependencies first:
pip3 install --user requests pyyaml markdown==3.4.1 pygments==2.13.0

# Update specific content types
python3 update.py --download docs           # Documentation
python3 update.py --download asset-portal   # Assets
python3 update.py --download games-showcase # Games
python3 update.py refdoc                   # API reference (needs refdoc_*.zip files)

# Search indexing is handled automatically by Pagefind during site build
# No manual search indexing command needed
```

### Ruby Environment Setup
```bash
# Install Ruby via Homebrew (macOS)
brew install ruby
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"

# Or using rbenv
brew install rbenv
rbenv install $(cat .ruby-version)
rbenv local $(cat .ruby-version)

# Install gems
gem install bundler
bundle install
```

### Testing Reference Documentation Locally
```bash
# Copy refdoc files to main folder
cp $DYNAMO_HOME/share/ref-doc.zip refdoc_alpha.zip
cp $DYNAMO_HOME/share/ref-doc.zip refdoc_beta.zip  
cp $DYNAMO_HOME/share/ref-doc.zip refdoc_stable.zip
./update.py refdoc
./serve.sh
```

## Working with Games Data

### Game Configuration
Games are configured in `_data/games.json` with placement fields:
- `"frontpage": "full"` - Eligible for main page featured game
- `"showcase": "full"` - Shown in full showcase view
- `"showcase": "half"` - Half-width showcase view
- `"games": "half"` - Half-width in games section

### Featured Game Selection
The main page game selection (`index.html:96`):
```liquid
{%- include games_full.html placement="frontpage" limit=1 offset=0 url="/showcase" -%}
```
- Randomly selects 1 game from those with `"frontpage": "full"`
- Selection happens at build time, not page load
- To see different games, rebuild the site

### Hardcoded Hero Elements
The main page hero section has hardcoded elements:
- Background image: `/images/frontpage/voidscrappers.jpg` (line 8)
- Credit link: "Void Scrappers - 8BitSkull" Steam link (line 51)

## File Organization

### Critical Files
- `index.html`: Main homepage with hardcoded hero and dynamic game selection
- `update.py`: Python script for pulling external content
- `serve.sh`: Jekyll development server with optimal flags
- `_data/games.json`: Game showcase configuration
- `_config.yml`: Jekyll configuration

### Template Structure
- `_includes/games_*.html`: Game display templates (full, half, third width)
- `_includes/game_*.html`: Individual game card templates
- `_layouts/`: Page layout templates
- `_includes/shared/`: Multilingual shared content

### Build Outputs
- `_site/`: Generated static site (ignored by git)
- `_site/_pagefind/`: Generated Pagefind search index
- Various `*-master.zip` files: Downloaded external content

## Search System
- **Site Search**: Uses Pagefind for static site indexing and client-side UI
- **Page Search**: Mark.js for in-page search and highlighting
- **Implementation**: Pagefind Python runner generates index during build; UI loaded on `/search.html`
- **Search Interface**: Pagefind UI with filters (e.g., `section`) and excerpts
- Index is generated during CI and local builds; no manual command needed

## Automated Updates
GitHub Actions automatically trigger `update.py` when external repositories change:
- Asset Portal, Games Showcase, Docs, Examples, CodePad changes trigger site rebuilds
- Hourly updates for GitHub star counts on assets

## CSS/SCSS Structure
- `_scss/`: SCSS source files
- `css/main.scss`, `css/media.scss`: Main stylesheets
- `assets/css/style.scss`: Theme stylesheet
- SASS compilation configured in `_config.yml`

## Important Notes
- Site uses GitHub Pages configuration and gems
- All external content must be processed through `update.py` 
- Game selection randomization requires site rebuild to change
- Ruby 3.4+ requires explicit `csv` and `logger` gems (included in Gemfile)
- Development server runs on http://localhost:4000 by default
