from customtkinter import filedialog    
import customtkinter

app = customtkinter.CTk()
app.geometry("600x500")
app.resizable(False, False)
app.title("StillCat Configurator")

def selectfile():
        filename = filedialog.askopenfilename()
        print(filename)
        print("Test")

button = customtkinter.CTkButton(app, text="CTkButton", command=selectfile)
button.pack(padx=20, pady=20)

app.mainloop()