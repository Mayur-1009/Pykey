# from pynput.mouse import Listener
#
# def writetofile(x,y):
#     print("position of current mouse (0)".format((x,y)))
#
# with Listener(on_move=writetofile) as l:
#     l.join()

# from pynput.mouse import Listener
#
# # File to store mouse movement logs
# LOG_FILE = "mouse_log.txt"
#
#
# # Function to log mouse movements
# def writetofile(x, y):
#     with open(LOG_FILE, "a") as f:
#         f.write(f"Mouse moved to: {x}, {y}\n")
#     print(f"Mouse moved to: {x}, {y}")  # Optional: Display in console
#
#
# # Start listening to mouse movements
# with Listener(on_move=writetofile) as listener:
#     listener.join()

import pyautogui
import time
import datetime

log_file = "mouse_log.txt"

while True:
    x, y = pyautogui.position()
    with open(log_file, "a") as f:
        f.write(f"{datetime.datetime.now()} - Mouse at ({x}, {y})\n")
    time.sleep(0.5)  # Adjust as needed
