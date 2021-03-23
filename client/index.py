from flask import Flask, render_template, request
from client.server.dbclass import PostGreSQL
from client.server.mail import MailSender
app = Flask(__name__)
db = PostGreSQL()
mail = MailSender()


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
    mail.send(user_mail, scores)
    return render_template("dataset.html", data=user_mail, score=scores)
