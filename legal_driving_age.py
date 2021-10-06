# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 11:46:17 2021

@author: Administrator
"""

'''Write a program that asks the userfortheir age and compare
it to the legal driving age of sixteen. If the user is sixteen or
older, then the program should display “You are old enough
to legally drive.” If the user is under sixteen, the program
should display “You are not old enough to legally drive.”


Example Output
What is your age? 15
You are not old enough to legally drive.
Or
What is your age? 35
You are old enough to legally drive.


'''
legal_driving_age = 16
your_age = int(input("What is your age? "))

a = 'You are old enough to legally drive.' if your_age >= legal_driving_age else 'You are not old enough to legally drive.'
print(a)