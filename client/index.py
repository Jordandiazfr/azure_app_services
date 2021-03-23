from flask import Flask, render_template, request
from client.server.dbclass import PostGreSQL
from client.server.mail import MailSender
from prettytable import PrettyTable
import pandas as pd

# Instances
x = PrettyTable()
app = Flask(__name__)
db = PostGreSQL()
mail = MailSender()


# Routes
@app.route("/")
def index():
    return render_template("index.html", jojo="You found the secret")


@app.route("/jojo")
def jojo_function():
    return "Hello Jojo"


@app.route("/mailhandler", methods=['POST', 'GET'])
def mail_handler():
    scores = db.select("score")
    user_mail = request.form.get("myMail")
    valid = mail.validate(user_mail)
    print(valid)
    # mail.send(user_mail, scores)
    if valid:
        return render_template("nice.html", user=user_mail, score=scores)
    else:
        return render_template("invalid.html")
