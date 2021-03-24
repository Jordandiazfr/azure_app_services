from flask import Flask, render_template, request, Markup
from client.server.dbclass import PostGreSQL
from client.server.mail import MailSender
import logging
from client.logger import log

# Instances
app = Flask(__name__)
db = PostGreSQL()
mail = MailSender()


# Routes

@app.route("/")
@log
def index():
    return render_template("index.html", jojo="You found the secret")


@app.route("/jojo")
@log
def jojo_function():
    return "Hello Jojo"


@app.route("/mailhandler", methods=['POST', 'GET'])
@log
def mail_handler():
    scores = db.select("score")
    user_mail = request.form.get("myMail")
    valid = mail.validate(user_mail)
    html_mail = mail.format_html(scores)
    print(valid)
    mail.send(user_mail, content_plain=scores, content_html=html_mail)
    if valid:
        logging.info(f"Email sent successfully to {user_mail}")
        return render_template("nice.html", user=user_mail, data=Markup(html_mail))
    else:
        return render_template("invalid.html")
