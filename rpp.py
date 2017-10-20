import random
import time 

# rock beats scissors, scissors beat paper, paper beats rock

def player():
    
    choice = raw_input(">")
    return choice

def machine():
    aichoice = random.randint(1,3)
    return aichoice

def running():
    print "Rock"
    time.sleep(0.5)
    print "paper"
    time.sleep(0.5)
    print "scissors"
    time.sleep(0.5)
    print "choose your throw"
    time.sleep(0.5)
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
    elif playerchoose == "2" and machinechoose == 1:
        print "you throw paper"
        print "computer throws Rock"
        print "Win"
    elif playerchoose == "2" and machinechoose == 2:
        print "you throw paper"
        print "computer throws paper"
        print "tie"
    elif playerchoose == "2" and machinechoose == 3:
        print "you throw paper"
        print "computer throws Scissors"
        print "lose"
    elif playerchoose == "3" and machinechoose == 1:
        print "you thorw scissors"
        print "computer throws Rock"
        print "lose"
    elif playerchoose == "3" and machinechoose == 2:
        print "you throw scissors"
        print "computer throws paper"
        print "win"
    elif playerchoose == "3" and machinechoose == 3:
        print "you throw scissors"
        print "machine throws scissors"
        print "tie"

    else:
        print "Not valid choice, please try again"

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
        raw_input("press enter to start over")
