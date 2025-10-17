# Taemin Park — Personal Site & Blog

Source for https://taemincode.github.io — a Jekyll-powered personal site with a long-form homepage, blog, and Manim-generated visuals.

**Live site:** https://taemincode.github.io

## Features

- **Landing page sections** – `index.html` renders a hero (with email reveal toggle), timeline, “Snapshot” profile card, work-in-progress/“Now” board, social links, and blog preview cards styled by `_sass/_about.scss`.
- **Blog listing & previews** – `blogs.html` builds an animated card grid (AOS) with full-card keyboard activation and an “Inspired by …” ribbon when `inspired_by` front matter is present; the homepage pulls the three latest posts, auto-detecting cover art from front matter or the first `<img>`.
- **Post UX** – `_layouts/post.html` shows published/updated metadata (via `jekyll-last-modified-at`), categories, copy-to-clipboard buttons, MathJax, Rouge styling, and a JS lightbox for in-article images.
- **Global theming** – SCSS design tokens in `_sass/_variables.scss` drive light/dark themes; the navbar toggle persists preference to `localStorage` and respects system defaults.
- **Accessibility & motion** – Reduced-motion visitors skip AOS and hover flair; keyboard focus states, ARIA labels, and responsive typography are wired throughout.
- **404 easter egg** – `404.html` includes an accessible “launch the rocket” animation with optional Typed.js heading reveal.
- **Visual assets** – Manim scenes under `manim/` render to `media/`; curated PNGs live in `assets/images/posts/` and hero art in `static/`.

## Tech Stack

- Jekyll 4.3.x, Kramdown/rouge markdown & highlighting
- Plugins: `jekyll-feed`, `jekyll-seo-tag`, `jekyll-last-modified-at`
- Front-end: SCSS partial pipeline, Bootstrap 5, Font Awesome, AOS, MathJax
- Tooling: Ruby/Bundler for site, Python + Manim for animations

## Directory Overview

```
├── index.html / blogs.html          # Landing + blog index pages
├── 404.html                         # Interactive not-found page
├── _config.yml                      # Site metadata & plugin config
├── _layouts/                        # Layouts (default, post)
├── _posts/                          # Markdown posts (YYYY-MM-DD-title.md)
├── _sass/                           # SCSS partials (variables, base, blog, post, ...)
├── assets/
│   ├── css/site.scss                # SCSS entry point (imports partials)
│   └── images/posts/<year>/...      # Post imagery checked into the repo
├── certificates/                    # PDF certificates linked from timeline
├── static/                          # Static hero/about assets
├── manim/                           # Python scenes that generate blog graphics
├── media/                           # Manim output dump (images/videos, ignored by posts)
├── _site/                           # Jekyll build output (do not edit; auto-generated)
├── Gemfile / Gemfile.lock           # Ruby dependencies
└── README.md                        # This doc
```

## Local Development

Prerequisites: Ruby (≥ 3.x recommended), Bundler, and optionally a Python environment for Manim.

```bash
bundle install
bundle exec jekyll serve --livereload
# Visit http://127.0.0.1:4000
```

Build the static site (useful for deployment previews):

```bash
bundle exec jekyll build
```

## Writing Posts

1. Create `_posts/YYYY-MM-DD-title.md` with front matter:

   ```yaml
   ---
   layout: post
   title: "Your Title"
   date: 2025-03-16
   categories: [ml]
   description: Optional SEO summary
   inspired_by: Claude Monet # optional overlay credit for cards
   last_modified_at: 2025-03-20 # optional, uses git history if omitted
   thumbnail: /assets/images/posts/2025/example/cover.webp # optional
   ---
   ```

2. Write Markdown content. MathJax is enabled for LaTeX:
   - Inline: `$a^2 + b^2 = c^2$`
   - Display: `$$\int_a^b f(x)\,dx$$`

3. Images:
   - Store permanent assets under `assets/images/posts/<year>/<slug>/`
   - Reference with `![Alt]({{ site.baseurl }}/assets/images/posts/2025/example/plot.webp)`
   - Post layout wraps images with a lightbox; clicking opens a full-size view.

4. Optional metadata:
   - `last_modified_at`, `updated`, or `edited` triggers the “Updated” badge.
   - `thumbnail`, `cover_image`, `image`, or `featured_image` feed the blog cards; otherwise the first `<img>` in the post is used.
   - `inspired_by` (or `artist_inspiration`) prints the “Inspired by …” ribbon on listing cards; leave unset if not needed.

## Visual Assets & Manim

- Python scripts in `manim/` generate graphics referenced throughout machine-learning posts.
- Suggested workflow (macOS):

  ```bash
  brew install cairo pkg-config pango ffmpeg
  python -m venv .venv && source .venv/bin/activate
  pip install manim

  # Example renders
  manim -pqh manim/linear_regression_scene.py LinearRegression --format=png
  manim -pqh manim/logistic_regression.py LogisticRegression --format=png
  ```

- Outputs land in `media/images/<scene>/` or `media/videos/<scene>/`; copy finished assets into `assets/images/posts/...` when ready to publish.

## Front-End Behavior Cheatsheet

- Theme toggle updates `data-theme` on `<html>` and mirrors system dark-mode unless overridden.
- AOS animations auto-disable on touch devices or when `prefers-reduced-motion` is set.
- Hero email icon toggles `aria-expanded`/`aria-pressed` to reveal `#hero-email-message`; preserve markup when editing the social list.
- Code blocks get a copy button (`.code-copy-btn`) injected by `_layouts/default.html`.
- Blog cards (`blogs.html`) rely on `data-href` plus JS to open on click/Enter and replay AOS animations; maintain `role="link"` and `tabindex="0"`.
- Navbar gains a “scrolled” class after 50px to adjust shadows.
- The 404 rocket listens for click/keyboard events and can be tuned via the `CONFIG` object (exposed helpers: `setRocketExitOffset`, `setRocketExitMode`).

## Deployment Notes

- Hosted at https://taemincode.github.io (`baseurl` left empty).
- GitHub Pages can build the site directly; commit only source files (never `_site/`).
- The RSS feed (`jekyll-feed`) and SEO tags (`jekyll-seo-tag`) activate automatically when layouts include `{% seo %}` (head already prepared).

## License

No license file is included. All rights reserved unless a license is added.

## Author

Taemin Park — https://github.com/taemincode
