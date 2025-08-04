# Taemin Park's Homepage

A personal homepage built with HTML, CSS, and JavaScript, optimized for GitHub Pages deployment.

## 🚀 Live Site

Visit the live site at: `https://taemincode.github.io/homepage/`

## 📁 Project Structure

```
/
├── index.html          # Homepage
├── about.html          # About page
├── playlist.html       # Music playlist page
├── static/            
│   ├── styles.css      # Custom styles
│   ├── main.png        # Hero background image
│   └── about-photo.jpg # About page photo
├── app.py             # Original Flask app (for local development)
├── templates/         # Original Flask templates (for reference)
└── README.md          # This file
```

## 🛠️ GitHub Pages Setup

This project is configured for GitHub Pages deployment. The static HTML files are in the root directory for direct serving.

### Deployment Steps:

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Setup for GitHub Pages"
   git push origin main
   ```

2. **Enable GitHub Pages:**
   - Go to your repository settings
   - Scroll to "Pages" section
   - Source: Deploy from a branch
   - Branch: `main`
   - Folder: `/ (root)`
   - Click "Save"

3. **Access your site:**
   - Your site will be available at: `https://[username].github.io/[repository-name]/`
   - For example: `https://taemincode.github.io/homepage/`

## 🔧 Local Development & Testing

### Option 1: Simple File Opening (Quick Test)
For quick testing, simply double-click `index.html` or open it in your browser:
```bash
# On macOS
open index.html

# On Windows
start index.html

# On Linux
xdg-open index.html
```

### Option 2: Local HTTP Server (Recommended)
Use a local server to properly test all features (recommended for accurate testing):

```bash
# Using Python (most common)
python3 -m http.server 8000
# Then visit: http://localhost:8000

# Using Python 2 (if needed)
python -m SimpleHTTPServer 8000

# Using Node.js
npx serve .
# Then visit: http://localhost:3000

# Using PHP
php -S localhost:8000
```

### Option 3: Live Server Extension (Best for Development)
**VS Code Live Server** - Automatic browser refresh when you save files:

#### Installation:
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X / Cmd+Shift+X)
3. Search for "Live Server" by Ritwick Dey
4. Click "Install"

#### Usage:
**Method 1 - Right-click:**
1. Right-click on `index.html` in VS Code
2. Select "Open with Live Server"
3. Your browser will automatically open to `http://127.0.0.1:5500`

**Method 2 - Status Bar:**
1. Open any HTML file in VS Code
2. Click "Go Live" in the bottom status bar
3. Browser opens automatically

**Method 3 - Command Palette:**
1. Press `Ctrl+Shift+P` (Cmd+Shift+P on Mac)
2. Type "Live Server: Open with Live Server"
3. Press Enter

#### Benefits:
- ✅ **Auto-refresh:** Browser updates instantly when you save changes
- ✅ **Easy setup:** One-click to start
- ✅ **Multiple devices:** Access from phone/tablet using your local IP
- ✅ **Port management:** Automatically finds available ports

#### To Stop Live Server:
- Click "Port: 5500" in the status bar, or
- Right-click in editor → "Stop Live Server"

### ❌ No More Flask Commands
Since this is now a static site, you **don't need** these anymore:
```bash
# ❌ Don't use these commands anymore:
flask run
python app.py
```

## 📱 Features

- **Responsive Design:** Works on desktop, tablet, and mobile
- **Modern UI:** Clean, professional design with hover effects
- **Interactive Elements:** Navigation underlines, toast notifications
- **Social Integration:** GitHub profile link in footer
- **Performance Optimized:** Lazy loading images, efficient CSS

## 🎨 Customization

### Updating Content:
- **Homepage:** Edit `index.html`
- **About Page:** Edit `about.html` 
- **Playlist:** Edit `playlist.html`
- **Styles:** Edit `static/styles.css`

### Adding New Pages:
1. Create new HTML file in root directory
2. Follow the same structure as existing pages
3. Update navigation links in all pages
4. Add any new styles to `static/styles.css`

## 🌟 Technologies Used

- **HTML5:** Semantic markup
- **CSS3:** Custom properties, Flexbox, Grid
- **JavaScript:** Vanilla JS for interactions
- **Bootstrap 5.3.0:** UI components and responsive grid
- **GitHub Pages:** Static site hosting

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

- **GitHub:** [@taemincode](https://github.com/taemincode)
- **Website:** [taemincode.github.io/homepage](https://taemincode.github.io/homepage/)

---

*Built with ❤️ by Taemin Park*
