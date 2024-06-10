from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from os import getenv
import secrets
import string
import hashlib
import mysql.connector
from db import DB

class Mail:
    def __init__(self):
        load_dotenv()
        self.SMTP_PORT = getenv('SMTP_PORT')
        self.SMTP_SERVER = getenv('SMTP_SERVER')
        self.SMTP_LOGIN = getenv('SMTP_LOGIN')
        self.SMTP_PASSWORD = getenv('SMTP_PASSWORD')

    def send_mail(self, l):
        #new password
        alphabet = string.ascii_letters + string.digits
        p = ''.join(secrets.choice(alphabet) for i in range(8))
        #hash
        h = hashlib.new('SHA256')
        h.update(p.encode())
        p_h = h.hexdigest()

        db = DB()
        email = db.get_email_by_login(l)
        msg = MIMEText(f'Ваш новый пароль: {p}')
        msg['Subject'] = 'Новый пароль'
        msg['From'] = self.SMTP_LOGIN
        msg['To'] = email

        server = smtplib.SMTP_SSL(self.SMTP_SERVER, self.SMTP_PORT)
        server.login(self.SMTP_LOGIN, self.SMTP_PASSWORD)
        server.sendmail(self.SMTP_LOGIN, [email], msg.as_string())

        cursor = db.db.cursor()
        cursor.execute(f'UPDATE teachers SET password = \"{p_h}\" WHERE login = \"{l}\"')
        db.db.commit()


