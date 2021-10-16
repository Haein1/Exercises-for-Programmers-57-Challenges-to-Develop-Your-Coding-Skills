# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 14:29:41 2021

@author: Administrator
"""
'''Create a tax calculator that handles multiple states and multiple counties within each state. The program prompts the user for the order amount and the state where the order will be shipped .

Eor Wisconsin resident, prompt for the county of residence 
For Eau Claire county residents, add an additional 0.005 tax 
For Dunn county residents, add an additional 0.004 tax 

Ilinois residents must be charged 8% sales tax with no additional county-level charge. All other states are not charged tax. The program then displays the tax and the total for Wisconsin and Illinois residents but just the total for everyone else.



 Example Output 
What is the order amount? 10 
What state do you Live in? Wisconsin 
The tax is $0. 50.
The total is $10.50.

'''
order_amount = float(input('What is the order amount? '))
living_state  = input('What state do you Live in? ')
living_county = input('What county do you live in? ')
wi_state_tax = 0.05
il_state_tax = 0.08
e_tax = wi_state_tax + 0.005
d_tax = wi_state_tax + 0.004
tax = 0
total = 0
if living_state == 'Wisconsin':
    if living_county == 'Eau Claire county':
        tax = order_amount * e_tax
        total = order_amount + tax
    elif living_county == 'Dunn county':
        tax = order_amount * d_tax
        total = order_amount + tax

    else:
        tax = order_amount * wi_state_tax
        total = order_amount + tax

elif living_state == 'Ilinois':
    tax = order_amount * il_state_tax
    total = order_amount + tax
else:
    tax == 0
    total = order_amount + tax
    
print('The tax is ${}. \nThe total is ${}.'.format(tax, total))