import os
import time

def open_notepad():
    while True:
        os.system("start notepad.exe")
        time.sleep(0.5)  # Adjust the speed as needed

if __name__ == "__main__":
    open_notepad()
