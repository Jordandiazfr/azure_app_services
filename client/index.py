from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", jojo="You found the secret")


@app.route("/jojo")
def jojofunction():
    return "Hello Jojo"
