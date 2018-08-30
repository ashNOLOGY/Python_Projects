'''
Digital Dice
v2.0 : done in Python 3
-----------------
Project: [bini-tek]\\
Code by: Ash Dawod


This is a simple program to allow you to roll a dice
Any range, as many times as you like

2018
'''


import random


'''
/////////////////////
Defining the fuction
/////////////////////
'''

#-- the diceRoll() Function
#--------------------------
def diceRoll():
    diceRange = int(input("\nEnter Dice Range: "))
    TheDice = random.randint(1,diceRange)
    print("You rolled a "+ str(TheDice))


'''
////////////////////////////
END of Defining the fuction
////////////////////////////
'''





#Dispaly the Name of the program
print("\nDigital Dice [v2.0]"
      "\n  [bini-tek]\\\\"
      "\n------------------\n")



#Setting up the WHILE loop to do 2 main things:
#1: To call the diceRoll() function
#2: To ask if the user wants do it again
while_again = 'y' # <-- the answer to the loop
while (while_again.lower() == 'y'):
    diceRoll()
    #Ask if the user wants to do it again
    while_again = input("\nWould you like roll again? Y/N: ")

#If the answer is not 'y'
#Thank the user & Exit
print("\n\nThanks for using Digital Dice"
      "\n- - - - - - - - - - - - - - - ")
exit()