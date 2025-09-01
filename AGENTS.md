# Repository Guidelines

## Project Structure & Organization
- Core: Jekyll + GitHub Pages using Liquid templates.
- Templates: `/_layouts` (page layouts), `/_includes` (partials), `/_data` (YAML data).
- Content: root `.html/.md` pages, blog in `/_posts`, localized/section pages in folders (e.g., `manuals/`, `examples/`, `authors/`).
- Assets: `/assets`, `/images`, `/_scss`, `/css`, `/js`.
- Generated: `/_site` (build output). Do not edit tracked content imported by `update.py`.

## Build, Test, and Development Commands
- Install gems: `bundle install`
- Serve locally: `./serve.sh` (builds site + Pagefind index, then serves at `http://localhost:4000`)
- Build site: `bundle exec jekyll build` (outputs to `/_site`)
- Update content: `python3 update.py --download docs examples asset-portal games-showcase refdoc`
  - Use `DM_DOC_DIR=/path/to/doc python3 update.py docs` to source local docs.

## Coding Style & Naming Conventions
- Markdown/HTML: two‑space indentation; add YAML front matter with `title`, `layout`, `permalink` where applicable.
- Liquid: prefer readable filters and named includes (e.g., `{% include card.html title=... %}`).
- Filenames/URLs: kebab‑case (e.g., `instant-games.html`).
- SCSS/CSS: keep shared variables/partials in `/_scss`; compile via Jekyll. Follow existing BEM‑like class patterns.
- JavaScript: place in `/js`; keep DOM‑ready logic minimal and page‑scoped.

## Testing Guidelines
- Local verify: build or serve without Liquid errors, then click through key pages.
- Sanity checks: `bundle exec jekyll doctor` for common issues; confirm Pagefind search works after site build.
- No formal unit tests; rely on local build + visual review and link checks.

## Commit & Pull Request Guidelines
- Commits: concise, imperative subject (e.g., “Update partner logos”). Use `[skip-ci]` for content-only/site text changes that shouldn’t trigger automation.
- PRs: include summary, linked issues, scope of change, and screenshots for visual/ui changes. Note how you tested locally (`./serve.sh`) and if `update.py` was run.
- Do not commit `/_site` or secrets.

## Security & CI Tips
- Secrets: never commit tokens. For automation, pass `--githubtoken` to `update.py` via GitHub Actions secrets.
- Large files: prefer importing via `update.py` over committing binaries manually.

