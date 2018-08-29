'''
The Tipping Calculator
v2.0
-----------------
Project: [bini-tek]\\
Code by: Ash Dawod

A simple program to help you figure out the tip for your bill
2018
'''

'''
///////////////////////
Defining the Fucntion
///////////////////////
'''
#-- the_tipper() Function
#------------------------
def the_tipper():

      #Ask the user for the Bill amount (convert to int)
      bill = int(input("\nEnter the Bill ammount: $"))

      #Calculate 15% tip : 0.15 x bill
      tip15 = 0.15 * bill
      print("15% tip is: $", tip15)

      #Calculate 20% tip : 0.20 x bill
      tip20 = 0.20 * bill
      print("20% tip is: $", tip20)

      #Display the total amount + 15% tip
      bill15 = bill + tip15
      print("\nBill + 15% tip = $",bill15)

      #Display the total amount + 20% tip
      bill20 = bill + tip20
      print("Bill + 20% tip = $",bill20)


'''
///////////////////////
END of Defining the Fucntion
///////////////////////
'''


#Display the name of the program
print("\nTipping Calculator v2.0"
      "\n   [bini-tek]\\\\"
      "\n---------------------\n")

#Setting up the WHILE loop to do 2 main things:
#1: To call the the_tipper() function
#2: To ask if the user wants calculate another bill
another_bill = 'y' # <-- the answer to the loop
while (another_bill.lower() == 'y'):
    the_tipper()
    #Ask if the user wants to do it again
    another_bill = input("\nWould you like to calculate another Bill? Y/N: ")

#print a thank you message & exit
print("\nThank$ for Tipping "
      "\n------------------")
exit()

