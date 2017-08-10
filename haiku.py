import random

five = ["close the darn door please", "we're out of pasta", "take a nap sometime", "hey look at that dog", "gosh diddly darn it", "close your eyes and breathe", "she hollers like wind", "would you look at that"];
seven = ["listen to the rain outside", "quiet nights are the sad ones", "i wish i knew how to drive", "i am but a tiny egg", "space is vast and infinite", "according to all known laws"];

def repeat():
    user_input = input("Would you like another haiku?")
    if user_input == "yes":
        haiku()
    elif user_input == "no":
        print ("reconsider.")
    else:
        print ("please type 'yes' or 'no'")

def haiku():
    print (random.choice(five))
    print (random.choice(seven))
    print (random.choice(five))
    repeat()



haiku()
repeat()
