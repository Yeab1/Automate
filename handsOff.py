import pyautogui
from pynput.mouse import Listener 
import pyperclip

allActions = []

def on_click(x,y, button, pressed):
    if pressed:
        print("Clicked: ", x, y, button)
        if str(button) == "Button.left" or str(button) == "Button.right":
            allActions.append(["click",x,y,str(button)])
        if str(button) == "Button.middle":
            return False
        
def on_scroll(x,y,dx,dy):
    allActions.append(["scroll",x,y,dx,dy])
    
with Listener(on_click = on_click, on_scroll = on_scroll) as listener:
    listener.join()
    
print(allActions)

inp = int(eval(input("How many times would you like to do the action?")))
x = 0
for i in range(inp):
    for index in range(1, len(allActions)):
        
        action = allActions[index]
        if x == 0:
            pyautogui.moveTo(allActions[0][1], allActions[0][2], duration=0.1)
            pyautogui.click(button= "left")
            x+=1
        if action[0] == "click":
            pyautogui.moveTo(action[1], action[2], duration=1)
            pyautogui.click(button= (action[3].split('.'))[1])
        if action[0] == "scroll":
            pyautogui.scroll(action[4]*100, x=action[1], y=action[2])