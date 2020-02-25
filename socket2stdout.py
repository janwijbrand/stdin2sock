#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import socket
import sys

ADDRESS = "0.0.0.0"
PORT = 31337
CHUNK = 2048

chunks_received = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    print(f'Connected to {ADDRESS}:{PORT}', file=sys.stderr)
    client.connect((ADDRESS, PORT))
    while True:
        try:
            data = client.recv(CHUNK)
            chunks_received += 1
            if not data:
                print(f'No more data', file=sys.stderr)
                break
            sys.stdout.buffer.write(data)
        except Exception as e:
            print(f'Exception {e}', file=sys.stderr)
            break
print(f'Socket closed', file=sys.stderr)
print(f'Received {chunks_received * CHUNK} bytes of data', file=sys.stderr)
