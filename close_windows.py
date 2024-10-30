import pygetwindow as gw
import time
from pywinauto.application import Application

# Function to close all open windows
def close_all_windows():
    # Get a list of all open windows
    windows = gw.getAllTitles()
    
    # Loop through all open windows and close them
    for window_title in windows:
        try:
            # Connect to the window and close it
            app = Application().connect(title=window_title)
            app.window(title=window_title).close()
            print(f"Closed: {window_title}")
        except Exception as e:
            print(f"Could not close {window_title}: {e}")

if __name__ == "__main__":
    # Delay to allow the user to see the output before closing windows
    print("Closing all open windows in 5 seconds...")
    time.sleep(5)  # 5 seconds delay
    close_all_windows()
