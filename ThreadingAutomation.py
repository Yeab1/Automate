from Actions import Action
import PySimpleGUI as sg
import pyautogui
from pynput.mouse import Listener 
import pyperclip
import threading
from pynput import keyboard

allActions = []

actionDictionary = {
    "caps_lock" : "capslock",
    "shift" : "shiftleft",
    "shift_r" : "shiftright",
    "ctrl_l" : "ctrlleft",
    "crrl_r" : "ctrlright",
    "alt_gr" : "altright",
    "alt_l" : "altleft"
}

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
                


layout = [[sg.Text("AUTOMATION PROJECT", size=(20,1))],
          [sg.Button('Start Recording')],
          [sg.Button('Stop Recording')],
          [sg.Button('Wait')],
          [sg.Input(key = '-input-'), sg.Button('Play')]],

window = sg.Window('Design Pattern 3 - Persistent Window', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == 'Start Recording':
        print("Start Typing")
        mouse = threading.Thread(target = mouseAction)
        keys = threading.Thread(target = keyBoardAction)

        # print statements for debugging and seeing the buttons recorded and their order.
        print("================================ Actions ==================================")
        for action in allActions:
            if action.actionType == "click":
                print(action.getButton())
            elif action.actionType == "keyPress":
                print(str(action.getKey()))
        print("================================ Done ==================================")
        mouse.start()
        keys.start()
        
        
    if event == "Stop Recording":
        mouse.daemon = True
        keys.daemon = True
        mouse.join()
        keys.join()
        
    if event == "Play":
        inp = int(values["-input-"])
        pyautogui.moveTo(allActions[0].getPosition()[0], allActions[0].getPosition()[1], duration=1)
        pyautogui.click(button= (allActions[0].getButton().split('.'))[1])

        for i in range(inp):
            for index in range(1, len(allActions)):
                
                action = allActions[index]
                if action.actionType == "click":
                    pyautogui.moveTo(action.getPosition()[0], action.getPosition()[1], duration=1)
                    pyautogui.click(button= (action.getButton().split('.'))[1])
                if action.actionType == "scroll":
                    pyautogui.scroll(action.getSpeed()[1]*100, x = action.getPosition()[0], y = action.getPosition()[1])
                if action.actionType == "keyPress":
                    keyString = str(action.getKey())
                    if len(keyString) > 3:
                        keyString = keyString.split('.')[1]
                    else:
                        keyString = keyString[1]
                    if keyString in actionDictionary:
                        pyautogui.press(actionDictionary[keyString], interval = 0.5)
                    else:
                        print("new string: ", keyString)
                        pyautogui.press(keyString, interval = 0.5)
    if event is None:
        break
        
window.close()
exit()
                
                
                
                
                
                
                
                
                
                
                
                
                
                
'''          
Testing Area
Please test your actions here so as not to break anything
















'''