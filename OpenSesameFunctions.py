import os, webbrowser, subprocess

# Functions
def OpenNotepad():
    os.system('notepad.exe')

def OpenGoogle():
    subprocess.Popen("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

def RocketLeague():
    webbrowser.open('steam://rungameid/252950')

def CSGO():
    webbrowser.open("steam://rungameid/730")

def Fortnite():
    webbrowser.open('com.epicgames.launcher://apps/Fortnite?action=launch&silent=true')

def LeagueOfLegends():
    webbrowser.open('C:\Riot Games\League of Legends\LeagueClient.exe')

def PUBG():
    webbrowser.open('steam://rungameid/578080')

def RedDead2():
    webbrowser.open('steam://rungameid/1174180')

def Cities():
    webbrowser.open('steam://rungameid/255710')