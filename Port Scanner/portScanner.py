import queue
import socket

target = "Some URL or IP Address"

def portScan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Para in bracket means(Internet socket and not UNiX socket, TCP protocol instead of UDP)
        sock.connect((target, port))
        return True
    except:
        return False

for port in range(1, 1024):
    result = portScan(port)
    if result:
        print("Port {} is open!".format(port))
    else:
        print("Port {} is closed!".format(port))


