import socket
from threading import Thread


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_server(address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    while True:
        client, addr = s.accept()
        print("connection", addr)
        Thread(target=fib_handler, args=(client,)).start()


def fib_handler(client):
    while True:
        data = client.recv(1024)
        if not data:
            break
        try:
            n = int(data)
            result = fib(n)
            response = str(result).encode() + b'\n'
        except ValueError:
            response = b'error!'
        client.send(response)
    print("close.")

if __name__ == '__main__':
    fib_server(('', 25000))
