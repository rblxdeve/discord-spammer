import pygetwindow as gw
import pyautogui
import time
# Find the Discord window by its title
discord_window = gw.getWindowsWithTitle('Discord')[0]

# Activate the Discord window
discord_window.activate()
while True:
    pyautogui.typewrite("nuts")
    pyautogui.press('return')
    time.sleep(1)
