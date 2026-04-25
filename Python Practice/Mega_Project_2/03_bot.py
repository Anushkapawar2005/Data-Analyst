import pyautogui
import time
import pyperclip

#step 1: click on the chrome icon at coordinates(1639, 1412)
pyautogui.click(1373, 1045)
time.sleep(1) # wait for 1 second to ensure the click is registered

#step 2: drag the mouse from (1003, 237) to (2187, 1258) to select the text
pyautogui.moveTo(740,198)
pyautogui.dragTo(1833,917, duration=1.0, button='left') # drag for 1 sec

# step 3: copy the selected text to the clipboard
pyautogui.hotkey('ctrl','c')
time.sleep(1) # wait for 1 sec to ensure the copy command is completes

#step 4: retrieve the text from the clipboard and store it in a value
text = pyperclip.paste()

#print the copied text to verify
print(text)