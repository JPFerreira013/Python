import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

def enviar_relatorio():
    # Configurações do servidor de e-mail
    remetente = "seu_email@gmail.com"
    senha = "sua_senha"
    destinatario = "destinatario@email.com"
    assunto = "Relatório Diário"
    
    # Mensagem do e-mail
    mensagem = MIMEMultipart()
    mensagem["From"] = remetente
    mensagem["To"] = destinatario
    mensagem["Subject"] = assunto
    
    # Corpo do e-mail
    corpo = "Olá,\n\nPor favor, encontre anexado o relatório diário.\n\nAtenciosamente,"
    mensagem.attach(MIMEText(corpo, 'plain'))
    
    # Anexando o arquivo de relatório
    with open("relatorio_diario.csv", "rb") as anexo:
        anexo_mime = MIMEBase('application', 'octet-stream')
        anexo_mime.set_payload(anexo.read())
    encoders.encode_base64(anexo_mime)
    anexo_mime.add_header('Content-Disposition', 'attachment; filename="relatorio_diario.csv"')
    mensagem.attach(anexo_mime)
    
    # Enviando o e-mail
    servidor_smtp = "smtp.gmail.com"
    porta = 587
    servidor = smtplib.SMTP(servidor_smtp, porta)
    servidor.starttls()
    servidor.login(remetente, senha)
    texto = mensagem.as_string()
    servidor.sendmail(remetente, destinatario, texto)
    servidor.quit()
    print("E-mail enviado com sucesso.")

# Agendando o envio do e-mail diariamente às 8h da manhã
schedule.every().day.at("08:00").do(enviar_relatorio)

while True:
    schedule.run_pending()
    time.sleep(1)
