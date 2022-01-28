import pyautogui
import time
open_chrome=pyautogui.locateCenterOnScreen('assets\chrome.PNG',confidence=0.7)
time.sleep(2)
pyautogui.click(open_chrome)
time.sleep(1)
for i in range(0,10):
    pyautogui.rightClick(x=900, y=460)
    time.sleep(1)
    pyautogui.typewrite('v')
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl','tab')
    time.sleep(1)
