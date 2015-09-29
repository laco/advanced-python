# request per seq on fast requests
import socket
import time
from threading import Thread


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 25000))


n = 0


def monitor():
    global n
    while True:
        time.sleep(1)
        print(n, 'r/s')
        n = 0

Thread(target=monitor).start()

while True:
    s.send(b'2')
    resp = s.recv(512)
    n += 1
