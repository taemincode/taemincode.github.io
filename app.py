from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/cs50")
def cs50():
    return render_template("cs50.html")

@app.route("/playlist")
def playlist():
    return render_template("playlist.html")

if __name__ == "__main__":
    app.run(debug=True)