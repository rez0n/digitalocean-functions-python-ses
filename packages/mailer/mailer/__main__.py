import os

from ses_mailer import send_email
from template_loader import env


def main(args):
    your_name = args.get("your_name")
    if not your_name:
        return {"body": "pong"}

    mail_to = os.getenv('MAIL_TO')
    template = env.get_template('mail.html')
    html = template.render(name=your_name)

    send_email(mail_subject="mail_subject",
               mail_body=html,
               mail_to=[mail_to],
               )

    return {"body": "email sent"}
