import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
    total_all = cash
    query = {}
    query = db.execute("SELECT symbol, shares FROM portfolio WHERE user_id = ?", session["user_id"])
    stocks = []
    for q in query:
        if q["shares"] > 0:
            for n in range(len(stocks)):
                if stocks[n]["symbol"] == q["symbol"]:
                    stocks[n]["shares"] += q["shares"]
                    break

            else:
                price = lookup(q["symbol"])["price"]
                total = price * q["shares"]
                stocks.append({"symbol": q["symbol"], "shares": q["shares"],
                              "price": usd(price), "total": usd(total)})
                total_all += total

    return render_template("index.html", stocks=stocks, cash=usd(cash), total=usd(total_all))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        symbol = request.form.get("symbol").upper()
        quote = lookup(symbol)
        if not quote:
            return apology("Invalid symbol", 400)
        price = quote["price"]
        shares = request.form.get("shares")
        if not shares.isdigit() or int(shares) < 1:
            return apology("Invalid shares", 400)
        shares = int(shares)
        cash_result = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        if not cash_result:
            return apology("User not found", 400)
        cash = cash_result[0]["cash"]

        # Check for valid input
        if not shares:
            return apology("Missing shares", 400)
        elif lookup(symbol) == "None":
            return apology("Missing shares", 400)
        elif shares < 1 or not isinstance(shares, int):
            return apology("Please enter a valid value", 400)

        # Ensure user has enough cash to afford the stock
        if cash < price * shares:
            return apology("Can't afford")

        # Purchase stock
        db.execute("INSERT INTO transactions (user_id, symbol, shares, time) VALUES (?, ?, ?, CURRENT_TIMESTAMP)",
                   session["user_id"], symbol, shares)

        existing_stock = db.execute(
            "SELECT shares FROM portfolio WHERE user_id = ? AND symbol = ?", session["user_id"], symbol)
        if existing_stock:
            db.execute("UPDATE portfolio SET shares = shares + ? WHERE user_id = ? AND symbol = ?",
                       shares, session["user_id"], symbol)
        else:
            db.execute("INSERT INTO portfolio (user_id, symbol, shares) VALUES (?, ?, ?)",
                       session["user_id"], symbol, shares)

        # Update cash
        db.execute("UPDATE users SET cash = ? WHERE id = ?",
                   cash - price * shares, session["user_id"])

        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/changepassword", methods=["GET", "POST"])
@login_required
def changepassword():
    """Change Password"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        current = request.form.get("current")
        new = request.form.get("new")
        new_again = request.form.get("new(again)")
        hash = db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])[0]["hash"]

        if not new or not new_again or not current:
            return apology("Missing fields", 400)
        if not check_password_hash(hash, current):
            return apology("Invalid password", 400)
        elif new != new_again:
            return apology("New passwords don't match", 400)

        db.execute("UPDATE users SET hash = ? WHERE id = ?",
                   generate_password_hash(new), session["user_id"])

        return redirect("/login")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("changepassword.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    history = db.execute(
        "SELECT symbol, shares, time FROM transactions WHERE user_id = ?", session["user_id"])
    for h in history:
        if h["shares"] > 0:
            h["price"] = usd(lookup(h["symbol"])["price"] * h["shares"])
        else:
            h["price"] = usd(lookup(h["symbol"])["price"] * -h["shares"])
    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        stock = lookup(request.form.get("symbol"))
        if stock:
            return render_template("quoted.html", name=stock["name"], symbol=stock["symbol"], price=usd(stock["price"]))
        else:
            return apology("Stock not found", 400)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    username = request.form.get("username")
    password = request.form.get("password")
    password_again = request.form.get("confirmation")

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Checking for errors
        if not username:
            return apology("must provide username", 400)
        elif not password:
            return apology("must provide password", 400)
        elif password != password_again:
            return apology("passwords don't match", 400)

        # Generate a hash of the password
        hash = generate_password_hash(password)

        # Add User to Database
        existing_user = db.execute("SELECT * FROM users WHERE username = ?", username)
        if existing_user:
            return apology("username is taken", 400)

        # Add User to Database
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)

        # Log user in
        session["user_id"] = db.execute(
            "SELECT id FROM users WHERE username = ?", username)[0]["id"]

        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        symbol = request.form.get("symbol").upper()
        quote = lookup(symbol)
        if not quote:
            return apology("Invalid symbol", 400)
        price = quote["price"]
        shares = request.form.get("shares")
        if not shares.isdigit() or int(shares) < 1:
            return apology("Invalid shares", 400)
        shares = int(shares)
        cash_result = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        if not cash_result:
            return apology("User not found", 400)
        cash = cash_result[0]["cash"]

        if not shares:
            return apology("Missing shares", 400)
        elif lookup(symbol) == "None":
            return apology("Missing shares", 400)
        elif shares < 1 or not isinstance(shares, int):
            return apology("Please enter a valid value", 400)

        if db.execute("SELECT shares FROM portfolio WHERE user_id = ? AND symbol = ?", session["user_id"], symbol)[0]["shares"] < shares:
            return apology("Too many shares", 400)

        db.execute("INSERT INTO transactions (user_id, symbol, shares, time) VALUES (?, ?, ?, CURRENT_TIMESTAMP)",
                   session["user_id"], symbol, -shares)
        db.execute("UPDATE portfolio SET shares = shares - ? WHERE user_id = ? AND symbol = ?",
                   shares, session["user_id"], symbol)
        db.execute("UPDATE users SET cash = ? WHERE id = ?",
                   cash + price * shares, session["user_id"])

        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        symbols = db.execute(
            "SELECT symbol FROM portfolio WHERE user_id = ? AND shares > 0", session["user_id"])
        return render_template("sell.html", symbols=symbols)
