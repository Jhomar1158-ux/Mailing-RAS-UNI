from email.message import EmailMessage 

import smtplib
# import imghdr


def mailingApp(correo,nombre):
    app_pass = "TU-PASSWORD"
    host_user= "TU-CORREO"

    smtp =smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(host_user, app_pass)
    msg = EmailMessage()
    msg['Subject'] = "TITULO DEL EVENTO - ASUNTO"
    msg['From'] = host_user
    msg['To'] = correo
    msg.add_alternative(f""" \n\n
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <main>
            <h1>EVENTOS RAS</h1>
            <p>Estimado {nombre} con correo {correo}, se le invita al evento magistral</p>
            <table>
            <tbody>
                <tr style="height:100px;">
                    <td>
                        Evento 1
                        <a href="https://ibb.co/LC9P2km"><img src="https://i.ibb.co/BgTPSzb/Flyers-IEEE-RAS-UNI-1.png" alt="Flyers-IEEE-RAS-UNI-1" border="0" style="width:90%;" /></a>
                    </td>
                    <td>
                        Evento 2
                        <a href="https://ibb.co/q7VDYLP"><img src="https://i.ibb.co/sbzg9pM/Afiche.png" alt="Afiche" border="0" style="width:90%;"  /></a>
                    </td>
                </tr>
                <tr>
                    <td>
                        Evento 3
                        <a href="https://ibb.co/J3MyzvZ"><img src="https://i.ibb.co/fDPnCkJ/Voluntariado-IEEE.png" alt="Voluntariado-IEEE" border="0" style="width:90%;" /></a>
                    </td>
                    <td>
                        Evento 4
                        <a href="https://ibb.co/T1KcgsW"><img src="https://i.ibb.co/5kYTRPK/bomber.png" alt="bomber" border="0" style="width:90%;" /></a>
                    </td>
                </tr>
            </tbody>
        </table>
        </main>
    </body>
    </html>
    """, subtype="html")
    smtp.send_message(msg)