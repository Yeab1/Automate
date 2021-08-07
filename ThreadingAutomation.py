from Action import MouseAction

import pyautogui
from pynput.mouse import Listener 
import pyperclip
import threading
clicks = []

def mouseAction():
    pass

def keyBoardAction():
    pass

mouse = threading.Thread(target=mouseAction)
keyboard = threading.Thread(target=keyBoardAction)

mouse.start()
keyboard.start()
mouse.join()
keyboard.join()

print("Done")