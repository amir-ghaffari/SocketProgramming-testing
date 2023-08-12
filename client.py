import socket
from PIL import ImageGrab
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 1242

client.connect(('127.0.0.1', port))

print(client.recv(1024).decode())

msg = client.recv(1024).decode()

if msg == 'take screenshot':

    img = ImageGrab.grab()

    path = "C:\\Users\ghafari\Pictures\Screenshots\screenshot_1.png"
    img.save(path)

    file = open(path, mode="rb")
    file_size = os.path.getsize(path)

    client.send('image.png'.encode())
    client.send(str(file_size).encode())

    data = file.read()
    client.sendall(data)
    client.send(b"endendend")

    file.close()
    print("done")


#server.close()
