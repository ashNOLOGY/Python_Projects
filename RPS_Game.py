"""
Rock Paper Scissors Game
------------------------
Project: [bini-tek]\\
Code by: Ash Dawod
Year: 2018
Version: 1.0


BRIEF DESCRIPTION OF THE PROGRAM
-------------------------------
A simple Rock Papers Scissors game
Computer vs User

"""

#-- The Imports
import os
import math
import random




"""
/////////////////////
Defining the fuction
/////////////////////
"""




#///////////////////////////////

#The Main() Function
#-------------------
def main():
    # Variables
    #global computer_choice  # the computer's random choice
    #global user_choice   # the user's choice
    #computer_point = 0
    #user_point = 0



    print("\nLets Play!"
          "\n----------\n"
          "\n[1] Rock"
          "\n[2] Paper"
          "\n[3] Scissors")


    # This is 3 plays While loop
    i = 0  # the While loop counter
    while (i < 3):
        #The computer will randomly choose a number
        computer_choice = random.randint(1,3)

        #The IF statement to determine what was choosen
        # ROCK function
        if computer_choice == 1:
            rock()
            i = i+1   #adding one to the While counter

        # PAPER function
        if computer_choice == 2:
            paper()
            i = i+1  #adding one to the While counter

        # SCISSORS function
        if computer_choice == 3:
            scissors()
            i = i+1  #adding one to the While counter





#////////////////////////////



#The Results Functions [ win / lose / tie]
#----------------------------------------
def win():
    print("You Win!")


def lose():
    print("You Lose!")


def tie():
    print("You Tie!")


#////////////////////////////




# Variables to be used in scoring
computer_point = 0   # the points given to computer when it wins
user_point = 0  # the points given to user when it wins


#The Rock Function
#-----------------
def rock():
    #the user's input
    user_choice = int(input("\nWhat's your play? :  "))

    #the IF statement to determine
    '''
    if user pics 1: Tie
    if user pics 2: User loses
    if user pics 3: User wins
    '''
    if user_choice == 1:
        tie()
        print("Computer also picked Rock")

    if user_choice == 2: # user loses / computer wins
        lose()
        print("Paper over Rock")
        #add point to computer



    if user_choice == 3: # user wins /  computer losess
        win()
        print("Rock crushes Scissors")
        #add point to user




#////////////////////////////






#The Paper Function
#-----------------
def paper():
    # the user's input
    user_choice = int(input("\nWhat's your play? :  "))

    # the IF statement to determine
    ''' 
    if user pics 1: User Loses
    if user pics 2: Tie
    if user pics 3: Computer wins    
    '''
    if user_choice == 1: # user loses / computer wins
        lose()
        print("Paper over Rock")
        #add point to computer



    if user_choice == 2:
        tie()
        print("Computer also picked Paper")

    if user_choice == 3: # user win / computer loses
        win()
        print("Scissor cuts Paper")
        #add point to user


#////////////////////////////






#The Scissors Function
#----------------------
def scissors():
    # the user's input
    user_choice = int(input("\nWhat's your play? :  "))

    # the IF statement to determine
    '''
    if user pics 1: User wins
    if user pics 2: User loses
    if user pics 3: Tie
    '''

    if user_choice == 1:     # user wins / computer loses
        win()
        print("Rocks crush Scissors")
        #add point to the user


    if user_choice == 2:    # user loses / computer wins
        lose()
        print("Scissors cut Paper")
        #add point to the computer


    if user_choice == 3:
        tie()
        print("Computer also picked Scissors")



"""
////////////////////////////
END of Defining the fuction
////////////////////////////
"""






#Dispaly the Name of the program
print("\nRock Paper Scissors"
      "\n  [bini-tek]\\\\"
      "\n------------------\n")



#Setting up the WHILE loop to do 2 main things:
#1: To call the FUNCTION() !!!!!!!!!!
#2: To ask if the user wants do it again
while_again = 'y' # <-- the answer to the loop
while (while_again.lower() == 'y'):
    #print("\nThe main() call goes here!!")
    main()

    #Ask if the user wants to do it again
    while_again = input("\nWould you like to play again Y/N: ")

#If the answer is not 'y'
#Thank the user & Exit
print("\n\n\n- - - - - - - - - - - - "
      "\nThank You For Playing")
exit()