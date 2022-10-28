from Getters import *

def Story2(debug = False):
    if debug : print("Story2 Function")

    print("")
    friendName1 = getWord("Enter a name: ", debug)
    sport1 = getSport("Enter a sport: ", debug)
    food1 = getfastFood("Enter a fast food restaurant: ", debug)
    name1 = getName1("Enter a name: ", debug)
    money1 = getMoney("Enter a amount of money: ", debug)
    foodOption1 = getFoodOption1("Enter a meal: ")
    foodOption2 = getFoodOption2("Enter a meal: ")
    drinkOption1 = getDrinkOption1("Enter a drink: ")
    drinkOption2 = getDrinkOption2("Enter a drink: ")
    
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
