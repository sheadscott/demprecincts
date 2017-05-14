from flask_mail import Message
from flask import render_template
from app import mail
from config import ADMINS

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

def send_contact_notification(user, msg):
    name = user.first_name + user.last_name
    send_email("demprecincts.org",
                ADMINS[0],
                [ADMINS[0]],
                render_template("contact_email.txt.j2",
                               user=user, msg=msg),
               render_template("contact_email.html.j2",
                               user=user, msg=msg))
