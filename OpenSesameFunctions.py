import os, webbrowser, subprocess
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# from EasyLogin import *

# Functions
# NOTE 1: 
# I think I need to add a Class and call these functions.
# Then I save it as a pynbd (Check correct file type)!
# And I can use a dictionary in delete_after.py so that I
# can relate each function to a simple name. This will
# allow me as the programmer an easier time to troubleshoot,
# program, etc. in the future. 

# NOTE 2: For loop the dictionary

# NOTE 3: Look into YAML files or something to make it so the 
# Python executable will be usable by anyone. 

# NOTE 4: Add a feature (eventually through GitHub repos and
# Agile development) to allow the user to *** MAP *** each button
# to any individual executable file they desire... 
# Future development can allow for specialization within apps.

# NOTE 5: Provide a service with this ease of use on a computer, 
# maybe you can market it? Find the business driver. Use your
# business savvy friends. 

# NOTE 6: Last unrelated note -- invest in stocks, take risks. 
# You only lose what you don't try.


def OpenNotepad():
    os.system('notepad.exe')
    now = datetime.now()
    instanceNotification = "Opening Notepad at {0} on {1}".format(
                                    str(now.strftime('%c')),
                                    str(now.strftime('%A')),
                                    # str(now.day),
                                    # str(now.year)
                                                                    )
    return print(instanceNotification)
# Need to add strftime for Weekday Name for {1}


def OpenGoogle():
    #subprocess.Popen("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    #webbrowser.open('https://securelogon.boeing.com/GAS/#/login')
    #width100 ng-dirty ng-touched ng-invalid
    twitter_login = 'https://twitter.com/login'
    webbrowser.open(twitter_login)
    xpath_userid = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
    userid = driver.findElement(By.xpath(xpath_userid))
    userid.sendKeys('123@gmail.com')



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

def RainbowSix():
    webbrowser.open('steam://rungameid/359550')

def GTAfive():
    webbrowser.open('steam://rungameid/271590')

def Loveline():
    classicLoveline = r'https://www.youtube.com/channel/UCcaYdF2OFL6WgERNmKmIBXg'
    webbrowser.open(classicLoveline)

def Mordhau():
    webbrowser.open('steam://rungameid/629760')

def COD():
    webbrowser.open('steam://rungameid/1938090')

def Skyrim():
    webbrowser.open('steam://rungameid/489830')

def Rust():
    webbrowser.open('steam://rungameid/252490')

def KingdomCome():
    webbrowser.open('steam://rungameid/379430')


'''Example

    Even if correct, leave out, git commit, change, commit again?

NOTE: Make two classes, call one in the other
        1st: Functions being called with their respective execution.
        2nd: Those functions being put in a dictionary with their
                respective string text name. e

# 
class buttonExecutables:

    def __init__(self, executable):

        self.executable = executable
        # NOTE: Dictionary that maps string text name to function?
        executable = {

                'notepad'     :   selectedProcesses.OpenNotepad(),
                'google'      :   selectedProcesses.OpenGoogle(),
                'Cities'      :   selectedProcesses.Cities()  

        }

# List of callable processes.
class selectedProcesses:

    def OpenNotepad():
        os.system('notepad.exe')

    def OpenGoogle():
        subprocess.Popen("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        #webbrowser.open('https://securelogon.boeing.com/GAS/#/login')
        #width100 ng-dirty ng-touched ng-invalid
        #webbrowser.open('https://twitter.com/login')

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
'''