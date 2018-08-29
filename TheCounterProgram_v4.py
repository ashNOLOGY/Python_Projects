'''
The Counter Program
Project: [bini-tek]\\
Coded by: Ash Dawod
Aug/2018
Version 4.0

# # # # # #

The program allows the user to count, forward or backward
Using the "STEP" method, to count every 2, 4, 7, 350
'''




#------ The Imports
import math
import random
from os import system , name
from time import sleep




''' 
///////////////////////
Defining The Functions
//////////////////////
'''

#-- The clear() FUNCTION
#- a quick way to clear some of the screen
#------------------------------------------
def clear():
    print("\n"*5)

########################





#-- The Instrucions() Function
#-----------------------------
def instructions():
    #-- Clear the Screen
    clear()

    #-- Display the instructions
    print("\nINSTRUCTIONS"
          "\n------------"
          "\n"
          "\n-This program allows you to count in any range"
          "\n-Forward or Backward"
          "\n-To count BACKWARD:"
          "\n\t*Make sure to put the large number first"
          "\n\t*And to use \'negative\' STEP, ie: -1, -2, ect. "
          "\n\n\n")

    #-- Call the main_choices()
    main_choices()


########################









#-- The counter_program() Function
#-- w/ Integrated WHILE loop
#----------------------------------
def counter_program():
    #-- the WHILE loop
    while_answer = 'y'
    while (while_answer.lower() == 'y'):

        # Clear the screen
        clear()

        # Ask the user for a Starting number
        start_num = int(input("Please enter START number: "))

        # Ask the user for an Ending number
        end_num = int(input("Please enter END number: "))

        # Ask the user for the Increment
        step_num = int(input("Please enter STEP number: "))

        # Print what the choosen parameters are
        print("\nYour START is:", start_num,
              "\nYour END is:", end_num,
              "\nYour STEP is: ", step_num)

        # Create a list and print the results
        result = list(range(start_num, end_num, step_num))
        print("\nYour results are:", result)

        # Ask the user if they want to do it again
        while_answer = input("\nTry it again? y/n: ")





########################





#-- The main_choices() FUNCTION
#------------------------------

# variables for this function
def main_choices():
    print("\n"
          "Main Choices"
          "\n------------"
          "\n1. Instructions"
          "\n2. Start the Counter program"
          "\n3. Clear the Screen"
          "\n4. Exit")


    # The User's Input for the main_choices() Function
    uI_mainChoice = ""

    #-- Getting the Users Input for their Main Choice
    uI_mainChoice = int(input("\nWhat is your choice: "))

    #-- the IF Statement for the Main Choice option
    if (uI_mainChoice == 1):
        #-- Present the instructions
        instructions()
    if (uI_mainChoice == 2):
        #-- run the Counter program
        counter_program()
    if (uI_mainChoice == 3):
        #-- clear the screen
        clear()
        main_choices()
    if (uI_mainChoice == 4):
        #-- Print Good Bye, and exit after 2 seconds
        print("Good Bye, exiting in a few seconds")
        sleep(2)
        exit()

    else:
        #-- if Option is not 1-4, print this and go back to Main Choices
        main_choices()

####################################


'''
////////////////////////////
END of Function Definitions
////////////////////////////
////////////////////////////
'''


#-- Print The Program Title
print("\n\t\t\t------------------------------"
      "\n\t\t\t| The Counter Program [v4.0] | "
      "\n\t\t\t|      [bini-tek]\\\\          |"
      "\n\t\t\t------------------------------\n")



#-- Calling the function main_choices() function
main_choices()



# outro
input("\n\t\t\t-----------------"
      "\n\t\t\t| ENTER to Exit |"
      "\n\t\t\t-----------------")