
def intro_credit():
    print("")
    print("")
    print("    __  ___                          __  ___                 _ ")          
    print("   /  |/  /___  ____  ___  __  __   /  |/  /___ _____  _____(_)___  ____ ")
    print("  / /|_/ / __ \/ __ \/ _ \/ / / /  / /|_/ / __ `/ __ \/ ___/ / __ \/ __ \ ")
    print(" / /  / / /_/ / / / /  __/ /_/ /  / /  / / /_/ / / / (__  ) / /_/ / / / /")
    print("/_/  /_/\____/_/ /_/\___/\__, /  /_/  /_/\__,_/_/ /_/____/_/\____/_/ /_/ ")
    print("                        /____/")
    print("")
    print("                     THE MYSTERY OF CLEOPATRA'S HEX")
    
# intro function
def intro():
    intro_credit()
    print("")
    print("")
    print("You are the notorious jewel thief (or as you like to call yourself: a professional asset acquirer) Robbin Urdiamondz.")
    print("For the last job before you retire...")
    print("You have decided to break into the mansion of recently deceased billionaire Max Moneybaggs.")
    print("You hope to find the priceless diamond Cleopatra's Hex rumoured to be hidden in his study.")
    print("You have thoroughly scouted the mansion and have come up with three possible points of entry.")
    print("")
    print("Your choices are: ")
    print("Type 1 for door, 2 for window, 3 for upper-floor balcony")

    answer = (input("   >>> "))

    if answer == "1":
        door()
    elif answer == "2": 
        window()
    elif answer == "3":
        roof()
    else:
        print("")
        print("Critical thinking and decisiveness are important traits of a professional asset acquirer.")
        print("You failed to pick an available option.")
        print("GAME OVER!")
        print("")
        intro()

# door function, leads to the kitchen
def door():
    print("")
    print("You find yourself situated in front of a very large and sturdy wooden door.")
    print("There is a big, red button located on the wall close to the door.")
    print("The door seems to be locked. Perhaps it could be opened under some form of force?")
    print("")
    print("Your choices are: ")
    print("Type 1 to try to push the door open, Type 2 to push the large red button.")

    answer = input("   >>> ")

    if answer == "1":
        print("")
        print("Congratulations you clever bugger! You've unlocked the door to the kitchen. ")
        print("You are now in the kitchen.")
        print("")
        kitchen()
    elif answer == "2":
        print("")
        print("An obnoxious alarm sound is triggered...")
        print("Moneybagg's hounds are alerted to your presence and they get to eat some man flesh.")
        print("GAME OVER!")
        print("")
        intro() 
    else:
        print("")
        print("Critical thinking and decisiveness are important traits of a professional asset acquirer.")
        print("You failed to pick an available option.")
        print("GAME OVER!")
        print("")
        intro()

# kitchen function, leads to the hall
def kitchen():
    print("")
    print("Compared to the enormous size of the house, the kitchen is rather small.")
    print("Up on a shelf you spot a bottle, clearly labelled shrinking potion with small text warning of side effects ")
    print("and put it into your tool bag for later.")
    print("Observing your surroundings, you notice 2 doors.")
    print("A RED door and a BLUE door.")
    print("")
    print("Your choices are: ")
    print("Type 1 to choose the RED door, Type 2 to choose the BLUE door.")

    answer = input("   >>> ")

    if answer == "1":
        print("")
        print("As red is the colour of blood, this colour is obviously superior to blue.")
        print("Well done. You have made it into the hall.")
        print("")
        hall()
    elif answer == "2":
        print("")
        print("You open the door and a colossal purple tentacle wraps itself around your leg...")
        print("You are immediately pulled into the mouth of a gigantic octopus.")
        print("You should have chosen RED.")
        print("GAME OVER!")
        print("")
        intro()
    else:
        print("")
        print("Critical thinking and decisiveness are important traits of a professional asset acquirer.")
        print("You failed to pick an available option.")
        print("GAME OVER!")
        print("")
        intro()

# roof function leads to the bedroom
def roof():
    print("")
    print("You're in the garden and look up towards the upper-floor balcony...")
    print("Your choices are: ")
    print("Type 1 to climb the trellis you spot to the left! Type 2 to pole vault up with the washing line pole!")

    answer = input("   >>> ")

    if answer == "1":
        print("Don't look down! You clamber onto the balcony and finding the door unlocked, you go inside. ")
        print("")
        bedroom()
    elif answer == "2":
        print("You almost reach the balcony but you fall backwards. You ain't no olympian, you're a professional asset acquirer! \nGAME OVER!")
        print("")
        intro()
    else:
        print("")
        print("Critical thinking and decisiveness are important traits of a professional asset acquirer.")
        print("You failed to pick an available option.")
        print("GAME OVER!")
        print("")
        intro()

# bedroom function, leads to the hall
def bedroom():
    print("")
    print("You're in a bedroom. One look around reveals a double-posted water bed, a lifesize stuffed polar bear, ")
    print("a collection of skeletons, and a ceiling-mounted portrait of Moneybaggs. ")
    print("You look at the bedside table and see a book titled 'Lost Treasures of Egypt.'")
    print("You hear a bark coming down the hall and you are terrified. ")
    print("")
    print("Your choices are: ")
    print("Type 1 to take the book. Type 2 to take the bedsheets to conceal yourself!")
    answer=input("   >>> ")

    if answer=="2":
        print("")
        print("You think it's safe now and come out of the bedsheets.")
        print("You get a fright when you catch your reflection in the mirror! It's not a ghost, it's just you.")
        print("You pull yourself together and exit the bedroom.")
        print("")
        hall()
    elif answer == "1":
        print("You are distracted by looking at the contents of the book and are caught by the mansion security chihuahua... ")
        print("You are now Mr Tiddles' favourite chew toy. \nGAME OVER!")
        print("")
        intro()
    else:
        print("")
        print("Critical thinking and decisiveness are important traits of a professional asset acquirer.")
        print("You failed to pick an available option.")
        print("GAME OVER!")
        print("")
        intro()

# hall function leads to the treasure room
def hall():
    print("")
    print("You find yourself inside a huge hall with an oversized chess board")
    print("and a ghost knight in a suit of armour is blocking the door to the study.")
    print("A talking deer head, with no eyes, mounted on the wall asks if you need help.")
    print("When you ask the deer what you should do next, he replies, 'No idea!' ")
    print("")
    print("Your choices are: ")
    print("Type 1 to invite the knight to play chess and ask him to let you in if you win.")
    print("Type 2 to run across the chess board and offer the knight an inflatable unicorn to bribe him to open the door.")
    
    answer=input("   >>> ")

    if answer == "1":
        print("")
        print("Great idea! You are a chess master and win easily!")
        print("The knight shakes your hand and lets you into the study.")
        print("")
        treasure()
    elif answer == "2":
        print("Bad idea. The knight has a phobia of unicorns and he slices you into pieces with his sword.")
        print("GAME OVER!")
        print("")
        intro()
    else:
        print("")
        print("Critical thinking and decisiveness are important traits of a professional asset acquirer.")
        print("You failed to pick an available option.")
        print("GAME OVER!")
        print("")
        intro()

# window function, leads to the trophy room      
def window():
    print("")
    print("You are facing the bottom floor window.")
    print("Through a gap in the curtains you can see the trophies that Moneybaggs has mounted up in the room.")
    print("")
    print("Your choices are: ")
    print("Type 1 to use your glass cutter, Type 2 to use your fists")
    print("")

    item = input("   >>> ")

    if item == "1":
        print("You cut open a hole in the window like a professional, and you unlock the window.")
        print("You are now in the Trophy Room.")
        print("")
        trophy_room()
    elif item == "2":
        print("")
        print("I haven't got time for that!")
        print("YOLO!")
        print("CRASH!")
        print("You break the window with a mighty punch.")
        print("The window's health dropped to 0!")
        print("Unfortunately your arm is all cut up!")
        print("You faint at seeing the slightest drop of blood.")
        print("The mansion hounds mistake you for dog food and they eat you!")
        print("GAME OVER!")
        print("")
        intro()
    else:
        print("")
        print("Critical thinking and decisiveness are important traits of a professional asset acquirer.")
        print("You failed to pick an available option.")
        print("GAME OVER!")
        print("")
        intro()

# trophy room function, leads to the hall
def trophy_room():
    print("")
    print("The trophy room displays a variety of stuffed creatures full of holes with limbs missing.")
    print("Seems like Moneybaggs was a terrible shot.")
    print("There is only one door and it has been boarded up.")
    print("")
    print("Your choices are: ")
    print("Type 1 to use the hammer, Type 2 to use the cheese grater")
    item = input("   >>> ")
    print("")

    if item == "1":
        print("Wow, you hammered your way through to the hall like a champ! You're one step closer to that diamond.")
        hall()
    elif item == "2":
        print("A cheese grater with no cheese? Now you've attracted an angry group of hungry mice who feed on you instead.")
        print("GAME OVER!")
        intro()
    else:
        print("")
        print("Critical thinking and decisiveness are important traits of a professional asset acquirer.")
        print("You failed to pick an available option.")
        print("GAME OVER!")
        print("")
        intro()

# treasure room function, final room
def treasure():
    print("")
    print("You have arrived at Max Moneybaggs' private study.")
    print("As you scan your flashlight across the room, you notice three points of interest.")
    print("In between the bookshelves there is a beautifully crafted jewellery box resting on top of a desk of equal artisan crasftsmanship.")
    print("On the left of the bookshelves, there is a safe. You notice a sticky note with some numbers written on it.")
    print("On the right of the bookshelves, there is a tall box-shaped object covered by a thin sheet of cloth.")
    print("")
    print("Your choices are: ")
    print("Type 1 to approach the desk, Type 2 to approach the safe, Type 3 to approach the tall box")
    answer = input("   >>> ")
    if answer == "1":
        print("")
        print("You carefully bring the jewellery box closer...")
        print("Slowly, you open the box...")
        print("In the box you see a small figurine and before you take a closer look, the figurine starts spinning and music starts playing...")
        print("You are caught by the mansion security and have your life beaten out of you.")
        print("GAME OVER!")
        intro()
        
    elif answer == "2":
        print("")
        print("You slowly input the numbers from the sticky note into the safe.")
        print("Old Moneybaggs must have had dementia, you think to yourself.")
        print("HISS")
        print("Before you can react, a snake vaults from the safe and bites you in the neck!")
        print("It seems that Moneybaggs has left his pet snake in the safe and forgotten about it.")
        print("GAME OVER!")
        intro()
    elif answer == "3":
        print("")
        print("You slowly remove the cloth covering the box...")
        print("It reveals the box to be a coffin...")
        print("Carefully, you pry open the coffin...")
        print("Inside is a mummy, but you recognise its bouffant wig and aristocratic clothing...")
        print("It's Mrs Moneybaggs.")
        print("")
        print("As you shine your flashlight away from her dried up face,")
        print("you notice a light reflecting and refracting from an object.")
        print("It's the Cleopatra's Hex diamond necklace!")
        print("Without hesitation, you remove the diamond necklace from Mrs Moneybaggs.")
        print("You are overwhelmed with joy!")
        print("")
        print("You notice some kind of tag attached to the necklace.")
        print("It reads:'Whoever touches this cursed diamond will die in 7 days.'")
        print("Oh crap!")
        print("")
        print("")
        print("")
        end_credits()

# The End and roll credits...
    else:
        print("")
        print("Critical thinking and decisiveness are important traits of a professional asset acquirer.")
        print("You failed to pick an available option.")
        print("GAME OVER!")
        print("")
        intro()

def end_credits():
    print("Cue spooky music.")
    print("Play sound effect - agonising screams.")
    print("")
    print("Roll credits... ")
    print("Jun - director and mummy preservationist")
    print("Lisa - narrator and animal trainer")
    print("Lewis - criminal expert and stuffed creature restorer")
    print("Joe - technical advisor and stunt coordinator")
    print("Glory - acting coach and ghosthunter")
    print("")
    print("No animals were harmed in the making of this game." )
    print("Any resemblance to real persons, living or dead, is purely coincidental." )
    print("")

    print("  ________  ________   _______   ______ ")
    print(" /_  __/ / / / ____/  / ____/ | / / __ \ ")
    print("  / / / /_/ / __/    / __/ /  |/ / / / /")
    print(" / / / __  / /___   / /___/ /|  / /_/ / ")
    print("/_/ /_/ /_/_____/  /_____/_/ |_/_____/  ")
    print("")
    print("")

intro()

