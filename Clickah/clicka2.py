#!/usr/bin/env python3

import pyautogui #pyautogui used for mouse control

print("Henry's Marvelous Auto-Clicker! To exit, first try Ctrl + C, if terminal not in focus it wont work. Instead drag mouse to top left. If majorly screwed up, Ctrl+Alt+Dlt then close the program, then email henrysynnott@gmail.com what happened")
print("Monitor " + pyautogui.size())
print("Press Ctrl + C once the mouse is over the right spot. If it doesn't work click onto the terminal then move mouse back")

try:
   while True:
        x, y = pyautogui.position()                                           #store mouse position in x and y
        positionstr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)      #concacentate string and store into var
        print(positionstr, end='')                                            #print location string
        print('\b' * len(positionstr), end ='', flush = True)                 #delete old string so new one takes same place
except KeyboardInterrupt:
    print('\nCoordinates fetched.')    #goes to new line and prints using Ctrl+C interrupt error to break from loop

xr = int(input("What is the X above?: ")) #not really necessary, but allows for manual movement
yr = int(input("What is the Y above?: "))
inte = int(input("At what interval should I click? Must be more than a second: "))  #takes .5 sec to move mouse to spot, idk what will happen
print("Reminder: Ctrl+C/Jam mouse in top left to exit") #top left is failsafe in pyautogui, will stop program

pyautogui.PAUSE = inte  #time in between mouse actions set here

clik = input("Should I say when I click Y/N: ") #mostly just here for debugging

try:
    while True:
        pyautogui.moveTo(xr, yr, 0.5)  #moves mouse to spot and clicks
        pyautogui.click()
        if clik.upper() == "Y":
            print("click")

except:                                #catches Ctrl + C and top left errors to exit program
    print("Goodbye")
