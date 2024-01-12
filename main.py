import pyautogui
import keyboard

def click():
    pyautogui.click()

while True:
    if keyboard.is_pressed("CTRL"):
        click()