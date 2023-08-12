import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 1242
server.bind(('', port))

server.listen(5)
print('server is listening')

client_socket, addr = server.accept()
print (f'connection established from {addr}')
client_socket.send('welcome to the server'.encode())

client_socket.send('take screenshot'.encode())

path = 'D:\socket_proj\client_screenshot\c_screenshot.png'

file_name = client_socket.recv(1024).decode()
print(file_name)

file_size = client_socket.recv(1024).decode()
print(file_size)

file = open(file_name, mode='wb')
file_bytes = b""

done = False
while not done:
    data = client_socket.recv(1024)
    if file_bytes[-9:] == b"endendend":
        done = True
        print('screenshot received')
    else:
        file_bytes += data

file.write(file_bytes)
file.close()
client_socket.close()


'''while True:
    tmp_data = server.recv(1024)
    if tmp_data == b"endendend":
        print("done")
        break
    data += tmp_data

filename = "client_screenshot"  # name save
file = open(filename, mode="wb")
file.write(data)
file.close()

client_socket.send('screenshot taken from your desktop'.encode())
print('screenshot from a client desktop saved')

client_socket.close()
#break'''
