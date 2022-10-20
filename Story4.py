from Getters import *

def Story4(debug = False):
    if debug: print("Story4 Function")
    
    print("\n")
    noun1 = getNoun("Enter a noun: ", debug)
    food1 = getFood("Enter a food: ", debug)
    food2 = getFood("Enter a food: ", debug)
    name1 = getWord("Enter a name: ", debug)
    restaurant1 = getRestaurant("Enter a restaurant: ", debug)
    creature1 = getCreature("Enter a creature: ", debug)
    game1 = getGame("Enter a game: ", debug)
    movementVerb1 = getPastVerb("Enter a movement verb: ", debug)
    name2 = getWord("Enter a name: ", debug)
    game2 = getGame("Enter a game: ", debug)
    adjective1 = getAdjective("Enter a adjective: ", debug)
    sport1 = getSport("Enter a sport: ", debug)
    
    out = " Once upon a time there was a " + noun1
    out += " and this " + noun1
    out += " loved to eat " + food1
    out += " as well as " + food2
    out += " because of this, the " + noun1
    out += " was named " + name1 + "."
    out += " One day, " + name1
    out += " was eating at " + restaurant1
    out += " unfortunately, while eating, a " + creature1
    out += " decided to attack." 
    out += " Luckily, it wasn't a real attack, the " + creature1 
    out += " just wanted to play " + game1
    out += " sadly, everyone was too scared to play with them and everyone ended up " + movementVerb1 + "."
    out += " Later on, " + name2
    out += " the best friend of the " + creature1
    out += " wanted to cheer up their friend, so they got everyone together and " 
    out += "they all played " + game2
    out += " while eating " + food1 
    out += " and " + food2
    out += " they all got so full that everyone became extremely " + adjective1
    out += " to counteract this, they decided to go play " + sport1
    out += " they ended up playing till the end of eternity.\n"
    out += "\n The End \n"
     
    return out
