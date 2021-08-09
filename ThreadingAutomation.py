from Actions import Action

import pyautogui
from pynput.mouse import Listener 
import pyperclip
import threading
from pynput import keyboard

allActions = []

def on_click(x,y, button, pressed):
    if pressed:
        print("Clicked: ", x, y, button)
        
        if str(button) == "Button.middle":
            return False
        else:
            newClick = Action("click")
            newClick.setPosition(x, y)
            newClick.setButton(str(button))
            
            allActions.append(newClick)
                    
def on_scroll(x,y,dx,dy):
    newScroll = Action("scroll")
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
    else:
        keyPressed = Action("keyPress")
        keyPressed.key = key
        allActions.append(keyPressed)

def mouseAction():
    with Listener(on_click = on_click, on_scroll = on_scroll) as listener:
        listener.join()
        
# this is a test
def keyBoardAction():
    # Collect events until released
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
            listener.join()

mouse = threading.Thread(target = mouseAction)
keys = threading.Thread(target = keyBoardAction)

mouse.start()
keys.start()
mouse.join()
keys.join()

print("================================Done==================================")
for action in allActions:
    if action.actionType == "click":
        print(action.getButton())
    elif action.actionType == "keyPress":
        print(str(action.getKey()))
        # print(type(str(action.getKey())))