import socket

host = "127.0.0.1"
port = 3000
sock = (host, port)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(sock)
    while True:
        msg = input('message : ')
        data = msg.encode()
        client.send(data)

    client.close()