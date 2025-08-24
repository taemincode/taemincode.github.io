# Taemin Park — Personal Site & Blog

Source for https://taemincode.github.io built with Jekyll, SCSS, MathJax, and Manim visuals.

## Highlights

- Clean, responsive layout (Bootstrap 5, SCSS partials)
- Dark mode toggle with theme persistence
- MathJax for LaTeX math (`$...$` / `$$...$$`)
- Copy-to-clipboard buttons on code blocks
- Manim-generated images/animations for ML/Math posts
- RSS feed and SEO plugin ready

## Tech

- Jekyll 4.x, Kramdown
- SCSS via Jekyll pipeline (`assets/css/site.scss` + `_sass/*`)
- Bootstrap, AOS, Font Awesome (CDN)
- MathJax v3
- GitHub Pages hosting

## Repository layout

```
├── _config.yml              # Site config (url, baseurl, markdown)
├── _layouts/
│   ├── default.html         # Global head, navbar, footer, scripts
│   └── post.html            # Post wrapper (prev/next nav)
├── _posts/                  # Blog posts (YYYY-MM-DD-title.md)
├── assets/
│   ├── css/site.scss        # SCSS entry (imports from _sass)
│   └── images/              # Images used by the site/posts
├── _sass/                   # SCSS partials (base, nav, blog, post, …)
├── manim/                   # Manim Python scripts (scenes)
├── media/                   # Manim render outputs (images/videos)
├── index.html, blogs.html   # Home and blog index
├── Gemfile                  # Ruby deps (jekyll, seo-tag, feed)
└── vendor/                  # Bundler dir (if vendored)
```

Note: `_site/` is Jekyll’s build output and shouldn’t be edited by hand.

## Local development (macOS)

Prereqs: Ruby (>= 3.x recommended) and Bundler.

1) Install gems

```bash
bundle install
```

2) Run the server (with live reload)

```bash
bundle exec jekyll serve --livereload
```

Visit http://127.0.0.1:4000

## Writing posts

1) Create `_posts/YYYY-MM-DD-title.md` with front matter:

```yaml
---
layout: post
title: "Your Title"
date: 2025-03-16
categories: [ml]
description: Optional SEO summary
---
```

2) Use Markdown. MathJax is available:

- Inline: `$a^2 + b^2 = c^2$`
- Display: `$$\int_a^b f(x)\,dx$$`

3) Images: place under `assets/images/…` or `assets/images/posts/…` and reference with `{{ site.baseurl }}` when needed:

```markdown
![Alt text]({{ site.baseurl }}/assets/images/posts/example.png)
```

## Manim: generating visuals

Install system deps and Manim (recommend a Python venv):

```bash
brew install cairo pkg-config pango ffmpeg
python -m venv .venv && source .venv/bin/activate
pip install manim
```

Render scenes from `manim/` (examples):

```bash
# Linear Regression still frame (PNG)
manim -pqh manim/linear_regression_scene.py LinearRegression --format=png

# Logistic Regression still frame (PNG)
manim -pqh manim/logistic_regression.py LogisticRegression --format=png
```

Outputs are written under `media/` (e.g., `media/images/linear_regression_scene/`). Move or reference the generated files from your posts.

## SEO and feeds

The Gemfile includes `jekyll-seo-tag` and `jekyll-feed`.

- To enable full SEO tags, add `{% seo %}` inside `<head>` of `_layouts/default.html`.
- The feed will be available at `/feed.xml` when built.

## Deployment

- Hosted at https://taemincode.github.io
- `baseurl` is empty for a user site; keep it that way unless you serve under a subpath.
- GitHub Pages can build from the default branch. If building locally, commit only sources (not `_site/`).

## License

No license file is included. All rights reserved unless a license is added.

## Author

Taemin Park — https://github.com/taemincode
