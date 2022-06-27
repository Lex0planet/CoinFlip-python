import random
import time
import this
choices = { # User made choices gets translated in number
    "pile" : 1,
    "face" : 0,
}

compChoices = { # Randomly generated computer number translated into readable words
    1 : "pile",
    0 : "face",
}

def menu(): # Main game
    userChoice = input("Pile où face ?")
    if userChoice.lower() in ["pile", "face"]: # Check if the lowered input is one of the 2 choices
        userChoice = userChoice.lower() # I'm not gonna talk about that, I just feel dumb
        userNumber = choices[userChoice] # Check the choices dictionnary comment
        print("On jette la pièce...")
        time.sleep(2)
        coinFlip = random.randint(0,1) # Computer launches the coin
        losingChoice = compChoices[coinFlip] # See compChoices comment
        if int(userNumber) == coinFlip:
            print(f"Gagné ! C'est {userChoice}!")
        else:                                      # This basically tells you if you won or lost
            print(f"Perdu... C'est {losingChoice}")
    else:
        print("Erreur !") # If you made an oopsie doopsie, launches the game again
        menu()

menu()