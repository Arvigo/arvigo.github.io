#!/usr/bin/env python3

import pyautogui #pyautogui used for mouse control

pyautogui.alert("Henry's Marvelous Auto-Clicker! To exit, first try Ctrl + C, if terminal not in focus it wont work. Instead drag mouse to top left. If majorly screwed up, Ctrl+Alt+Dlt then close the program, then email henrysynnott@gmail.com what happened", "AutoClicker")
pyautogui.alert("Monitor " + str(pyautogui.size()), "AutoClicker")
pyautogui.alert("Click on the terminal (black blank window) then go to where you want me to click, and press CTRL + C. You don't have to click once you have the mouse in the right spot. I'm gonna disappear for a second!", "AutoClicker")

try:
   while True:
        x, y = pyautogui.position()                                           #store mouse position in x and y
#        positionstr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)      #concacentate string and store into var
#        print(positionstr, end='')                                            #print location string
#        print('\b' * len(positionstr), end ='', flush = True)                 #delete old string so new one takes same place
except KeyboardInterrupt:
    pyautogui.alert('Coordinates fetched.')    #goes to new line and prints using Ctrl+C interrupt error to break from loop

xr = pyautogui.prompt("What X should I use? You were at " + str(x), "AutoClicker") #not really necessary, but allows for manual movement

yr = pyautogui.prompt("What Y should I use? You were at " + str(y), "AutoClicker")

if type(xr) == str and type(yr) == str:
    xr = int(xr)
    yr = int(yr)
else:
    pyautogui.alert("Better Luck Next Time", "AutoClicker")
    exit()
    

inte = int(pyautogui.prompt("At what interval should I click? Must be more than a second: ", "AutoClicker"))  #takes .5 sec to move mouse to spot, idk what will happen
pyautogui.alert("Reminder: Ctrl+C/Jam mouse in top left to exit", "AutoClicker") #top left is failsafe in pyautogui, will stop program

pyautogui.PAUSE = inte  #time in between mouse actions set here

#clik = pyautogui.prompt("Should I say when I click Y/N: ", "AutoClicker") #mostly just here for debugging

try:
    while True:
        pyautogui.moveTo(xr, yr, 0.5)  #moves mouse to spot and clicks
        pyautogui.click()
#        if clik.upper() == "Y":
#            print("click")

except:                                #catches Ctrl + C and top left errors to exit program
    pyautogui.alert("Goodbye", "AutoClicker")
