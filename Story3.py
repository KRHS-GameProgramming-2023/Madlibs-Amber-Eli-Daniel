from Getters import*

def Story3(debug = False):
    if debug: print("Story3 Function")    
    
    print("\n")
    friendName3 = getWord("Enter a name: ", debug)
    sport3 = getWord("Enter a Daily Activity: ", debug)
    thing3 = getWord("Enter a plural noun: ", debug)
    weapon3 = getWeapon("Enter a Weapon: ", debug)
    actionVerb3 = getWord("Enter an action verb: ", debug)
    bigNumber3 = getWord("Enter a big number: ", debug)
    loud1 = getWord("Enter an asertive remark: ", debug)

    out = "\n"
    out += "    One day me and my friend " + friendName3
    out += " were out " + sport3
    out += ";\n Out of no where huge " + thing3
    out += " fell out of the sky! \n"
    out += " so " + friendName3
    out += " pulled out a " + weapon3
    out += " and started " + actionVerb3
    out += "\n " + friendName3
    out += "'s " + weapon3
    out += " hit with over " + bigNumber3
    out += " joules of energy! "
    out += "\n we never saw those " + thing3
    out += " again! " + friendName3 
    out += " screamed " + loud1
    out += "\n out of excitement!"
    
    
    return out
    
    
