from customtkinter import filedialog 
import json

filename = filedialog.askopenfilename()

print("=========StillCat-configurator=========")
print("Welcome to the StillCat configurator! [Version 0.1 CMD]\n")
print("[1] = Choose configuration file")
print("[2] = Make a configuration file")
print("[3] = Information about this program")
print("[4] = Exit\n")
mainmenu = input("Select >> ")

if mainmenu == "1":
    print("=========StillCat-Config-Menu=========")
    print(f"Editing {filename}\n")
    print("[1] = Edit configuration file")
    print("[2] = Reset configuration file to defaults")
    config_menu = input("Select >> ")
    if config_menu == "1": 
        with open(filename, "r") as f:
            data = json.load(f)
        for config in data["config"]:
            print("=========Current-config=========")
            print("Maximum amount of pictures =", config["max_deployed_cats"])
            print(f"Custom picture directory =", config["custom_file_dir"])
            print(f"How long before opening another picture? (in seconds) =", config["stand_still"]) 


# def jsonstuff():
#     print(filename)
#     print("Getting JSON values")
#     print("Filename has not been selected")
#             stand_still_number.configure(placeholder_text=config["stand_still"])
#             if config["max_deployed_cats"] == None:
#                 config["max_deployed_cats"] = "None set!"
#             max_deploy_cats_number.configure(placeholder_text=config["max_deployed_cats"])
#             if config["custom_file_dir"] == None:
#                 config["custom_file_dir"] = "None set!"
#             custom_image_dir.configure(placeholder_text=config["custom_file_dir"])
#             print(config["max_deployed_cats"])
#             print(config["custom_file_dir"])
#             print(config["stand_still"]) 

# def save_to_file():
#     stand_still_json = stand_still_number.get()
#     custom_image_dir_json = custom_image_dir.get()
#     max_deployed_cats_json = max_deploy_cats_number.get() 
#     print(stand_still_json, custom_image_dir_json, max_deployed_cats_json)
#     if (stand_still_json == "" and custom_image_dir_json == "" and max_deployed_cats_json == ""):
#         print("everything empty! ")
#         messagebox.showerror("Empty boxes!", "This configuration has not been saved since all the text boxes are empty!")
#     else: 
#         print(filename)
#         with open(filename, "r") as f:
#             data = json.load(f)
#         for config in data["config"]:
#             if stand_still_json == "":
#                 stand_still_json = config["stand_still"]
#             if custom_image_dir_json == "":
#                 custom_image_dir_json = config["custom_file_dir"]
#             elif custom_image_dir_json == "none":
#                 custom_image_dir_json = None
#             if max_deployed_cats_json == "":
#                 max_deployed_cats_json = config["max_deployed_cats"]
#             elif max_deployed_cats_json == "inv":
#                 max_deployed_cats_json = None
#         writeplz = {
#             "config": [ 
#                 {
#                     "max_deployed_cats": max_deployed_cats_json,
#                     "custom_file_dir": custom_image_dir_json,
#                     "stand_still": stand_still_json,
#                     # "stand_still_number": stand_still_wait,
#                 }
#             ]
#             # "activation_period": [ # WIP!!!
#             #     {
#             #         "start_date": start_date,
#             #         "end_date": end_date,
#             #     }
#             # ] 
#         }

#         with open("config.json", "w") as f:
#             json.dump(writeplz, f)
#         messagebox.showinfo("Saved Successfully!", "The configuration has been saved!")
#         messagebox.showinfo("Closing...", "Just a heads up, this program will now close!")