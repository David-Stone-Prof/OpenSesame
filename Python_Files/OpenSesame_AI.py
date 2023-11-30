#!usr/bin/env python3
import logging
from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image
from OpenSesameFunctions import *

# Setup logging
logging.basicConfig(filename=r'C:\OS_Programming\OpenSesame\OpenSesameLog.txt', level=logging.INFO,
                    format='%(asctime)s: %(message)s')

# Log application start
logging.info("Application started")

# Initialize root window
root = Tk()
root.title('Muffy Lord')
iconPic = ImageTk.PhotoImage(Image.open('./Muffy.jpg'))
root.iconphoto(False, iconPic)
root.geometry('+900+300')
canvas = Canvas(root, width=1280, height=720, bg="black")
canvas.pack()

# Set up background image
img = ImageTk.PhotoImage(Image.open(r'./OpenSesame_PatrickStar2.jpg'))
Patrick = Label(root, image=img, bg="#5e5e5e", highlightthickness=0.75)
# Ensure the image is centered and fills the space behind the buttons
Patrick.place(x=0,y=0)
canvas.create_window(450, 10, anchor=NW, window=Patrick)
# path = r'./OpenSesame_PatrickStar2.jpg'
# img = ImageTk.PhotoImage(Image.open(path))
# Patrick = Label(root, image=img, bg="#5e5e5e", highlightthickness=0.75)
# Patrick.place(x=0,y=0)
# canvas.create_window(450, 10, anchor=NW, window=Patrick)

# Font for buttons
arial12 = tkFont.Font(family='Times New Roman', size=12, weight=tkFont.BOLD)

# Function to create a logged version of another function
def log_and_execute(func):
    def wrapper(*args, **kwargs):
        logging.info(f"{func.__name__} function called")
        return func(*args, **kwargs)
    return wrapper

# Modify functions to include logging
OpenGoogle = log_and_execute(OpenGoogle)
OpenNotepad = log_and_execute(OpenNotepad)
RocketLeague = log_and_execute(RocketLeague)
CSGO = log_and_execute(CSGO)
Fortnite = log_and_execute(Fortnite)
LeagueOfLegends = log_and_execute(LeagueOfLegends)
PUBG = log_and_execute(PUBG)
RedDead2 = log_and_execute(RedDead2)
Cities = log_and_execute(Cities)
RainbowSix = log_and_execute(RainbowSix)
GTAfive = log_and_execute(GTAfive)
Loveline = log_and_execute(Loveline)
COD = log_and_execute(COD)
Skyrim = log_and_execute(Skyrim)
KingdomCome = log_and_execute(KingdomCome)
# ... repeat for other functions ...

# Create buttons
button_specs = [
    ("Google", OpenGoogle, 450, 300),
    ("Notepad", OpenNotepad, 595, 300),
    ("Rocket League", RocketLeague, 739, 300),
    ("CSGO", CSGO, 450, 350),
    ("Fortnite", Fortnite, 595, 350),
    ("LoL", LeagueOfLegends, 739, 350),
    ("PUBG", PUBG, 450, 400),
    ("RDR2", RedDead2, 595, 400),
    ("CITIES", Cities, 739, 400),
    ("Rainbow 6: Siege", RainbowSix, 450, 450),
    ("GTA V", GTAfive, 595, 450),
    ("Loveline", Loveline, 739, 450),
    ("Call of Duty", COD, 450, 500),
    ("Skyrim", Skyrim, 595, 500),
    ("Kingdom Come", KingdomCome, 739, 500)
    # Add more buttons if necessary
]

for text, command, x, y in button_specs:
    button = Button(root, font=arial12, text=text, padx=10, pady=5,
                    fg="white", bg="#5e5e5e", command=command)
    button.configure(width=10, activebackground='#33B5E5', relief=RAISED)
    button.place(x=x, y=y)

# EXIT APPLICATION
def ExitApp():
    logging.info("Application closed")
    root.destroy()

# Adjust the 'Exit Application' button placement
exitButton = Button(root, font=arial12, text="Exit Application", padx=10,
                    pady=5, fg="white", bg="#3300ff", command=ExitApp)
exitButton.configure(width=15, activebackground='#3300ff', relief=RAISED)
# Reposition the button so it does not cross the application's border
exitButton.place(x=1150 - exitButton.winfo_reqwidth(), y=10)

# Main loop
mainloop()
