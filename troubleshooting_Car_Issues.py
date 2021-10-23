# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 20:11:00 2021

@author: Administrator
"""

'''Create a program that walks the user through troubleshooting issues with a car. Use the following decision tree to build
the system:
    
    
    
Example Output
Is the car silent when you turn the key? y
Are the battery terminals corroded? n
The battery cables may be damaged.
Replace cables and try again.

'''

ans_1 = input('Is the car silent when you turn the key? ')

if ans_1 == 'y':
    ans_2 = input('Are the battery terminals corroded? ')
    if ans_2 == 'y':
        print('Clean terminals and try starting again.')
    else:
        d = input()
        print('Replace cables and try again.')

elif ans_1 == 'n':
    ans_3 = input('Does the car make a clicking noise? ')
    if ans_3 == 'y':
        print('Check spark plug connections.')
    else:
        ans_4 = input('Does the car crank up but fail to start? ')
        if ans_4 == 'y':
            print('Check spark plug connections.')
        else:
            ans_5 = input('Does the engine start and then die? ')
            if ans_5 == 'y':
                ans_6 = input('Does your car have fuel injection? ')
                if ans_6 == 'y':
                    print('Get it in for service.')
                else:
                    print('Check to ensure the choke is opening and closing.')
            
    
    
    