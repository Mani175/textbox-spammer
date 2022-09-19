import pyautogui
import time
message = "msg here" # message to spam
while True:
  time.sleep(3.5) # here's the delay you can change it, this is good in my opinion
  pyautogui.moveTo(0,0) # type the text box X and Y here
  pyautogui.leftClick() # click the textbox to type in
  pyautogui.hotkey('ctrl','a') 
  pyautogui.press('backspace') # clean the text box if it has any text in it
  for i in message:
    pyautogui.typewrite(i) # make it realistic by typing like a normal human
  pyautogui.leftClick() # making sure mouse is interacting with the text box
  pyautogui.press("enter") # sending the message
