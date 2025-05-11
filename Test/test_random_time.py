import random
import time
import pyautogui

# Less bloated version of StillCat using a random waiting time
# and with a lot less features

last_location = 0
stand_still = 0
moving_mouse = True
cats_deployed = 0
stand_still_number = random.randrange(2, 10)

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
        print("============Deploy-cat-menu============")
        print("Mouse has been standing still for 10 seconds")
        stand_still = 0
        print("stand_still counter has been reset!")
        print("This is a test program so just imagine if this program deployed a cat picture")
        cats_deployed = cats_deployed + 1
        print("deployed cat counter has been updated!")
        stand_still_number = random.randrange(2, 10)
        print("Stand_still_number has also been assigned a new number")