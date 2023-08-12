import socket
from PIL import ImageGrab
import os

# Create a socket object and connect to the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 12345
sock.connect((host, port))


print('please enter what you want to do')
print('1: receiving a file, 2: tacking a screenshot, 3: controlling the mouse')
message = input()
sock.send(message.encode())

if message == "1":
    # Ask the user for the file name to search
    file_name = input("Enter the file name to search: ")

    # Send the file name to the server
    sock.send(file_name.encode())

    # Receive the response from the server
    confirmation = sock.recv(1024).decode()
    print(confirmation)
    response = sock.recv(1024).decode()

    # Print the response
    print("Response from server:", response)

    data = b""
    while True:
        tmp_data = sock.recv(1024)
        if tmp_data == b"endendend":
            print("done")
            break
        data += tmp_data

    filename = input("output name : ")  # name save
    file = open(filename, mode="wb")
    file.write(data)
    file.close()
# Close the socket
if message == "2":

    response = sock.recv(1024).decode()
    print("Response from server:", response)

    msg = sock.recv(1024).decode()
    print(msg)
    if msg == 'take screenshot':
        img = ImageGrab.grab()

        path = "C:\\Users\ghafari\Pictures\Screenshots\screenshot_1.png"
        img.save(path)

        file = open(path, mode="rb")
        file_size = os.path.getsize(path)

        sock.send('image.png'.encode())
        sock.send(str(file_size).encode())

        data = file.read()
        sock.sendall(data)
        sock.send(b"<THE_END>")

        file.close()
        print("done")
elif message == "3":
    # confirm = sock.recv(1024).decode()
    # print(confirm)
    msg = sock.recv(1024).decode()
    print("Server says:", msg)
    # Send a confirmation message to the server
    sock.send("OK, you can control my mouse.".encode())

# sock.close()
