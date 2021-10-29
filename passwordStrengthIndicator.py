# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 16:09:38 2021

@author: Administrator
"""
'''Create a program that determines the complexity of a given
password based on these rules:
• A very weak password contains only numbers and is
fewer than eight characters.
• A weak password contains only letters and is fewerthan
eight characters.
• A strong password contains letters and at least one
number and is at least eight characters.
• A very strong password contains letters, numbers, and
special characters and is at least eight characters.



Example Output
The password '12345' is a very weak password.
The password 'abcdef' is a weak password.
The password 'abc123xyz' is a strong password.
The password '1337h@xor!' is a very strong password.



'''
def passwordValidator(s):
    all_number = '0123456789'
    all_letter = 'abcdefghijklmnopqrst'
    spec_char = '`~!#@$%^&*()_+-=[]{}\|;:'",<>./?"
    num_count = 0
    letter_count = 0
    spco_count = 0
    pv = ''
    for e in s:
        if e in all_number:
            num_count += 1
        if e in all_letter:
            letter_count += 1
        if e in spec_char:
            spco_count +=1
    
    if (num_count == len(s)) and (len(s) < 8):
        pv = 'very weak'
    elif (len(s) == letter_count) and (len(s) < 8):
        pv = 'weak'
    elif (letter_count > 0) and (num_count >= 1) and (spco_count == 0) and (len(s) >= 8):
        pv = 'strong'
    elif  (letter_count > 0) and (num_count > 0) and (spco_count > 0) and (len(s) >= 8):
        pv = 'very strong'
        
    return pv
        
if __name__ == '__main__':
    password_list = ['1234', 'abcdef', 'abc123xyz', '1337h@xor!']
    
    for password in password_list:
        pv = passwordValidator(password)
        print('The password \'{}\' is a {} password.'.format(password, pv))
        
            
    