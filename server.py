import socket

# s => server socket
# c => client socket

s = socket.socket()
# We can pass the type of network and protocol in socket above
# for network it can be ivp4 or 6 and for protocol TCP or UDP
# by default it is Ivp4 and TCP.

print("Socket Created")

s.bind(('localhost', 9999))
# Range for port no. 0 -> 65535

s.listen(3)
print("waiting for connections....")

while True:
    c, address = s.accept()
    print("Connected with", address)

    c.send(bytes("Welcome to the Server", 'utf-8'))

    c.close()