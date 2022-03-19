import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 25)#587

"""
    Use the EHLO command to identify the domain name of the 
    sending host to SMTP before you issue a MAIL FROM command. 
    Rule: Send the EHLO command once before a MAIL FROM command.
"""
server.ehlo()

with open('pswd.txt', 'r') as f:
    password = f.read()

server.login('manyudhyani@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'Manyu Dhyani'
msg['To'] = 'manyudhyanipankaj@gmail.com'
msg['Subject'] = "Just A Test"

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))