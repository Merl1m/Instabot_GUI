# GUI Application for Instabot tool which is used to retrive user data from instagram profiles
# Version 1.0

# Import Section
import tkinter as tk
from instaloader import Instaloader, Profile
from pyshorteners import Shortener as shortie

# Variables
Window_Size = "900x700"
Window_Title = "Instabot (GUI Version)"
R_Start, Gap = 0.2, 0.06
Window_List = list()
Result_List = list()

# Functions
def InstaLoad(USERNAME):
    List = []
    Loader = Instaloader()
    profile = Profile.from_username(Loader.context, USERNAME)
    try:
        URL = shortie().tinyurl.short(profile.profile_pic_url)
        List.append("USERNAME     : {0}".format(profile.username))
        List.append("Name         : {0}".format(profile.full_name))
        List.append("Bio          : {0}".format(profile.biography))
        List.append("Profile Pic  : {0}".format(URL))
        List.append("Followers    : {0}".format(profile.followers))
        List.append("Following    : {0}".format(profile.followees))
        List.append("External URL : {0}".format(profile.external_url))
        List.append("Private      : {0}".format(profile.is_private))
        List.append("Verified     : {0}".format(profile.is_verified))
        List.append("ID           : {0}".format(profile.userid))
        return List
    except Exception as Error:
        print(Error)
        return None

def Reload():
    global Result_List
    for element in Result_List:
        element.after(0, element.destroy())
    Result_List = []
    Input()

def Retrive_Information():
    global Result_List
    Username = Window_List[0].get()
    Result = InstaLoad(Username)

    for element in Window_List:
        element.after(0, element.destroy)
    if Result == None:
        pass
    else:
        C = R_Start - Gap
        Result
        for i in Result:
            C += Gap
            tmp = tk.Label(Window, text=i, font=('Arial', 15))
            tmp.place(relx=0.1, rely=C, anchor='w')
            Result_List.append(tmp)

    def Save():
        with open("{0}.txt".format(Username), "w") as File_Obj:
            for i in Result:
                File_Obj.write(i + '\n')

    Save_Button = tk.Button(Window, text="Save", command=Save, height=1, width=9, bd=6)
    Save_Button.place(relx=0.5, rely=0.9, anchor='center')
    Result_List.append(Save_Button)

    Back_Button = tk.Button(Window, text="Back", command=Reload, height=1, width=9, bd=6)
    Back_Button.place(relx=0.2, rely=0.9, anchor='center')
    Result_List.append(Back_Button)

def Input():
    global Window_List
    Label = tk.Label(Window, text="Username", font=('Bold', 25))
    Label.place(relx=0.5, rely=0.42, anchor='center')
    Entry = tk.Entry(Window, bd=5)
    Entry.place(relx=0.5, rely=0.49, anchor='center')
    Button = tk.Button(Window, text="OSInt", command=Retrive_Information, height=1, width=13, bd=6)
    Button.place(relx=0.5, rely=0.56, anchor='center')
    Window_List = [Entry, Label, Button]

def Quit():
    Window.after(0, Window.destroy())

# Window
Window = tk.Tk()
Window.geometry(Window_Size)
Window.title(Window_Title)
Window.resizable(True, True)
Window.iconbitmap(".\images\Instabot_icon.ico")

Q_Button = tk.Button(Window, text="Quit", command=Quit, height=1, width=9, bd=6).place(relx=0.8, rely=0.9, anchor='center')

Input()
Window.mainloop()