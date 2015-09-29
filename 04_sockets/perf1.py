# time of long running requests

import socket
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 25000))

while True:
    start = time.time()
    s.send(b'30')
    resp = s.recv(512)
    end = time.time()
    print(end-start)
