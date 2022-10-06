from Getters import*

def Story1(debug = False):
    if debug: print("Story1 Function")    
    
    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    sport1 = getSport("Enter a Sport: ", debug)
    thing1 = getThing("Enter a Thing: ", debug)
    weapon1 = getWeapon("Enter a Weapon: ", debug)
    actionVerb1 = getAction("Enter an verb: ", debug)

    out = "\n"
    out += "    One day me and my friend " + friendName1
    out += " were out " + sport1
    out += "\n and huge " + thing1
    out += " fell out of the sky \n"
    out += " so we pulled out our " + weapon1
    out += "\n and started " + actionVerb1
    out += "\n we never saw those " + thing1
    out += " again " 
    
    
    return out
