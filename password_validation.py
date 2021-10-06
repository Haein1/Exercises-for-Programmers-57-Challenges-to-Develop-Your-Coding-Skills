# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 08:39:57 2021

@author: Administrator
"""

'''Create a simple program that validates userlogin credentials.
The program must prompt the user for a username and
password. The program should compare the password given
by the user to a known password. If the password matches,
the program should display “Welcome!” If it doesn’t match,
the program should display “I don’t know you.”


Example Output
What is the password? 12345
I don't know you.
Or
What is the password? abc$123
Welcome!



'''
true_password = 'abc$123'
user_input_p = input("What is the password? ")
if user_input_p == true_password:
    print('Welcome!')
else:
    print("I don't know you.")