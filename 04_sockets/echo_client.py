# Echo client program
import socket
import os
import random


def get_random_quote():
    return random.choice([line for line in open('quotes.txt', 'rb')])


HOST = '127.0.0.1'    # The remote host
PORT = int(os.environ.get('SERVER_PORT', 25000))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall(get_random_quote())
data = s.recv(1024)
s.close()

print('Received', repr(data))
