import configparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email():

    def __init__(self):
        parser = configparser.ConfigParser()
        parser.read("email_config.txt")

        self.my_address = parser.get("user", "address")
        self.password = parser.get("user", "password")
        self.host = parser.get("server", "host")
        self.port = int(parser.get("server", "port"))

    def enviar(self, email_destino, subject, arquivo_mensagem):

        s = smtplib.SMTP(host=self.host, port=self.port)
        s.starttls()
        s.login(self.my_address, self.password)

        msg = MIMEMultipart()
        msg['From']=self.my_address
        msg['To']=email_destino
        msg['Subject']= subject

        with open(arquivo_mensagem) as f:
            lines = f.readlines()
        message = ' '.join(lines)
        msg.attach(MIMEText(message, 'html'))

        s.send_message(msg)
        del msg