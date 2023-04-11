### E-MAIL ###
# checagem 2 fatores (tem que ativar pelo servidor de e-mail antes)

# app password (para locais que não possuem autenticação de dois fatores)
# Em alguns servidores (como google mail), é possível gerar um "app password".


from email.message import EmailMessage
from AbaSenha import app_password  #Onde AbaSenha é uma aba python com a senha em forma de variável "app_password"
import ssl
import smtplib

email_sender = "exemplo@email.com"
email_senha = app_password

email_receiver = "temporario@server.com"

assunto = "Mensagem de email"
corpo = "Olá! Este é o corpo da mensagem!"

eM = EmailMessage()
eM["De"] = email_sender
eM["Para"] = email_receiver
eM["Assunto"] = assunto
eM.set_content(corpo)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_senha)
    smtp.sendmail(email_sender, email_receiver, eM.as_string())

