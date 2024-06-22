import socket
import argparse
import threading
from datetime import datetime

def serverHandler(addr, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((addr, port))
    server.listen()
    print(f'Listening on {addr}:{port}')

    while True:
        conn, client = server.accept()
        print(f'Connection received from {client} at {datetime.now().time()}')
        while conn:
            data = conn.recv(1024)
            if data:
                msg =  data.decode('utf-8')
                print(f'Received Message : {msg}')
            else:
                break
        conn.close()
    server.close()

def clientHandler(addr, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((addr, port))
    while True:
        msg = input(f'Message : ')
        data = msg.encode()
        client.send(data)
    client.close()

def argParser():
    parser = argparse.ArgumentParser(description='TCP based chat application')
    parser.add_argument('-a', '--addr', type=str, help='IP address to bind or connect to', default='127.0.0.1')
    parser.add_argument('-p', '--port', type=int, default=3000, help='Port number to bind or connect to')
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--server', action='store_true', help='Run as server')
    group.add_argument('--client', action='store_true', help='Run as client')

    args = parser.parse_args()
    return(args)

def main():
    args = argParser() 
    if args.server:
        serverHandler(args.addr, args.port)
    else:
        clientHandler(args.addr, args.port)

if __name__ == '__main__':
    main()