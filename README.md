# Taemin Park's Personal Website

This repository contains the source code for my personal website and blog, hosted at [taemincode.github.io](https://taemincode.github.io).

## 🚀 Features

- Personal portfolio and blog
- Responsive design
- Math equation support using MathJax
- Blog posts with categories
- GitHub-style alert boxes
- Image support
- Code syntax highlighting
- Dynamic visualization of machine learning concepts using Manim

## 💻 Technology Stack

- **Static Site Generator**: Jekyll
- **Styling**: Custom CSS
- **Mathematics**: MathJax
- **Visualizations**: Manim (Mathematical Animation Engine)
- **Hosting**: GitHub Pages

## 🎬 Manim Animations

The blog uses Manim (Mathematical Animation Engine) to create beautiful images for explaining mathematical and machine learning concepts. The images are pre-rendered and included in the blog posts.

### Running Manim Locally

1. Install Manim dependencies:
   ```bash
   brew install cairo pkg-config pango ffmpeg
   pip install manim
   ```

2. Generate an animation:
   ```bash
   manim -pqh manim/linear_regression_scene.py LinearRegressionExample --format=png
   ```

The generated animations will be saved in the `media/` directory.

## 💻 Technology Stack

- **Static Site Generator**: Jekyll
- **Styling**: Custom CSS
- **Mathematics**: MathJax
- **Hosting**: GitHub Pages

## 📁 Project Structure

```
taemincode.github.io/
├── _config.yml          # Jekyll configuration
├── _layouts/            # HTML layouts
│   ├── default.html     # Base layout
│   └── post.html        # Blog post layout
├── _posts/             # Blog posts
│   ├── 2025-08-04-welcome-to-my-blog.md
│   └── 2025-08-05-linear-regression.md
├── _site/              # Generated site files
├── assets/             # Static assets
│   └── images/
│       └── posts/      # Blog post images
├── blogs.html          # Blog listing page
├── manim/              # Manim scripts
├── media/              # Generated media files
│   ├── images/         # Generated images from Manim
│   ├── Tex/           # Generated LaTeX files
│   └── videos/         # Generated animation videos
├── static/             # CSS and other static files
│   ├── about.css       # About page styles
│   ├── main.png        # Main header image
│   ├── post.css        # Blog post styles
│   └── styles.css      # Main stylesheet
├── Gemfile            # Ruby dependencies
├── Gemfile.lock       # Ruby dependencies lock file
└── index.html         # Homepage
```

## 🛠 Local Development

1. Install Ruby and Bundler if you haven't already:
   ```bash
   brew install ruby
   gem install bundler
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/taemincode/taemincode.github.io.git
   cd taemincode.github.io
   ```

3. Install dependencies:
   ```bash
   bundle install
   ```

4. Run the development server:
   ```bash
   bundle exec jekyll serve
   ```

5. Open your browser and visit `http://127.0.0.1:4000`

## 📝 Creating New Posts

1. Create a new markdown file in `_posts/` with the format:
   ```
   YYYY-MM-DD-title.md
   ```

2. Add the front matter:
   ```yaml
   ---
   layout: post
   title: "Your Title"
   date: YYYY-MM-DD
   categories: [category1, category2]
   ---
   ```

3. Write your content using Markdown

### Special Features

#### Math Equations
Use single `$` for inline math and double `$$` for display math:
```markdown
Inline: $y = mx + b$
Display: $$y = mx + b$$
```

#### Alert Boxes
Use GitHub-style alerts:
```markdown
> [!NOTE]
> This is a note

> [!TIP]
> This is a tip
```

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

- **Taemin Park**
- GitHub: [@taemincode](https://github.com/taemincode)
