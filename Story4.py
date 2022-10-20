from Getters import *

def Story4(debug = False):
    if debug: print("Story4 Function")
    
    print("\n")
    noun1 = getNoun("enter a noun ", debug)
    food1 = getFoodOption1("enter a food option ", debug)
    food2 = getFoodOption2("enter a food option ", debug)
    name1 = getName1("enter a name ", debug)
    restaurant1 = getRestaurant("enter a restaurant ", debug)
    creature1 = getCreature("enter a creature ", debug)
    game1 = getGame1("enter a game ", debug)
    movementVerb1 = getMovmentVerb("enter a movement verb ", debug)
    name2 = getName2("enter a name ", debug)
    game2 = getGame2("enter a game ", debug)
    adjective1 = getAdjective("enter a adjective ", debug)
    sport1 = getSport("enter a sport ", debug)
    
    out = " Once upon a time there was a " + noun1
    out += " and this " + noun1
    out += " loved to eat " + food1
    out += " as well as " + food2
    out += " because of this, the " + noun1
    out += " was named " + name1 + ".\n"
    out += " One day, " + name1
    out += " was eating at " + restaurant1
    out += " unfortunately, while eating, a " + creature1
    out += " decided to attack. Luckily, it wasn't a real \n" 
    out += " attack, the " + creature1 
    out += " just wanted to play " + game1
    out += " sadly, everyone was too scared to play with them and everyone ended up " + movementVerb1 + " \n"
    out += " Later on, " + name2
    out += " the best friend of the " + creature1
    out += " wanted to cheer up their friend, so they got everyone together and \n" 
    out += " they all played " + game2
    out += " while eating " + food1 
    out += " and " + food2
    out += " they all got so full that everyone became extremely " + adjective1
    out += " to counteract \n"
    out += " this, they decided to go play " + sport1
    out += " they ended up playing till the end of eternity."
    out += "\n \n The End \n"
     
    return out
