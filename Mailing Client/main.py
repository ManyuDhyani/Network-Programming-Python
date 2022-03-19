import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 25)

"""
    Use the EHLO command to identify the domain name of the 
    sending host to SMTP before you issue a MAIL FROM command. 
    Rule: Send the EHLO command once before a MAIL FROM command.
"""
server.ehlo()

with open('pswd.txt', 'r') as f:
    password = f.read()
#server = smtplib.SMTP('smtp.example.com', 25)
server.connect("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login('manyudhyani@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'ManyuDhyani'
msg['To'] = 'manyudhyanipankaj@gmail.com'
msg['Subject'] = "Just A Test"

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = '11.JPG'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)

p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('manyudhyani@gmail.com', 'manyudhyanipankaj@gmail.com', text)