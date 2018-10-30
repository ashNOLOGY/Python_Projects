'''
Program: HY Salary
Coder: ashNOLOGY
Company: [bini-tek]\\
Version 2.0

'''

"""
Brief Description
------------------
-This is a simple program that allows you to calculate Hourly/Yearly (HY) Salary.
-This is based on a standard 40 hours / 5 Day week schedule.
-The program will provide 2 options:
 1- Type in your Hourly wage, and it will give you the Salary.
 2- Type in the Salary, and it will give you the Hourly wage.
-There will be a Version 2.0, which will have a "Custom" option.
 In that version that user will be able to set up non-standard settings.
"""



#------ The Imports
import math
import random
import os


# intro
# function definitions

'''
/////////////////////////
The Main Menu Function
/////////////////////////
'''

# defining the MainMenu()
def mainMenu():

      # the greeting and the menu
      print("\nWelcome to \"HY Salary\" by [bini-tek]\\\\"
            "\n--------------------------------------"
            "\n[1] Hourly to Salary calculation."
            "\n[2] Salary to Hourly calculation."
            "\n[3] Exit Program.")

      # the user input for selection
      userMenuSelection = int(input("\nPlease make a selection: "))

      if(userMenuSelection == 1):
            # the Hourly to Salary calculation
            hourly_to_salary()
      if(userMenuSelection == 2):
            # the Salary to Hourly calculation
            salary_to_hourly()
      if(userMenuSelection == 3):
            # Exit program
            exit()








'''
/////////////////////////
The Hourly to Salary Function
/////////////////////////
'''

# defineing the function
def hourly_to_salary ():
      # user input
      hourly_input = int(input("\nWhat is your Hourly wage?: "))

      # the calculation
      # [hourly input] x 80 (for 2 weeks) = [] x 26 (payments per year) = Salary

      #bi-weekly
      bi_weekly = hourly_input * 80

      #yearly
      salary = bi_weekly * 26

      #print them out
      print("You entered [", hourly_input, "] as your Hourly wage"
            "\nYour Bi-Weekly pay is: ", bi_weekly,
            "\nYour Salary is: ", salary)

      # to Go back to Main menu
      input("\n\nPress ENTER to go back to the Menu")
      mainMenu()








'''
//////////////////////////////
The Salary to Hourly Function
//////////////////////////////
'''

# defining the function
def salary_to_hourly ():
      # user input
      salary_input = int(input("\nWhat is your Salary?: "))

      # the calculation
      #([salary input] / 52 (weeks in a year)) / 40 (hours per week) = Hourly Wage

      #hourly
      hourly = (salary_input/52) / 40

      #bi-weekly
      biweekly = hourly * 80

      # print them out
      print("You entered [", salary_input, "] as your Salary"
            "\nYour Hourly wage is: ", hourly,
            "\nYour bi-weekly is: ", biweekly)

      # to Go back to Main menu
      input("\n\nPress ENTER to go back to the Menu")
      mainMenu()







'''
######################
Calling The Functions
'''
mainMenu()



# outro
input("\n\t\t\t-----------------"
      "\n\t\t\t| ENTER to Exit |"
      "\n\t\t\t-----------------")