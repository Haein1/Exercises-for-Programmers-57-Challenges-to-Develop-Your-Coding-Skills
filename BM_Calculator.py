# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:23:48 2021

@author: Administrator
"""
'''Create a program to calculate the body mass index (BMI)
for a person using the person’s height in inches and weight
in pounds. The program should prompt the user for weight
and height.
Calculate the BMI by using the following formula:
bmi = (weight / (height × height))* 703


Example Output
Your BMI is 19.5.
You are within the ideal weight range.
or
Your BMI is 32.5.
You are overweight. You should see your doctor.

'''
#used to ensure that user's input is numeric

def is_number(a):
    
    if '.' in a:
        try:
            float(a)
        except ValueError:
            return 'Invalid input!'
    else:
        try:
            int(a)
        except ValueError:
            return 'Invalid input!'

weight = (input('Enter your weight: '))
height = (input('Enter your height: '))
is_w_n = is_number(weight)
is_h_n = is_number(height)
# print(is_w_n)
# print(is_h_n)

if is_w_n == None and is_h_n == None:
    bmi = (float(weight) / (float(height) * float(height)))* 703
    print("Your BMI is {0:.1f}.".format(bmi))
    if bmi >= 18.5 and bmi <= 25:
        print("You are within the ideal weight range.")
    elif bmi < 18.5:
        print('You are too thin. You should see your doctor.')
    elif bmi > 25:
        print('You are overweight. You should see your doctor.')
    
else:
    print("Invalid input!")
    
    
# if bmi >= 18.5 and bmi <= 25:
#     print("You are within the ideal weight range.")
# elif bmi < 18.5:
#     print('You are too thin. You should see your doctor.')
# elif bmi > 25:
#     print('You are overweight. You should see your doctor.')
    

# print(int(a))

        


