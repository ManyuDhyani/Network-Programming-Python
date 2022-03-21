import socket
from unicodedata import name

# s => server socket
# c => client socket

c = socket.socket()

# Only Server will bind the service to a port. 
# Client will only connect to that port for the service.

c.connect(('localhost', 9999))
# In connect we send write the server's ip address and the host
# connect() and bind() function take a single argument, send ip add. and host number in a tuple.

name = input("Enter your name: ")
c.send(bytes(name, 'utf-8'))

print(c.recv(1024).decode())

# In recv() mention buffer size like 1024 bytes