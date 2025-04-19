from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "random_secret_key"

@app.route("/", methods=["GET", "POST"])
def index():
    if "counter" not in session:
        session["counter"] = 0
    if request.method == "POST":
        session["counter"] += 1
    return render_template("index.html", counter=session["counter"])

if __name__ == "__main__":
    app.run(debug=True)
    print("Running on : http://127.0.0.1:5000/")
