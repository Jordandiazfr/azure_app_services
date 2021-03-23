import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from validate_email import validate_email
import os

load_dotenv(dotenv_path="./secrets/.env")


class MailSender():
    def __init__(self):
        self.sender_address = os.getenv("MAIL")
        self.sender_pass = os.getenv("MAIL_PASS")

    def send(self, receiver_address: str, content: str):
        mail_content = """As everyday new players start to beat their records, we present you their latest scores {0}""".format(
            content)

        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = self.sender_address
        message['To'] = receiver_address

        # The subject line
        message['Subject'] = 'The latest scores! .'
        # The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))

        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        # login with mail_id and password
        session.login(self.sender_address, self.sender_pass)
        text = message.as_string()
        session.sendmail(self.sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')

    def validate(self, receiver_address: str):
        is_valid = validate_email(email_address=receiver_address, check_format=True, check_blacklist=True, check_dns=True, dns_timeout=10,
                                  check_smtp=True, smtp_timeout=10, smtp_helo_host='my.host.name', smtp_from_address='my@from.addr.ess', smtp_debug=False)
        return is_valid
