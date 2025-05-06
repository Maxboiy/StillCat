import os
import pyautogui
import time
import random
import json

with open("config.json", "r") as f:
    data = json.load(f)   

last_location = 0
stand_still = 0
moving_mouse = True
cats_deployed = 0
for config in data["config"]:
    stand_still_number = config["stand_still"]
    max_cats_deployed = config["max_deployed_cats"]
    # stand_still_wait = config["stand_still_wait"]
    if config["custom_file_dir"] == None:
        catpath = "F:\A innoncent program\Cats"
    else: 
        catpath = config["custom_file_dir"]

os.system("cls")
print("a MBD project, StillCat [Version 0.1]")
print("Early release!\n")
while True:
    time.sleep(0.5)
    cursor_location = pyautogui.position()
    # Prints out cursor coordinates and if the cursor is moving. If the cursor hasn't moved this section will report for how long
    # Aka it prints out the current status for varibles
    print("============Start============")
    print(cursor_location) # Current cursor location
    print(cats_deployed) # How many cat picture has been opened
    print(max_cats_deployed) # How many cat pictures can be opened before the program closes
    print(stand_still_number) # How long you have to wait before a cat is deployed
    print(moving_mouse) # If the mouse is moving
    if moving_mouse == False:
        print(stand_still) # How long the mouse has been at these coordinates
    
    # If the max_cats_deployed number is the same as cats_deployed than the program self-destructs or just closes
    if cats_deployed == max_cats_deployed:
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
            print("Stand still counter has not been effected!")
        else:
            stand_still = 0
            print("Stand still counter has been reset!")
    
    # If the mouse has been standing still for around 10 seconds the counter will reset back to 0 and it will start all over again!
    if stand_still == stand_still_number:
        print("Mouse has been standing still for 10 seconds")
        stand_still = 0
        print("stand_still counter has been reset!")
        print("Deploying cat picture")
        random_file = random.choice(os.listdir(catpath))
        file_dir = os.path.join(catpath,random_file)
        os.startfile(file_dir)
        cats_deployed = cats_deployed + 1
        print("deployed cat counter has been updated!")