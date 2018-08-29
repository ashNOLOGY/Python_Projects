'''
The Coin Flip Game
v2.0
-----------------
Project: [bini-tek]\\
Code by: Ash Dawod

2018
'''
import math
import random

'''
This is a simple game where the computer randomly "flips a coin" and tells you how many times it get "Heads" or "Tails"
The user gets to tell the computer how many times to flip the coin
'''

'''
//////////////////////
Defining the Functions
//////////////////////
'''

#-- The coin_flip() Function
#---------------------------
def coin_flip():
    #Ask user how many flips should it do
    howMany = int(input("\nHow many times do you want to flip the coin? "))

    # Set up Heads & Tails as 0
    h = 0  # <-- H for Heads
    t = 0  # <-- T for Tails


    #Setting up the FLIP WHILE loop
    #This is to go through the number of flips
    i = 0 # <-- the counter for the While loop
    while (i < howMany):
        # The random Flip (f)
        # The range is between 1 and 2
        f = random.randint(1,2)

        # If the Flip (f) is 1, add one to Heads (h)
        if f == 1:
            h = h + 1

        # If the Flip (f) is NOT 1, add one to Tails (t)
        else:
            t = t + 1

        # Add '1' to the While loop counter after each Flip
        i = i +1

    #Display the result for Heads & Tails
    print("\nHeads: ", h) # <-- Heads
    print("Tails: ", t) # <-- Tails



'''
//////////////////////
END of Defining the Functions
//////////////////////
'''


#Dispaly the Name of the Game
print("\nThe Coin Flip Game [v2.0]"
      "\n   [bini-tek]\\\\"
      "\n--------------------------\n")


#Setting up the WHILE loop to do 2 main things:
#1: To call the coin_flip() function
#2: To ask if the user wants do it again
while_again = 'y' # <-- the answer to the loop
while (while_again.lower() == 'y'):
    coin_flip()
    #Ask if the user wants to do it again
    while_again = input("\nWould you like to do it again? Y/N: ")

#If the answer is not 'y'
#Thank the user & Exit
print("\nThanks for Playing"
      "\n[--Game Over--]")
exit()
