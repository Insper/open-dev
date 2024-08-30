import configparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging 
logging.basicConfig(filename='enviar_email.log', level=logging.INFO)

class Email():

    def __init__(self):
        parser = configparser.ConfigParser()
        parser.read("email_config.txt")

        self.my_address = parser.get("user", "address")
        self.password = parser.get("user", "password")
        self.host = parser.get("server", "host")
        self.port = int(parser.get("server", "port"))

    def enviar(self, email_destino, subject, arquivo_mensagem):

        try:
            print(f'Iniciando conexao com {self.host}:{self.port}')
            s = smtplib.SMTP(host=self.host, port=self.port)
            logging.info(f'Iniciando conexao com {self.host}:{self.port}')
            s.starttls()
            logging.info(f'Fazendo logging com {self.my_address}')
            s.login(self.my_address, self.password)
            logging.info('Logging feito')

            msg = MIMEMultipart()
            msg['From']=self.my_address
            msg['To']=email_destino
            msg['Subject']= subject

            with open(arquivo_mensagem) as f:
                lines = f.readlines()
            message = ' '.join(lines)
            msg.attach(MIMEText(message, 'html'))

            logging.info(f'Email montado para enviar para {email_destino}')
            s.send_message(msg)
            logging.info(f'O email para {email_destino} foi enviado.')
            del msg
        except Exception as e:
            print(f'O email para {email_destino} nao foi enviado.')
            logging.info(f'O email para {email_destino} nao foi enviado: {str(e)}')
