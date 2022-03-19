import smtplib

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
