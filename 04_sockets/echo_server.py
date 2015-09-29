# Echo server program
import socket
import os

HOST = ''
PORT = int(os.environ.get('SERVER_PORT', 25000))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print("binding.")
s.listen(1)
print("listening.")

conn, addr = s.accept()
print('Connected by', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
conn.close()
