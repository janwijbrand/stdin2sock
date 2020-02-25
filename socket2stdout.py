#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import socket
import sys

ADDRESS = "0.0.0.0"
PORT = 31337
CHUNK = 2048

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    print(f'Connected to {ADDRESS}:{PORT}')
    client.connect((ADDRESS, PORT))
    while True:
        try:
            data = client.recv(CHUNK)
            if not data:
                print(f'No more data')
                break
            sys.stdout.buffer.write(data)
        except Exception as e:
            print(f'Exception {e}')
            break
print(f'Socket closed')
