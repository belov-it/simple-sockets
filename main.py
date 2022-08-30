
import socket


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #AF_INET - tcp/ip, SOCK_STREAM - tcp
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print(request)
        print()
        print(addr)

        client_socket.sendall("Hello world".encode())
        client_socket.close()


if __name__ == '__main__':
    run()
