from Getters import *

def Story2(debug = False):
    if debug : print("Story2 Function")

    print("")
    friendName1 = getWord("enter a name ", debug)
    sport1 = getSport("enter a sport ", debug)
    food1 = getfastFood("enter a fast food restaurant ", debug)
    name1 = getName1("enter a name ", debug)
    money1 = getMoney("enter a amount of money ", debug)
    foodOption1 = getFoodOption1("enter a meal ")
    foodOption2 = getFoodOption2("enter a meal ")
    drinkOption1 = getDrinkOption1("enter a drink ")
    drinkOption2 = getDrinkOption2("enter a drink ")
    
    out = "\n"
    out+= "One day my friend, " +friendName1
    out+= " and I were out playing " + sport1 + ".\n"
    out+= "When we finished playing, I wanted to eat at " + food1 + ".\n"
    out+= "My dad " +name1+ " drove us there and gave me $" + money1 + ".\n"
    out+= "" + (friendName1) + " got " + foodOption1 +" & " + drinkOption1
    out+= " while I got " + foodOption2 + " & " + drinkOption2 + ".\n"
    out+= "Once we dropped off " + (friendName1) + " I went home and took a nap.\n"
    out+= "THE END"
    return out
