from Action import MouseAction

import pyautogui
from pynput.mouse import Listener 
import pyperclip

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


with Listener(on_click = on_click, on_scroll = on_scroll) as listener:
    listener.join()
    
inp = int(eval(input("How many times would you like to do the action?")))

pyautogui.moveTo(allActions[0].getPosition()[0], allActions[0].getPosition()[1], duration=1)
pyautogui.click(button= (allActions[0].getButton().split('.'))[1])

for i in range(inp):
    for index in range(1, len(allActions)):
        
        action = allActions[index]
        if action.actionType == "click":
            pyautogui.moveTo(action.getPosition()[0], action.getPosition()[1], duration=1)
            pyautogui.click(button= (action.getButton().split('.'))[1])
        if action.actionType == "scroll":
            pyautogui.scroll(action.getSpeed()[1]*100, x=action.getPosition()[0], y=action.getPosition()[1])
            
