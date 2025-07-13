import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
import imghdr

load_dotenv(dotenv_path='.env')

PASSWORD = os.getenv('google_app_password')
SENDER = os.getenv('sender_gmail')
RECEIVER = os.getenv('receiver_gmail')


def send_mail(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New Object was detected around."
    email_message.set_content("Hey, watch out n rm all stuff, smbd is coming in.")

    with open(image_path, 'rb') as file:
        content = file.read()
    
    email_message.add_attachment(content, maintype='image', subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)   
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()