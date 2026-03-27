from flask import Flask, render_template, request
from core import run_pipeline  # your system entry

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/run", methods=["POST"])
def run():
    data = {
        "query": request.form.get("query"),
        "platform": request.form.get("platform"),
        "budget": int(request.form.get("budget")),
        "audience": request.form.get("audience"),
        "awareness": request.form.get("awareness")
    }

    result = run_pipeline(data)

    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)