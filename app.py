from flask import Flask, render_template, request, redirect, session
from core import run_pipeline
from utils.logger import setup_logger
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

setup_logger()
users = {}
app = Flask(__name__, template_folder="templates")
app.secret_key = "secret123"

# ---------------- HOME → LOGIN ----------------
@app.route("/")
def home():
    return render_template("login.html")

# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = users.get(email)

        if user and user['password'] == password:
            session['user'] = user['name']
            return redirect('/dashboard')
        else:
            return "Invalid credentials ❌"

    return render_template('login.html')
# ---------------- REGISTER ----------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if email in users:
            return "User already exists ❌"

        users[email] = {
            "name": name,
            "password": password
        }

        return redirect('/login')

    return render_template('register.html')
# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html')
    return redirect('/login')

# ---------------- RUN PIPELINE ----------------
@app.route("/run", methods=["POST"])
def run():
    if 'user' not in session:
        return redirect('/login')

    query = request.form.get("query")
    platform = request.form.get("platform")
    budget_value = request.form.get("budget")
    audience = request.form.get("audience")
    awareness = request.form.get("awareness")

    try:
        budget = int(budget_value)
        if budget <= 0:
            return "Please enter a valid budget"
    except:
        return "Invalid budget"

    data = {
        "query": query,
        "platform": platform,
        "budget": budget,
        "audience": audience,
        "awareness": awareness
    }

    from utils.logger import log
    log(f"[WEB] Received input: {data}")

    result = run_pipeline(data)

    return render_template("result.html", result=result)

# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')


if __name__ == "__main__":
    app.run(debug=True)