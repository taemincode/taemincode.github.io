# Taemin Park's Personal Website

Source code for my personal website and blog, hosted at [taemincode.github.io](https://taemincode.github.io). The site is built with [Jekyll](https://jekyllrb.com/), styled with custom CSS, and enhanced with MathJax and Manim-generated visuals for mathematical content.

## 🚀 Features

- Personal portfolio and blog posts
- Responsive design with Bootstrap and custom styles
- Math equation rendering via MathJax
- GitHub-style alert boxes and syntax highlighting
- Dynamic visualizations of machine learning concepts using Manim
- SEO metadata and RSS feed support

## 🛠 Tech Stack

- **Static Site Generator:** Jekyll
- **Styling:** Custom CSS, Bootstrap, AOS, Font Awesome
- **Mathematics:** MathJax
- **Visualizations:** Manim (Mathematical Animation Engine)
- **Hosting:** GitHub Pages

## 📁 Project Structure

```
taemincode.github.io/
├── _config.yml          # Site configuration
├── _layouts/            # HTML layouts
│   ├── default.html     # Base layout
│   └── post.html        # Blog post layout
├── _posts/              # Blog posts (Markdown)
├── assets/
│   └── images/posts     # Images used in posts
├── blogs.html           # Blog listing page
├── index.html           # Homepage
├── manim/               # Manim animation scripts
├── media/               # Generated media from Manim
├── static/              # CSS and other static assets
│   ├── about.css
│   ├── post.css
│   └── styles.css       # Main stylesheet
├── Gemfile              # Ruby dependencies
└── Gemfile.lock         # Dependency lock file
```

## 🧪 Local Development

1. Install Ruby and Bundler.
2. Install dependencies:
   ```bash
   bundle install
   ```
3. Run the development server:
   ```bash
   bundle exec jekyll serve
   ```
4. Visit `http://127.0.0.1:4000` in your browser.

## 🎬 Manim Animations

Manim scripts in the `manim/` directory generate images and animations included in blog posts.

1. Install Manim and its dependencies:
   ```bash
   brew install cairo pkg-config pango ffmpeg
   pip install manim
   ```
2. Render an animation:
   ```bash
   manim -pqh manim/linear_regression_scene.py LinearRegressionExample --format=png
   ```
   Output files are saved in the `media/` directory.

## 📝 Writing Posts

1. Add a new Markdown file in `_posts/` with the format `YYYY-MM-DD-title.md`.
2. Include front matter:
   ```yaml
   ---
   layout: post
   title: "Your Title"
   date: YYYY-MM-DD
   categories: [category1, category2]
   ---
   ```
3. Write your content using Markdown. Use `$` for inline math and `$$` for display math. GitHub-style alert boxes are also supported:
   ```markdown
   > [!NOTE]
   > This is a note.
   ```

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

- **Taemin Park**
- GitHub: [@taemincode](https://github.com/taemincode)
