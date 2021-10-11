# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 09:01:38 2021

@author: Administrator
"""

'''Create a program that converts temperatures from Fahrenheit to Celsius or from Celsius to Fahrenheit. Prompt for the
starting temperature. The program should prompt for the
type of conversion and then perform the conversion.
The formulas are
C = (F − 32) × 5 / 9
and
F = (C × 9 / 5) + 32



Example Output
Press C to convert from Fahrenheit to Celsius.
Press F to convert from Celsius to Fahrenheit.
Your choice: C
Please enter the temperature in Fahrenheit: 32
The temperature in Celsius is 0.
'''

your_choice =  input('Press C to convert from Fahrenheit to Celsius.\nPress F to convert from Celsius to Fahrenheit.').upper()
print('Your choice:', your_choice)

if your_choice == 'C':
    f = int(input('Please enter the temperature in Fahrenheit: '))
    c = int((f-32)*5/9)
    print('The temperature in Celsius is {}.'.format(c))
if your_choice == 'F':
    c = int(input('Please enter the temperature in Celsius: '))
    f = int(c*(9/5)+32)
    print('The temperature in Fahrenheit is {}.'.format(f))
    
    
    