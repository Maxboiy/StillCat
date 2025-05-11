import keyboard
import time
from tkinter import messagebox

# This keybind will hopefully kill the program 
# This program will also notify the user to confirm that this program has been terminated!

while True:
    if keyboard.is_pressed("ctrl+k+l"):
        print("Keybind pressed")
        messagebox.showinfo("StillCat", "The cat deployment has been terminated! along with the program\nAtleast after you press OK")
        break
    else: 
        print("Keybind not pressed")
    time.sleep(0.5)