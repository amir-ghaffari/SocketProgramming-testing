import socket
import os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 12456
server_socket.bind((host, port))

server_socket.listen(3)
print("server is listening...")

client_socket, address = server_socket.accept()
print(f"connection established \n" + address)
