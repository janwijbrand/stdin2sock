#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import socket
import sys

ADDRESS = "0.0.0.0"
PORT = 31337
CHUNK = 2048

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ADDRESS, PORT))
server_socket.listen(0)

print(f'Accept connections')
connection, address = server_socket.accept()

print(f'Accepted connection from {address}')
print(f'Start sending data in chunks of {CHUNK}')

with connection:
    while True:
        try:
            data = sys.stdin.buffer.read(CHUNK)
            if not data:
                break
            connection.send(data)
        except BrokenPipeError as e:
            print(f'Connection closed from the other end')
            break
print(f'Socket closed')
