from Screens import *
from Getters import *
from Story1 import *
from Story2 import *
from Story3 import *

def Madlibs(debug = False):
    if debug: print("welcome to debug")
    
    print(TitleScreen(debug))
    input("Press enter to continue")
    
    done = False
    
    while not done:
        print(MainMenu(debug))
        choice = getMenuOption(debug)
        
        if choice == "q":
            print(ExitScreen())
            exit()
        if choice == "1":
            print(Story1())
            print("\n")
            input("Press enter to continue")
        if choice == "2":
            print(Story2())
            print("\n")
            input("Press enter to continue")
        if choice == "3":
            print(Story3())
            print("\n")
            input("Press enter to continue")
        

Madlibs(False)
