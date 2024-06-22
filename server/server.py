import socket

host = "127.0.0.1"
port = 3000
sock = (host, port)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(sock)
    server.listen()
    conn, addr = server.accept()
    print(f'Conection from {addr}')
    while conn:
        msg = conn.recv(1024)
        if msg:
            print(msg.decode())
        else:
            break
    server.close()