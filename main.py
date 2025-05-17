import os
import pyautogui
import time
import random
import json
from tkinter import messagebox
import keyboard
import sys

# This value can be ignored and will only change when your config.json file can't be found!
jsonerror = False

temp_folder = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

try:
    with open("config.json", "r") as f:
        data = json.load(f)   

except FileNotFoundError:
    stand_still_number = 10
    max_cats_deployed = 2
    catpath = os.path.join(temp_folder, "Cats") 
    jsonerror = True

last_location = 0
stand_still = 0
moving_mouse = True
cats_deployed = 0
random_stand_still = False
rss_br = 5 # Random_stand_still_begin_range
rss_er = 10 # Random_stand_still_end_range
initial_wait_time = 0
enable_random_deployment = False
random_deployment = False

# The configs 
if jsonerror == True:
    print("============Logs============")
    print("WARNING: config.json file not file! Resulting to default variables!")
else:
    for config in data["config"]:
        if config["stand_still"] == None:
            stand_still_number = 10
        else:
            stand_still_number = config["stand_still"]
        if config["max_deployed_cats"] == None:
            max_cats_deployed = 2
        else:
            max_cats_deployed = config["max_deployed_cats"]
        if config["custom_file_dir"] == None:
            catpath = os.path.join(temp_folder, "Cats")  
        else: 
            catpath = config["custom_file_dir"]
        if config["initial_wait_time"] > 0:
            initial_wait_time = config["initial_wait_time"]
        else: 
            initial_wait_time = initial_wait_time
        if config["enable_random_deployment"] == True:
            random_deployment = random.randrange(1,10)
            enable_random_deployment = True

    for rsidc in data["random_time_stuff"]:
        if rsidc["random_stand_still"] == True:
            if rsidc["begin_range"] > 0:
                rss_br = rsidc["begin_range"]
            if rsidc["end_range"] > 0:
                rss_er = rsidc["end_range"]
            random_stand_still = True
            stand_still_number = random.randrange(rss_br, rss_er)

print("a MBD project, StillCat [Version 0.1]")
print("Early release!\n")
while True:
    if initial_wait_time > 0:
        print("============Initial_wait============")
        print(f"Initial wait has been set to True!\n the initial waiting time is {initial_wait_time}\nAfter the this initial waiting time the program will continue as usual")
        time.sleep(initial_wait_time)
        initial_wait_time = 0
    time.sleep(0.5)
    cursor_location = pyautogui.position()
    # Prints out cursor coordinates and if the cursor is moving. If the cursor hasn't moved this section will report for how long
    # Aka it prints out the current status for varibles
    print("============Start============")
    print(cursor_location) # Current cursor location
    print(cats_deployed) # How many cat picture has been opened
    print(max_cats_deployed) # How many cat pictures can be opened before the program closes
    print(stand_still_number) # How long you have to wait before a cat is deployed
    print(catpath) # Cats folder / Picture folder
    print(random_stand_still) # If the random_stand_still is set to True or False
    if random_stand_still == True:
        print(rss_br, rss_er) # Informs the user about their custom range or default one
    print(enable_random_deployment) # If the random deployment function is enabled
    if enable_random_deployment == True:
        print(random_deployment)
    print(moving_mouse) # If the mouse is moving
    if moving_mouse == False:
        print(stand_still) # How long the mouse has been at these coordinates
    
    # The keybind to terminate this program
    if keyboard.is_pressed("ctrl+k"):
        print("Keybind pressed")
        messagebox.showinfo("StillCat", "The deployed cats have been terminated! Script has stopped\n Press OK to close this program")
        break # Also for some weird reason after pressing this keybind the console clears itself?? 
    else: 
        print("Keybind not pressed")

    # If the max_cats_deployed number is the same as cats_deployed than the program self-destructs or just closes

    if max_cats_deployed > 0:
        print("1")
        if cats_deployed == max_cats_deployed:
            print("Quiting program...")
            break

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
    
    # Deploys the random cat just to rub salt in the wound
    if enable_random_deployment == True:
        if stand_still == random_deployment:
            print("============Random_cat_deployment============")
            print("Random cat deployed!")
            random_file = random.choice(os.listdir(catpath))
            file_dir = os.path.join(catpath,random_file)
            os.startfile(file_dir)
            random_deployment = random.randrange(1,10)

    # If the mouse has been standing still for around 10 seconds the counter will reset back to 0 and it will start all over again!
    if stand_still == stand_still_number:
        print("============Cat_deployed============")
        stand_still = 0
        print("stand_still counter has been reset!")
        random_file = random.choice(os.listdir(catpath))
        file_dir = os.path.join(catpath,random_file)
        os.startfile(file_dir)
        print("Deployed cat picture")
        cats_deployed = cats_deployed + 1
        print("deployed cat counter has been updated!")
        if random_stand_still == True:
            stand_still_number = random.randrange(rss_br, rss_er)
            print("New number has been assigned to stand_still_number!")
        if enable_random_deployment == True:
            random_deployment = random.randrange(1,10)
            print("Random_deployment has been assigned a new number")
