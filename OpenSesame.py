#!usr/bin/env python3
from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image  # Changed PIL to pillow
from OpenSesameFunctions import *

# Variable initialization
''' Canvas Sizing '''
canvas_width  = 1280
canvas_height = 720
canvasPosX    = 900
canvasPosY    = 300
''' Background Sizing '''
begX=0
begY=0
finalX=1280
finalY=720

# Creation of application's window (AW)
root = Tk()
root.title('Muffy Lord')                                        # Titling Main Window (AW)
iconPic = ImageTk.PhotoImage(Image.open('./Muffy.jpg'))         # Selecting AW Icon Photo
root.iconphoto(False, iconPic)                                  # Setting AW Icon Photo
root.geometry('+{}+{}'.format(canvasPosX,canvasPosY))           # Determining location of AW
canvas = Canvas(root, width=canvas_width, height=canvas_height) # Determining size of location
canvas.create_rectangle(begX,begY,finalX,finalY,fill="black")   # Create background.
canvas.pack()

#canvas.create_text(500, 100, activefill="white", font=("Purisa", 36, 'bold'), text="Hello World!")

#3300ff - boeing blue
#263D42 - dark grey / black

# Application Background Imaging
path = r'./OpenSesame_PatrickStar2.jpg'
img = ImageTk.PhotoImage(Image.open(path))
Patrick = Label(root, image=img, bg="#5e5e5e", highlightthickness=0.75)
Patrick.place(x=0,y=0)
canvas.create_window(450, 10, anchor=NW, window=Patrick)

arial12 = tkFont.Font(family='Times New Roman', size=12, weight=tkFont.BOLD)    # Font Details for Buttons

# Buttons
''' GOOGLE '''
googleButton = Button(root, font=arial12, text="Google", padx=10, 
            pady=5, fg="white", bg="#5e5e5e", command=OpenGoogle)
googleButton.configure(width=10, activebackground= '#33B5E5', relief=RAISED)
canvas.create_window(10,10, anchor=NW, window=googleButton)
googleButton.place(x=450,y=300)

''' NOTEPAD '''
notepadButton = Button(root, font=arial12, text="Notepad", padx=10, 
            pady=5, fg="white", bg="#5e5e5e", command=OpenNotepad)
notepadButton.configure(width=10, activebackground= '#33B5E5', relief=RAISED)
canvas.create_window(10,10, anchor=NW, window=notepadButton)
notepadButton.place(x=595,y=300)

''' ROCKET LEAGUE '''
rlButton = Button(root, font=arial12, text="Rocket League", padx=10, 
            pady=5, fg="white", bg="#5e5e5e", command=RocketLeague)
rlButton.configure(width=10, activebackground= '#33B5E5', relief=RAISED)
canvas.create_window(10,10, anchor=NW, window=rlButton)
rlButton.place(x=739,y=300)

''' COUNTER STRIKE: GLOBAL OFFENSIVE '''
csgoButton = Button(root, font=arial12, text="CSGO", padx=10, 
            pady=5, fg="white", bg="#5e5e5e", command=CSGO)
csgoButton.configure(width=10, activebackground= '#33B5E5', relief=RAISED)
canvas.create_window(10,10, anchor=NW, window=csgoButton)
csgoButton.place(x=450,y=350)

''' FORTNITE '''
fortniteButton = Button(root, font=arial12, text="Fortnite", padx=10, 
            pady=5, fg="white", bg="#5e5e5e", command=Fortnite)
fortniteButton.configure(width=10, activebackground= '#33B5E5', relief=RAISED)
canvas.create_window(10,10, anchor=NW, window=fortniteButton)
fortniteButton.place(x=595,y=350)

''' LEAGUE OF LEGENDS '''
lolButton = Button(root, font=arial12, text="LoL", padx=10, 
            pady=5, fg="white", bg="#5e5e5e", command=LeagueOfLegends)
lolButton.configure(width=10, activebackground= '#33B5E5', relief=RAISED)
canvas.create_window(10,10, anchor=NW, window=lolButton)
lolButton.place(x=739,y=350)

''' PUBG '''
pubgButton = Button(root, font=arial12, text="PUBG", padx=10, 
            pady=5, fg="white", bg="#5e5e5e", command=PUBG)
pubgButton.configure(width=10, activebackground= '#33B5E5', relief=RAISED)
canvas.create_window(10,10, anchor=NW, window=pubgButton)
pubgButton.place(x=450,y=400)

''' RED DEAD REDEMPTION 2 '''
rd2Button = Button(root, font=arial12, text="RDR2", padx=10, 
            pady=5, fg="white", bg="#5e5e5e", command=RedDead2)
rd2Button.configure(width=10, activebackground= '#33B5E5', relief=RAISED)
canvas.create_window(10,10, anchor=NW, window=rd2Button)
rd2Button.place(x=595,y=400)

''' CITIES: SKYLINES '''
citiesButton = Button(root, font=arial12, text="CITIES", padx=10, 
            pady=5, fg="white", bg="#5e5e5e", command=Cities)
citiesButton.configure(width=10, activebackground= '#33B5E5', relief=RAISED)
canvas.create_window(10,10, anchor=NW, window=citiesButton)
citiesButton.place(x=739,y=400)

''' RAINBOW SIX: SIEGE '''
r6Button = Button(root, font=arial12, text="Rainbow 6: Siege", padx=10,
            pady=5, fg="white", bg="#5e5e5e", command=RainbowSix)
r6Button.configure(width=10, activebackground= '#33B5E5', relief=RAISED)
canvas.create_window(10,10, anchor=NW, window=r6Button)
r6Button.place(x=450,y=450)

''' GTA V '''
gtaVButton = Button(root, font=arial12, text="GTA V", padx=10,
            pady=5, fg="white", bg="#5e5e5e", command=GTAfive)
gtaVButton.configure(width=10, activebackground= '#33B5E5', relief=RAISED)
canvas.create_window(10,10, anchor=NW, window=gtaVButton)
gtaVButton.place(x=595,y=450)

''' LOVELINE '''
lovelineButton = Button(root, font=arial12, text="Loveline", padx=10,
            pady=5, fg="white", bg="#5e5e5e", command=Loveline)
lovelineButton.configure(width=10, activebackground= '#33B5E5', relief=RAISED)
canvas.create_window(10,10, anchor=NW, window=lovelineButton)
lovelineButton.place(x=739,y=450)

''' COD '''
codButton = Button(root, font=arial12, text="Call of Duty", padx=10,
            pady=5, fg="white", bg="#5e5e5e", command=COD)
codButton.configure(width=10, activebackground= '#33B5E5', relief=RAISED)
canvas.create_window(10,10, anchor=NW, window=codButton)
codButton.place(x=450,y=500)

''' SKYRIM '''
rd2Button = Button(root, font=arial12, text="Skyrim", padx=10,
            pady=5, fg="white", bg="#5e5e5e", command=RedDead2)
rd2Button.configure(width=10, activebackground= '#33B5E5', relief=RAISED)
canvas.create_window(10,10, anchor=NW, window=rd2Button)
rd2Button.place(x=595,y=500)

''' RUST '''
citiesButton = Button(root, font=arial12, text="Rust", padx=10,
            pady=5, fg="white", bg="#5e5e5e", command=Cities)
citiesButton.configure(width=10, activebackground= '#33B5E5', relief=RAISED)
canvas.create_window(10,10, anchor=NW, window=citiesButton)
citiesButton.place(x=739,y=500)

''' EXIT APPLICATION '''
def ExitApp():
    root.destroy()

exitButton = Button(root, font=arial12, text="Exit Application", padx=10, 
            pady=5, fg="white", bg="#3300ff", command=ExitApp)
exitButton.configure(width=10, activebackground= '#3300ff', relief=RAISED)
canvas.create_window(10,10, anchor=NW, window=exitButton)
exitButton.place(x=1150,y=10)

''' NOT CURRENTLY USED
# New Window & Button
def openNewWindow():
    newWindow = Toplevel(root)
    newWindow.title('New Window')
    newWindow.geometry('300x300+700+300')
    Label(newWindow, text = 'This is a new window').pack()
btn = Button(root, font=arial12, text='New Window!', command=openNewWindow)
canvas.create_window(10,10, anchor=NW, window=btn)
''' 

mainloop()
 

