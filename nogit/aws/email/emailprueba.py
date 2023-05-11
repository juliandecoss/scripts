import os 
import smtplib
EMAIL_ADDRESS='decossjulian@gmail.com'
EMAIL_PASSWORD='Netoesguey2!'
to = ['julian.decoss@konfio.mx', "juligan_2911@hotmail.com"]
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    subject=('Reporte semanal de login')
    body="This is your password: 961133 for the next 20 seconds"
    msg=f'Subject: {subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS, to,msg)



