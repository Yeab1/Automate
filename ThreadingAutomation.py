from Actions import Action
import PySimpleGUI as sg
import pyautogui
from pynput.mouse import Listener 
import pyperclip
import threading
from pynput import keyboard
import time

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

    allActions.append(newScroll)
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
                
# DarkGrey13
sg.theme('DarkGrey13')
layout = [[sg.Text("AUTOMATION PROJECT TEST", size=(25,1), font=('Courier 15'))],
          [sg.Button('Start Recording', font=('Verdana 9')), sg.Button('Stop Recording', font=('Verdana 9'))],
          [sg.Input(key = '-waitTime-'), sg.Button('Wait (in Seconds)', font=('Verdana 9'))],
          [sg.Text("Can't estimate wait time? Just tell me when to start and stop waiting:", size=(60,0), font=('Verdana 9'))],
          [sg.Button('Start Wait', font=('Verdana 9')), sg.Button('Stop Wait', font=('Verdana 9'))],
          [sg.Input(key = '-input-'), sg.Button('Play', font=('Verdana 9'))],
          [sg.Text("", size=(60,0), key='-Errors-', font=('Verdana 9'))]]

window = sg.Window('Automation Project Test Window', layout)
startTime = None
stopTime = None
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
        mouse.join()
        keys.join()
        
    if event == "Stop Recording":
        window['-Errors-'].update("Stop recording button is still under development.")
        
    if event == "Wait (in Seconds)":
        try:
            waitTime = int(values["-waitTime-"])
            currWaitTime = Action("wait")
            currWaitTime.setWaitTime(waitTime)
            allActions.append(currWaitTime)
            
        except (ValueError):
            window['-Errors-'].update("Please insert time to wait in seconds")
            
    if event == "Start Wait":
        print("Started Waiting")
        startTime = time.time()
        
    if event == "Stop Wait":
        stopTime = time.time()
        print("Stopped Waiting")
        
    if startTime and stopTime:   
        calculatedWaitTime = stopTime - startTime
        window['-Errors-'].update("Recorded " + str(round(calculatedWaitTime, 1)) + " seconds of wait time.")
        startTime = None
        stopTime = None
        
        currWaitTime = Action("wait")
        currWaitTime.setWaitTime(calculatedWaitTime)
        allActions.append(currWaitTime)
        
    if event == "Play":
        try:
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
                    if action.actionType == "wait":
                        time.sleep(action.getWaitTime())
            
            # clear previous actions for the next recording
            allActions = []
        except (ValueError):
            window['-Errors-'].update("Please enter number of repititions")
        except (TypeError):
            window['-Errors-'].update("No Recording Found")
        except (IndexError):
            window['-Errors-'].update("No Recording Found")
    if event is None:
        break
        
window.close()
exit()
                
                
                
  
'''
Scratch Area

Introducing wait time
problem, I can't click buttons in UI because of the events running with it.
What if I create another thread for the 

Or read the wait space in seconds after stopping event clickers, then restart recording if there is more to do

make another wait thread that just waits for a specific input?





'''
                
                
                
                
                
                
                
                
                
'''          
Testing Area
Please test your actions here so as not to break anything
















'''