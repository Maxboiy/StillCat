import os
import pyautogui
import time
import random
import json
from tkinter import messagebox
import keyboard
import sys

temp_folder = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

try:
    with open("config.json", "r") as f:
        data = json.load(f)   

except FileNotFoundError:
    stand_still_number = 10

last_location = 0
stand_still = 0
moving_mouse = True
cats_deployed = 0
catpath = os.path.join(temp_folder, "Cats") 

# The configs 
for config in data["config"]:
    if config["stand_still"] == None:
        stand_still_number = 10
    else:
        stand_still_number = config["stand_still"]

print("a MBD project, StillCat [Version 0.1]")
print("Early release! Might still be unstable\n")
while True:
    time.sleep(0.5)
    cursor_location = pyautogui.position()
    # Prints out cursor coordinates and if the cursor is moving. If the cursor hasn't moved this section will report for how long
    # Aka it prints out the current status for varibles
    print("============Start============")
    print(cursor_location) # Current cursor location
    print(cats_deployed) # How many cat picture has been opened
    print(stand_still_number) # How long you have to wait before a cat is deployed
    print(moving_mouse) # If the mouse is moving
    if moving_mouse == False:
        print(stand_still) # How long the mouse has been at these coordinates
    
    # The keybind to terminate this program
    if keyboard.is_pressed("ctrl+k+l"):
        print("Keybind pressed")
        messagebox.showinfo("StillCat", "The deployed cats have been terminated! Script has stopped\n Press OK to close this program")
        break # Also for some weird reason after pressing this keybind the console clears itself?? 
    else: 
        print("Keybind not pressed")

    # This checks if the mouse is still in the same coordinates as last time, if it is the stand_still counter will move up and moving_mouse will be set to False
    if cursor_location == last_location:
        print("============No_movement============")
        print("No movement detected!")
        # If you change the time.sleep(0.5) to a higher number or lower one it is recommended to change the value of this one too!
        stand_still = stand_still + 0.5
        moving_mouse = False
    
    # If the mouse has been moving the stand_still counter will reset and the moving_mouse will be set to True
    else: 
        print("============Movement============")
        last_location = cursor_location
        stand_still = 0
        moving_mouse = True
        print("last location =", last_location)
        if stand_still == 0:
            print("Stand still counter was already on 0!")
        else:
            stand_still = 0
            print("Stand still counter has been reset!")
    
    # If the mouse has been standing still for around 10 seconds the counter will reset back to 0 and it will start all over again!
    if stand_still == stand_still_number:
        print("============Cat_deployed============")
        stand_still = 0
        print("stand_still counter has been reset!")
        random_file = random.choice(os.listdir(catpath))
        file_dir = os.path.join(catpath,random_file)
        os.startfile(file_dir)
        print("Deployed cat picture")