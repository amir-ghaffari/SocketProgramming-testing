import socket
import os  # Import the os module
import pyautogui
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 12345
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)
print("Server is listening on port", port)

# Accept a connection from a client
client_socket, address = server_socket.accept()
print("Got connection from", address)

data = client_socket.recv(64).decode()
print('Received "' + data + '"')

client_socket.send("Message Received!".encode())

if data == "1":
    # Receive the file name from the client
    file_name = client_socket.recv(1024).decode()

    file = open(file_name, mode="rb")
    data = file.read()
    file.close()

    # Check if the file exists on the server
    if os.path.isfile(file_name):

        # Send a positive response to the client
        response = f"File {file_name} found on server"
        client_socket.send(response.encode())
        while True:
            if len(data) > 0:
                tmp_data = data[0:1024]
                if len(tmp_data) < 1024:
                    tmp_data += chr(0).encode() * (1024 - len(tmp_data))
                data = data[1024:]

                client_socket.send(tmp_data)
                print(".", end="")
            else:
                client_socket.send(b"endendend")
                print("done")
                # server_socket.close()
                break
    else:

        # Send a negative response to the client
        response = f"File {file_name} not found on server"

        # Send the response to the client
        client_socket.send(response.encode())
if data == "2":
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
        if file_bytes[-9:] == b"<THE_END>":
            done = True
            print('screenshot received')
        else:
            file_bytes += data

    file.write(file_bytes)
    file.close()

if data == "3":
    print('hi')
    # Receive a confirmation message from the client
    msg = client_socket.recv(1024).decode()
    print("Client says:", msg)

    # Get the screen size of the client
    screenWidth, screenHeight = pyautogui.size()

    # Move the mouse to the center of the screen on the client
    pyautogui.moveTo(screenWidth / 2, screenHeight / 2)


# Close the socket
# client_socket.close()
