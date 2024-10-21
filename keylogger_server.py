import socket

# Define server address and port
SERVER_ADDRESS = '0.0.0.0'  # Listen on all interfaces
SERVER_PORT = 9999  # Choose a port number

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
server_socket.listen(5)

print(f'Server listening on {SERVER_ADDRESS}:{SERVER_PORT}')

while True:
    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print(f'Connection from {client_address}')

    # Receive data from the client
    while True:
        data = client_socket.recv(1024)
        if not data:
            break  # Exit if no data
        print(data.decode('utf-8'))  # Print received data

    client_socket.close()
