import pyautogui
import keyboard
import time

def move():
    pyautogui.press("W")


while True:
    if keyboard.is_pressed("TAB"):
        move()