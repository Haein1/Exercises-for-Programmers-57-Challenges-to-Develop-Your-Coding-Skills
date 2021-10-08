# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 08:49:58 2021

@author: Administrator
"""

'''Create a program that prompts for your weight, gender,
number of drinks, the amount of alcohol by volume of the
drinks consumed, and the amount of time since your last
drink. Calculate your blood alcohol content (BAC) using this
formula
BAC = (A × 5.14 / W × r) − .015 × H
where
• A is total alcohol consumed, in ounces (oz).
• W is body weight in pounds.
• r is the alcohol distribution ratio:
– 0.73 for men
– 0.66 for women
• H is number of hours since the last drink.

'''
try:
    weight = int(input('What is your weight(pounds)? '))
    gender = input('Are you a female or male(Female:0; Male:1)? ')
    number_drinks = int(input('What is the number of drinks that you had?' ))
    amount_alcohol  = int(input('Please input the amount of alcohol by volume of the drinks consumed: '))
    amount_time = int(input('Please input the amount of time since your last drink: '))
except ValueError:
    print('Please input a number......')
    
A = number_drinks * amount_alcohol
W = weight
H = amount_time
female_r = 0.66
male_r = 0.73
blood_alcohol_calculutor = 0

if gender == '1':
    blood_alcohol_calculutor = (A * 5.14 / W * male_r)-0.015 * H
if gender == '0':
    blood_alcohol_calculutor = (A * 5.14 / W * female_r)-0.015 * H

 
if blood_alcohol_calculutor >= 0.08:
    print('Your BAC is {}. It is not legal for you to drive.'.format(blood_alcohol_calculutor))
else:
    print('Your BAC is {}. It is legal for you to drive.'.format(blood_alcohol_calculutor))
    
