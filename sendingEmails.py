import smtplib

connection = smtplib.SMTP('smtp.google.com{host here}', 55)
connection.ehlo()

connection.starttls()
connection.login('username', 'password')
connection.sendmail('from_addr', 'to_addr', 'msg')

connection.quit()
