from Getters import *

def Story2(debug = False):
    if debug : print("Story1 Function")
    
    print("")
    friendName1 = getWord("enter a name ", debug)
    sport1 = getSport("enter a sport ", debug)
    food1 = getFood("enter a fast food resteraunt ", debug)
    
    out = "\n"
    out+= "One day my friend, " +friendName1
    out+= " were out playing " + sport1 + ".\n"
    out+= "When we finished playing, I wanted to eat at " + food1 + ".\n"
    
    return out
