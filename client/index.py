from flask import Flask, render_template, request, Markup
from client.server.dbclass import PostGreSQL
from client.server.mail import MailSender
from client.logger import log
from time import sleep
import logging
import json

# Instances
app = Flask(__name__)
db = PostGreSQL()
mail = MailSender()


# Routes

@app.route("/")
@log
def index():
    return render_template("index.html", jojo="You found the secret")


@app.route('/logs')
def logs():
    def generate():
        with open('client/logserver.log') as f:
            while True:
                yield f.read()
                sleep(2)

    return app.response_class(generate(), mimetype='text/plain')


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
    print("Email is valid " + valid)
    if valid:
        html_mail = mail.format_html(scores)
        mail.send(user_mail, content_plain=scores, content_html=html_mail)
        logging.info(f"Email sent successfully to {user_mail}")
        return render_template("nice.html", user=user_mail, data=Markup(html_mail))
    else:
        return render_template("invalid.html")
