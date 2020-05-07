import pyautogui
import script.bmscript as bmscript
script = (bmscript.BEEMOVIE_STRINGS)
for x in script.split():
    pyautogui.write(x)
    pyautogui.press("enter")