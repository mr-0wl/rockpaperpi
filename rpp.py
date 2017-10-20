import random

# rock beats scissors, scissors beat paper, paper beats rock

def player():
    
    choice = raw_input(">")
    return choice

def machine():
    aichoice = random.randint(1,3)
    return aichoice

def running():
    print "Rock Paper Scissors"
    print "Type 1 for Rock"
    print "Type 2 for paper"
    print "Type 3 for scissors"
    playerchoose = player()
    machinechoose = machine()
    if playerchoose == "1" and machinechoose == 1:
        print "You throw Rock"
        print "computer throws Rock"
        print "tie"
        
    elif playerchoose == "1" and machinechoose == 2:
        print "you throw Rock"
        print "computer throws Paper"
        print "loose"
    elif playerchoose == "1" and machinechoose == 3:
        print "you throw Rock"
        print "computer throws Scissors"
        print "win"

play = raw_input("play a round? y or n > ")

while play == "y":

    running()
    playagain = raw_input("Play again? y or n > ")
    if playagain == "y":
        pass
    elif playagain == "n":
        play = "n"
    else:
        print "invalid, please type 'y' or 'n'"
        print "starting a new round"
