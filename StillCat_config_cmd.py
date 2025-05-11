from customtkinter import filedialog 
import json
import os
import time

filename = None
max_cat_deployment = 2
stand_still = 10
custom_file_dir = None
initial_wait_time = 0
enable_random_deployment = False
random_stand_still = False
begin_range = 5
end_range = 10
unapplyed_changes = False
ac_iwt = False
ac_erd = False
ac_rss = False
version = "0.1 CMD"

while True:
    print("=========StillCat-configurator=========")
    print(f"Welcome to the StillCat configurator! [Version {version}]\n")
    print("[1] = Choose configuration file")
    print("[2] = Make a configuration file")
    print("[3] = Information about this program")
    print("[4] = Exit\n")
    mainmenu = input("Select >> ")

    if mainmenu == "1":
        filename = filedialog.askopenfilename()
        print("=========StillCat-Config-Menu=========")
        print(f"Editing {filename}\n")
        with open(filename, "r") as f:
            data = json.load(f)
            for config in data["config"]:
                for random in data["random_time_stuff"]:
                    print("=========Current-config=========")
                    print("Maximum amount of pictures =", config["max_deployed_cats"])
                    print(f"Custom picture directory =", config["custom_file_dir"])
                    print(f"How long before opening another picture? (in seconds) =", config["stand_still"]) 
                    print("=========Options=========")
                    print("[1] = Edit configuration file")
                    print("[2] = Reset configuration file to defaults")
                    config_menu = input("Select >> ")
                    if config_menu == "1": 
                        op1 = config["initial_wait_time"]
                        op2 = config["enable_random_deployment"]
                        op3 = random["random_stand_still"]
                        sr = random["begin_range"]
                        er = random["end_range"]
                        while True:
                            os.system("cls")
                            print("=========Configuration_editor=========")
                            print("[1] = The basics")
                            print("[2] = Other features")
                            print("[3] = Back")
                            edit_config_menu = input("Select >> ")
                            if edit_config_menu == "1":
                                print("=========The_basics/max_cat_deployment=========")
                                print("How many cat pictues should be deployed before closing the program?")
                                max_cat_deployment_menu = input("Max_cat_deployment >> (2) ")
                                print("=========The_basics/stand_still=========")
                                print("How long does the mouse have to be at a standstill before deploying a cat?")
                                stand_still_menu = input("stand_still >> (10) ")
                                print("=========The_basics/custom_file_dir=========")
                                print("Do you want to use a custom file directory?\nIf not press enter")
                                custom_file_dir_menu = input("custom_file_dir >> (None) ")
                                if max_cat_deployment_menu == "":
                                    max_cat_deployment_menu = max_cat_deployment
                                else: 
                                    max_cat_deployment_menu = int(max_cat_deployment_menu)
                                if stand_still_menu == "":
                                    stand_still_menu = stand_still
                                else:
                                    stand_still_menu = int(stand_still_menu)
                                if custom_file_dir_menu == "":
                                    custom_file_dir_menu = custom_file_dir
                                else: 
                                    custom_file_dir_menu = int(custom_file_dir_menu)
                                print("=========The_basics/Confirmation=========")
                                print("This will be written to your config.json file\n")
                                print("max_cat_deployment =", max_cat_deployment_menu)
                                print("stand_still =", stand_still_menu)
                                print("custom_file_dir =", custom_file_dir_menu)
                                print("Apply? [y/n]")
                                final_confirmation = input("Apply >> ")
                                if final_confirmation == "y":
                                    print("Clearing config.json file....")
                                    clear_file = {}
                                    with open("config.json", "w") as f:
                                        json.dump(clear_file, f)
                                    time.sleep(0.5)
                                    print("Writing config to config.json file...")
                                    writeplz = {
                                        "config": [ 
                                            {
                                                "max_deployed_cats": max_cat_deployment_menu,
                                                "custom_file_dir": custom_file_dir_menu,
                                                "stand_still": stand_still_menu,
                                                "initial_wait_time": initial_wait_time,
                                                "enable_random_deployment": enable_random_deployment
                                            }
                                        ],
                                        "random_time_stuff": [
                                            {
                                                "random_stand_still": random_stand_still,
                                                "begin_range": begin_range,
                                                "end_range": end_range,
                                            }
                                        ]
                                        # "activation_period": [ # WIP!!!
                                        #     {
                                        #         "start_date": start_date,
                                        #         "end_date": end_date,
                                        #     }
                                        # ] 
                                    } 

                                    with open("config.json", "w") as f:
                                        json.dump(writeplz, f)
                                    print("Config saved successfully!")
                                    print("Returning back to menu...")
                                    time.sleep(0.5)
                                elif final_confirmation == "n":
                                    print("Changes have not been saved!")
                                    print("Returning back to menu...")
                                    time.sleep(0.5)
                            elif edit_config_menu == "2":
                                while True:
                                        print("=========Other_features=========")
                                        print("[1] = Initial waiting time | active?", op1)
                                        print("[2] = Enable random cat deployment | active?", op2)
                                        print("[3] = Replace static stand still time with a random time | active?", op3)
                                        if unapplyed_changes == True:
                                            print("[4] = Apply changes")
                                        print("[5] = Back")
                                        other_feature_menu = input("Select >> ")
                                        if other_feature_menu == "1":
                                            print("=========Other_features/Initial_wait_time=========")
                                            print("This feature is for delaying the start of the script")
                                            print("By setting this value above 0 means you have to wait an extra set seconds before the script starts")
                                            init_wait_time = input("initial_wait_time >> (0) ")
                                            if init_wait_time > "0":
                                                unapplyed_changes = True
                                                op1 = init_wait_time
                                                ac_iwt = True
                                        elif other_feature_menu == "2":
                                            print("=========Other_features/enable_random_deployment=========")
                                            print("By turning this feature on the program will also deploy random cats during the stand_still time\nThis does not count as a deployed cat\n Enable random deployment? [Y/n]")
                                            enab_rand_depl = input("enable_random_deployment >> (False) ")
                                            if enab_rand_depl == "Y":
                                                unapplyed_changes = True
                                                enab_rand_depl = True
                                                op2 = enab_rand_depl
                                                ac_erd = True
                                        elif other_feature_menu == "3":
                                            print("=========Other_features/random_stand_still=========")
                                            print("WARNING!! After you enable this feature the stand_still value will no longer be used!")
                                            print("This feature will replace the static stand_still time with a constantly changing one")
                                            print("Enable this feature? [Y/n]")
                                            rand_stan_stil = input("random_stand_still >> (False) ")
                                            if rand_stan_stil == "Y":
                                                unapplyed_changes = True
                                                rand_stan_stil = True
                                                op3 = rand_stan_stil
                                                ac_rss = True
                                                print("=========Other_features/random_stand_still=========")
                                                print("This feature also allows you to have a custom start and end range")
                                                print("The random function will only give a random number in between the start and end ranges")
                                                star_rang = input("start_range >> (1) ")
                                                sr = star_rang
                                                print("=========Other_features/random_stand_still=========")
                                                print("The end range is the highest this random number can go")
                                                end_rang = input("end_range >> (5) ")
                                                er = end_rang
                                        elif other_feature_menu == "4":
                                            if unapplyed_changes == True:
                                                print("=========Other_features/Apply_changes=========")
                                                print("Do you want to apply these changes? [Y/n]")
                                                if ac_iwt == True:
                                                    print("Initial_wait_time = ", op1)
                                                if ac_erd == True:
                                                    print("enable_random_deployment =", op2)
                                                if ac_rss == True:
                                                    print("random_stand_still =", op3)
                                                    print("start_range =", sr)
                                                    print("end_range =", er)
                                                apply_changes = input("Save changes >> ")
                                                if apply_changes == "Y":
                                                    print("Applying changes...")
                                                    temp_mdc = config["max_deployed_cats"]
                                                    temp_cfd = config["custom_file_dir"]
                                                    temp_sts = config["stand_still"]
                                                    op1 = int(op1)
                                                    sr = int(sr)
                                                    er = int(er)
                                                    writeplz = {
                                                        "config": [ 
                                                            {
                                                                "max_deployed_cats": temp_mdc,
                                                                "custom_file_dir": temp_cfd,
                                                                "stand_still": temp_sts,
                                                                "initial_wait_time": op1,
                                                                "enable_random_deployment": op2
                                                            }
                                                        ],
                                                        "random_time_stuff": [
                                                            {
                                                                "random_stand_still": op3,
                                                                "begin_range": sr,
                                                                "end_range": er,
                                                            }
                                                        ]
                                                        # "activation_period": [ # WIP!!!
                                                        #     {
                                                        #         "start_date": start_date,
                                                        #         "end_date": end_date,
                                                        #     }
                                                        # ] 
                                                    }

                                                    with open("config.json", "w") as f:
                                                        json.dump(writeplz, f)


                                            else: 
                                                print("=========Other_features/Apply_changes=========")
                                                print("There's nothing for you to apply! Maybe make some changes?")
                                        elif other_feature_menu == "5":
                                            break
                            elif edit_config_menu == "3":
                                break
                    elif config_menu == "2": 
                        print("=========Reset_config=========")
                        print("Do you wish to reset your config back to default? [Y/n]")
                        reset_config = input("Select >> ")
                        if reset_config == "Y":
                            writeplz = {
                                "config": [ 
                                    {
                                        "max_deployed_cats": 2,
                                        "custom_file_dir": None,
                                        "stand_still": 10,
                                        "initial_wait_time": 0,
                                        "enable_random_deployment": False
                                    }
                                ],
                                "random_time_stuff": [
                                    {
                                        "random_stand_still": False,
                                        "begin_range": 1,
                                        "end_range": 5,
                                    }
                                ]
                            }

                            with open("config.json", "w") as f:
                                json.dump(writeplz, f)
    elif mainmenu == "2":
        print("=========Config_file_maker=========")
        print("Writing new config.json file!")
        json_config = {
            "config": [ 
                {
                    "max_deployed_cats": 2,
                    "custom_file_dir": None,
                    "stand_still": 10,
                    "initial_wait_time": 0,
                    "enable_random_deployment": False
                }
            ],
            "random_time_stuff": [
                {
                    "random_stand_still": False,
                    "begin_range": 1,
                    "end_range": 5,
                }
            ]
        }

        with open("config.json", "w") as f:
            json.dump(json_config, f)
        print("New config.json file written!")
    elif mainmenu == "3":
        print("=========Information=========")
        print(f"Version {version}")
        print("This program is used for configuration the config file for StillCat")
        print("Just so you know, this program has not been properly tested! Errors will still happen")