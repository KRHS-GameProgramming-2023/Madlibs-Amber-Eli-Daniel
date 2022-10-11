def getMenuOption(debug = False):
    if debug: print("getMenuOption Function")
    
    goodInput = False
    
    while not goodInput:
        option = input("Please select an option: ")
        option = option.lower()
        
        if (option == "q" or 
            option == "quit" or
            option == "x" or 
            option == "exit"):
                option = "q"
                goodInput = True
                
        elif (option == "1" or 
            option == "one" or
            option == "story 1" or 
            option == "story1"):
                option = "1"
                goodInput = True
        
        elif (option == "2" or 
            option == "two" or
            option == "story 2" or 
            option == "story2"):
                option = "2"
                goodInput = True
       
        elif (option == "3" or 
            option == "three" or
            option == "story 3" or 
            option == "story3"):
                option = "3"
                goodInput = True
                
        else:
            print("Please make a valid choice")
        
    return option


def getWord(prompt, debug = False):
    if debug: print("getWord Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't use language like that")
        
    return word
    
def getWeapon(prompt, debug = False):
    if debug: print("getWeapon Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word):
            goodInput = False
            print("Don't use that foul language")
        
    return word
    
def getSport(prompt, debug = False):
    if debug: print("getSport Function")
    
    goodInput = False
    
    sports = ["soccer",
              "football",
              "hockey",
              "volleyball",
              "tennis",
              "rugby",
              "baseball",
              "softball",
              "field hockey",
              "ice hockey",
              "hockey",
              "dodgeball",
              "table tennis",
              "basketball",
              "badminton"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't use language like that")
        elif word.lower() not in sports:
            goodInput = False
            print("Sorry I don't know that one.")
        
        
    return word
    
def getfastFood(prompt, debug = False):
    if debug: print("getFood Function")
    
    goodInput = False
    
    fastFood = ["mcdonalds", 
                "burger king", 
                "dunkin donuts", 
                "wendys", 
                "five guy's",]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't use language like that")
        elif word.lower() not in fastFood:
            goodInput = False
            print("please use a real fast food place")
        
    return word

def getFood(prompt, debug = False):
    if debug: print("getFood Function")
    
    goodInput = False
    f = open("foods.txt", 'r')
    foods = f.read().splitlines()
    f.close()
    # ~ if debug: print(foods)
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't use language like that")
        elif word.lower() not in foods:
            goodInput = False
            print("Sorry I don't know that one.")
        
    return word
    
def getAdjective(prompt, debug = False):
    if debug: print("getAdjective Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't use language like that")
        
        
    return word

def getGame(prompt, debug = False):
    if debug: print("getGame Function")
    
    goodInput = False
    
    games = ["uno",
             "war",
             "rummy",
             "racko",
             "poker",
             "speed",
             "go fish",
             "solitare",
             "bridge",
             "crazy eight",
             "crazy 8",
             "cribbage",
             "skat",
             "old maid",
             "gofish",
             "crazyeight",
             "crazy8",
             "crazy eights"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't use language like that")
        elif word.lower() not in games:
            goodInput = False
            print("Sorry I don't know that one.")
        
        
    return word

def getNoun(prompt, debug = False):
    if debug: print("getVerb Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't use language like that")
        
        
    return word

def getVerb(prompt, debug = False):
    if debug: print("getVerb Function")
    
    goodInput = False
    
    verbs = ["ran",
             "swam",
             "jumped",
             "hopped",
             "walked",
             "skipped",
             "leaped",
             "trotted",
             "slithered",
             "sprinted",
             "jogged",
             "flew",
             "crawled"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't use language like that")
        elif word.lower() not in verbs:
            goodInput = False
            print("Sorry I don't know that one.")
        
    return word
    
def getName1(prompt, debug = False):
    if debug: print("getName1 Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't use language like that")
            
        
    return word

def getMoney(prompt, debug = False):
    if debug: print("getMoney Function")
    
    goodInput = False
    nums = "0123456789."
    
    while not goodInput:
        word = input(prompt)
        word = word.strip("$")
        dcount = 0
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't use language like that")
        for char in word:
            if char not in nums:
                goodInput = False
                print(word + " is not a number")
                break
            if char == ".":
                dcount += 1
        if dcount > 1:
            goodInput = False
            print("too many decimals")
        if word == ".":
            goodInput = False
            
            
            
        
    return word
    
def isSwear(word, debug = False):
    if debug: print("isSwear Function")
    f = open("swearList.txt", 'r')
    swearList = f.read().splitlines()
    f.close()

    if word.lower() in swearList:
        return True
    else:
        return False
