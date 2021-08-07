from Action import MouseAction

import pyautogui
from pynput.mouse import Listener 
import pyperclip
import threading
allActions = []

def on_click(x,y, button, pressed):
    if pressed:
        print("Clicked: ", x, y, button)
        if str(button) == "Button.left" or str(button) == "Button.right":
            newClick = MouseAction("click")
            newClick.setPosition(x, y)
            newClick.setButton(str(button))
            
            allActions.append(newClick)
        if str(button) == "Button.middle":
            return False
        
def on_scroll(x,y,dx,dy):
    newScroll = MouseAction("scroll")
    newScroll.setPosition(x, y)
    newScroll.setSpeed(dx, dy)

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
# ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()

def mouseAction():
    with Listener(on_click = on_click, on_scroll = on_scroll) as listener:
        listener.join()
from pynput import keyboard

def keyBoardAction():
    # Collect events until released
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
            listener.join()

mouse = threading.Thread(target=mouseAction)
keys = threading.Thread(target=keyBoardAction)

mouse.start()
keys.start()
mouse.join()
keys.join()

print("Done")