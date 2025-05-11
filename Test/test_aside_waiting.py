import random
import time
import pyautogui

# Less bloated version of StillCat along with a random image pop-up feature
# and with a lot less features

last_location = 0
stand_still = 0
moving_mouse = True
cats_deployed = 0
stand_still_number = 5
random_deployment = random.randrange(1,10)

while True:
    time.sleep(0.5)
    cursor_location = pyautogui.position()
    # Prints out cursor coordinates and if the cursor is moving. If the cursor hasn't moved this section will report for how long
    # Aka it prints out the current status for varibles
    print("============Start============")
    print(cursor_location) # Current cursor location
    print(random_deployment) # Time before a random cat gets deployed
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
    
    # Deploys the random cat just to rub salt in the wound
    if stand_still == random_deployment:
        print("============Random_cat_deployment============")
        print("Random cat deployed!")
    
    # If the mouse has been standing still for the set amount of time the counter will reset back to 0 and it will start all over again
    # Along with assigning a new number to the random_deployed varible
    if stand_still == stand_still_number:
        print("============Deploy_cat_menu============")
        stand_still = 0
        print("stand_still counter has been reset!")
        random_deployment = random.randrange(1,10)
        if random_deployment > stand_still_number:
            random_deployment = random_deployment - random_deployment
        print("Random_deployment has been assigned a new number")