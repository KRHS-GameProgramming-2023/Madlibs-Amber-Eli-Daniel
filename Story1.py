from Getters import *

def Story1(debug = False):
    if debug: print("Story1 Function")
    
    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    sport1 = getSport("Enter a sport: ", debug)
    food1 = getFood("Enter a food: ", debug)
    adjective1 = getAdjective("Enter an adjective: ", debug)
    friendName2 = getWord("Enter a name: ", debug)
    cardGame1 = getGame("Enter a card game: ", debug)
    noun1 = getNoun("Enter a noun: ", debug)
    verb1 = getVerb("Enter a past tense verb: ", debug)

    out = "\n"
    out += "One day me and my friend " + friendName1
    out += " were out playing " + sport1
    out += " and we were having a blast, but " + friendName1
    out += " got hungry so we decided to get some " + food1
    out += " to eat. It was so " + adjective1
    out += ". Later on, our other friend " + friendName2
    out += " joined us. We all played " + sport1
    out += " for most of the day, and once it got dark, we decided to go to my house where we decided to play the card game " + cardGame1
    out += ". After that, a " + noun1
    out += " crashed into my house, so we " + verb1
    out += " out of the house and onto the street where we watched the world end."
    out += "\n \n The End.\n"
    
    
    return out
