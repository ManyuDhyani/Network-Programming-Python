from concurrent.futures import thread
import queue
import socket
import threading
from queue import Queue

<<<<<<< HEAD
target = "Some URL or IP address"

=======
>>>>>>> 46ab915da20858d0a038a8cbaaeef7c1743e7d79

queue = Queue()
open_ports = []

def portScan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Para in bracket means(Internet socket and not UNiX socket, TCP protocol instead of UDP)
        sock.connect((target, port))
        return True
    except:
        return False

# This for loop in slow so we can use Multithreading.
# Multithreading can be also inefficient as it can check same more than Once.
# SO will use threading with Queue.

# for port in range(1, 1024):
#     result = portScan(port)
#     if result:
#         print("Port {} is open!".format(port))
#     else:
#         print("Port {} is closed!".format(port))


def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portScan(port):
            print("Port {} is open!". format(port))

port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

# Define no. of threads
for t in range(500):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

# To start the Threads in the list
for thread in thread_list:
    thread.start()

# We need the Thread List so that we can wait for all the threads to finish
for thread in thread_list:
    thread.join()
    # join() waits until thread is done

print("Open ports are: ", open_ports)