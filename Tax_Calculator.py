# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 16:42:08 2021

@author: Administrator
"""

conversion_rate = 5.5
tax = 0

subtotal = float(input("What is the order amount? "))
state = input("What is the state? ")

if state == "WI":
    print("The subtotal is ${:.2f}.".format(subtotal))
    tax = subtotal*conversion_rate/100
    print("The tax is ${:.2f}.".format(tax))
    
print("The total is ${:.2f}.".format(subtotal+tax))