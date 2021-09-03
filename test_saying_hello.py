# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 08:48:16 2021

@author: Administrator
"""

from saying_hello import saying_hello
#the "saying_hello" followed by the keyward "import" is a function in a py file which is named saying_hello too

# all_lower_letters = 'abcdefghijklmnopqrst'
# all_capital_letters = all_lower_letters.upper()

# print(all_lower_letters)
# print(all_capital_letters)

'''Test 1: assume that the user inputs a normal English name

Input: Haein
Expected output (display):
                        What is your name? Haein
                        Hello, Haein, nice to meet you!
Actual output:
                        What is your name? Haein
                        Hello, Haein, nice to meet you!

'''

#saying_hello()



'''Test 2: assume that the user inputs a number 
    
Input:2
Expected output: Sorry, your name is invalid or too long!
Actual output: Sorry, your name is invalid or too long!
'''
#saying_hello()



'''Test 3: assume that the user inputs a symbol, which is neither a number nor a letter

Input: *
Expected output: Sorry, your name is invalid or too long!
Actual output: Sorry, your name is invalid or too long!

'''
#saying_hello()

'''Test 4: assume that users' input is too long 

Input: Haaaaaaaaaaaaaaaaa
Expected output: Sorry, your name is invalid or too long!
Actual output: Sorry, your name is invalid or too long!

'''
saying_hello()

'''Test 5: assume that 

Input: 
Expected output:
Actual output:

'''




