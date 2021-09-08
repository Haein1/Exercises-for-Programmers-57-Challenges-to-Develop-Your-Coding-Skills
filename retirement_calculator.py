# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 22:16:16 2021

@author: Administrator
"""
# importing date class from datetime module
from datetime import date
'''(STEP ONE: a clear problem statement):
Create a program that determines how many years you have
left until retirement and the year you can retire. It should
prompt for your current age and the age you want to retire
and display the output as shown in the example that follows.

(Your computer knows what the current yearis, which means
you can incorporate that into your programs. You just have
to figure out how your programming language can provide
you with that information.)

Q:how to get the current year in python
# importing date class from datetime module
from datetime import date
  
# creating the date object of today's date
todays_date = date.today()
  
# printing todays date
print("Current date: ", todays_date)
  
# fetching the current year, month and day of today
print("Current year:", todays_date.year)
print("Current month:", todays_date.month)
print("Current day:", todays_date.day)


(STEP TWO: input, output, process):
    input: your_age: 25; retire_age:65
    process:
        1.prompt for your_age with "What is your current age? "
        2.prompt for retire_age with "At what age would you like to retire? "
    display:
        Example Output
        What is your current age? 25
        At what age would you like to retire? 65
        You have 40 years left until you can retire.
        It's 2015, so you can retire in 2055.
        
(STEP THREE: DESIGN AT LEAST FOUR TEST):
    test 1: for testing the normal occasion
        input:  
            1. for your_age : 25
            2. for retire_age: 65
            
        expected display: 
            What is your current age? 25
            At what age would you like to retire? 65
            You have 40 years left until you can retire.
            It's 2015, so you can retire in 2055.

(STEP FOUR: WRITE THE ALGORITHM INTO PSEUDOCODE):
     these pseudocodes are displayed following the symbol #
     DONE
'''
#1. initialize your_age to an input function
# prompt for your_age with "What is your current age? "
# convert it to numbers
your_age = int(input("What is your current age? "))

#2. initialize retire_age to an input function
# prompt for retire_age with "At what age would you like to retire? "
# convert it to numbers
retire_age = int(input("At what age would you like to retire? "))


#3. initialize left_year to (retire_age - your_age)
# left_year: the left years until you can retire
left_year = retire_age - your_age


#4. get current_year use datetime module
# creating the date object of today's date
todays_date = date.today()
current_year = todays_date.year

#5.initialize retire_year to (current_year + left_year)
retire_year = current_year + left_year
#6.display:
    #"You have {left_year} years left until you can retire.\nIt's {current_year}, so you can retire in {retire_year}."format(left_year = left_year, current_year = current_year, retire_year = retire_year)
print("You have {left_year} years left until you can retire.\nIt's {current_year}, so you can retire in {retire_year}.".format(left_year = left_year, current_year = current_year, retire_year = retire_year))


#if __name__ = "__main__":
    
