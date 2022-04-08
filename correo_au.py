
import smtplib, ssl
import getpass

username = input("Ingrese usuario: ")
password = getpass.getpass("Ingrese su password: ")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(username, password)
    print("Inicio sesion")
    destinatario=input("Ingrese el destinatario")
    mensaje=input("Ingrese el mensaje: ")
    server.sendmail(username, destinatario, mensaje)
    print("Mensaje enviado")
