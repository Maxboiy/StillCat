from customtkinter import filedialog
from tkinter import messagebox    
import customtkinter
import json

app = customtkinter.CTk()
app.geometry("600x500")
app.resizable(False, False)
app.title("StillCat Configurator [Version 0.1]")

filename = filedialog.askopenfilename()

def jsonstuff():
    print(filename)
    print("Getting JSON values")
    print("Filename has not been selected")
    with open(filename, "r") as f:
        data = json.load(f)
        for config in data["config"]:
            stand_still_number.configure(placeholder_text=config["stand_still"])
            if config["max_deployed_cats"] == None:
                config["max_deployed_cats"] = "None set!"
            max_deploy_cats_number.configure(placeholder_text=config["max_deployed_cats"])
            if config["custom_file_dir"] == None:
                config["custom_file_dir"] = "None set!"
            custom_image_dir.configure(placeholder_text=config["custom_file_dir"])
            print(config["max_deployed_cats"])
            print(config["custom_file_dir"])
            print(config["stand_still"]) 

def save_to_file():
    stand_still_json = stand_still_number.get()
    custom_image_dir_json = custom_image_dir.get()
    max_deployed_cats_json = max_deploy_cats_number.get() 
    print(stand_still_json, custom_image_dir_json, max_deployed_cats_json)
    if (stand_still_json == "" and custom_image_dir_json == "" and max_deployed_cats_json == ""):
        print("everything empty! ")
        messagebox.showerror("Empty boxes!", "This configuration has not been saved since all the text boxes are empty!")
    else: 
        print(filename)
        with open(filename, "r") as f:
            data = json.load(f)
        for config in data["config"]:
            if stand_still_json == "":
                stand_still_json = config["stand_still"]
            if custom_image_dir_json == "":
                custom_image_dir_json = config["custom_file_dir"]
            elif custom_image_dir_json == "none":
                custom_image_dir_json = None
            if max_deployed_cats_json == "":
                max_deployed_cats_json = config["max_deployed_cats"]
            elif max_deployed_cats_json == "inv":
                max_deployed_cats_json = None
        writeplz = {
            "config": [ 
                {
                    "max_deployed_cats": max_deployed_cats_json,
                    "custom_file_dir": custom_image_dir_json,
                    "stand_still": stand_still_json,
                    # "stand_still_number": stand_still_wait,
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
        messagebox.showinfo("Saved Successfully!", "The configuration has been saved!")
        messagebox.showinfo("Closing...", "Just a heads up, this program will now close!")
        app.destroy()
        app.quit()

label = customtkinter.CTkLabel(app, text="StillCat Configurator", fg_color="transparent")
label.pack(pady=2)
label1 = customtkinter.CTkLabel(app, text="Compatible with version 0.1!", fg_color="transparent")
label1.pack(pady=4)

label2 = customtkinter.CTkLabel(app, text="How long does the mouse have to stand still before opening the image? (in seconds)", fg_color="transparent")
label2.pack(pady=2)

stand_still_number = customtkinter.CTkEntry(app, placeholder_text="Stand Still")
stand_still_number.pack(pady=6)

label3 = customtkinter.CTkLabel(app, text="How many pictures should open before the program closes? type 'inv' to keep it alive until closed", fg_color="transparent")
label3.pack(pady=2)

max_deploy_cats_number = customtkinter.CTkEntry(app, placeholder_text="Max deployed cats")
max_deploy_cats_number.pack(pady=6)

label4 = customtkinter.CTkLabel(app, text="Do you want to use a custom image directory? If you want to use the built-in ones type none", fg_color="transparent")
label4.pack(pady=2)

custom_image_dir = customtkinter.CTkEntry(app, placeholder_text="Custom image directory")
custom_image_dir.pack(pady=6)

label5 = customtkinter.CTkLabel(app, text="If you tend on using this directory on a different computer be aware to have it in the \nSame directory as you set here! It is recommended to put it on a flashdrive!", fg_color="transparent")
label5.pack(pady=2)

label6 = customtkinter.CTkLabel(app, text="Also make sure the file is named config.json else the program can't recognize it!", fg_color="transparent")
label6.pack(pady=2)

savebutton = customtkinter.CTkButton(app, text="Save config", command=save_to_file)
savebutton.pack()

jsonstuff()
app.mainloop()