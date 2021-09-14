# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 19:56:48 2021

@author: Administrator
"""

'''(STEP ONE: a clear problem statement):
        Create a simple self-checkout system. Prompt for the prices
and quantities of three items. Calculate the subtotal of the
items. Then calculate the tax using a tax rate of 5.5%. Print
out the line items with the quantity and total, and then print
out the subtotal, tax amount, and total.


(STEP TWO: input, output, process):
    input:
        price_item1: 25
        quantities_item1: 2
        price_item2: 10
        quantities_item2: 1
        price_item3: 4
        quantities_item3: 1
        
    process:
        (1) prompt for price_item1 with "Enter the price of item 1: "
        (2) prompt for quantities_item1 with "Enter the quantity of item 1: "
        (3) prompt for price_item2 with "Enter the price of item 2: "
        (4) prompt for quantities_item2 with "Enter the quantity of item 2: "
        (5) prompt for price_item3 with "Enter the price of item 3: "
        (6) prompt for quantities_item3 with "Enter the quantity of item 3: "
        (7) initialize subtotal to (price_item1 * quantities _item1 + price_item2* quantities _item2 + price_item3 * quantities _item3)
        (8)initialize tax_rate to 5.5%
        (9) initialize tax to (subtotal * tax_rate)
        (10)initialize total to (subtotal + tax)
        (11) display:
            print (“Subtotal: ${subtotal}“.format(subtotal = subtotal)
            print(“Tax: ${tax}”.format(tax = tax))
            print(“Total: “.format(total = total))
    example output:
        Enter the price of item 1: 25
        Enter the quantity of item 1: 2
        Enter the price of item 2: 10
        Enter the quantity of item 2: 1
        Enter the price of item 3: 4
        Enter the quantity of item 3: 1
        Subtotal: $64.00
        Tax: $3.52
        Total: $67.52
        
(STEP THREE: DESIGN TESTS)
    test 1:
        input:
            price_item1: 25
            quantities_item1: 2
            price_item2: 10
            quantities_item2: 1
            price_item3: 4
            quantities_item3: 1
            
        expected display:
            Enter the price of item 1: 25
            Enter the quantity of item 1: 2
            Enter the price of item 2: 10
            Enter the quantity of item 2: 1
            Enter the price of item 3: 4
            Enter the quantity of item 3: 1
            Subtotal: $64.00
            Tax: $3.52
            Total: $67.52
            
        actual display:
            
            
((STEP FOUR: WRITE THE ALGORITHM INTO PSEUDOCODE):
     these pseudocodes are displayed following the symbol #
     DONE)
            
            
        
            
        


'''

def self_checkout(price_item1, quantities_item1, price_item2, quantities_item2, price_item3, quantities_item3):
    
    #1.initialize price_item1 to an input function
    # prompt for price_item1 with "Enter the price of item 1: "
    #convert it to a numerical value
    # price_item1 = int(input("Enter the price of item 1: "))
    
    # #2.initialize quantities_item1 to an input function
    # # prompt for quantities_item1 with "Enter the quantity of item 1: "
    # #convert it to a numerical value
    # quantities_item1  = int(input("Enter the quantity of item 1: "))
    
    # #3.initialize price_item2 to an input function
    # # prompt for price_item2 with "Enter the price of item 2: "
    # #convert it to a numerical value
    # price_item2 = int(input("Enter the price of item 2: "))
    
    # #4.initialize quantities_item2 to an input function
    # # prompt for quantities_item2 with "Enter the quantity of item 2: "
    # #convert it to a numerical value
    # quantities_item2 = int(input("Enter the quantity of item 2: "))
    
    
    
    # #5.initialize price_item3 to an input function
    # # prompt for price_item3 with "Enter the price of item 3: "
    # #convert it to a numerical value
    # price_item3 = int(input("Enter the price of item 3: "))
    
    # #6.initialize quantities_item3 to an input function
    # # prompt for quantities_item3 with "Enter the quantity of item3: "
    # #convert it to a numerical value
    # quantities_item3 = int(input("Enter the quantity of item3: "))
    
    #7.initialize subtotal to (price_item1 * quantities _item1 + price_item2* quantities _item2 + price_item3 * quantities _item3)
    subtotal = (price_item1 * quantities_item1) + (price_item2* quantities_item2) + (price_item3 * quantities_item3)
    
    #8.initialize tax_rate to 5.5%
    tax_rate = 0.055  #  5.5%
    
    #9.initialize tax to (subtotal * tax_rate)
    tax = subtotal * tax_rate
    
    #10. initialize total to (subtotal + tax)
    total = (subtotal + tax)
    
    #11.display:
                # print (“Subtotal: ${subtotal}“.format(subtotal = subtotal)
                # print(“Tax: ${tax}”.format(tax = tax))
                # print(“Total: “.format(total = total))
                
    print ('Subtotal: ${:.2f}'.format(subtotal))
    print('Tax: ${:.2f}'.format(tax))
    print('Total: ${:.2f} '.format(total))            


if __name__ == "__main__":
    #1.initialize price_item1 to an input function
    # prompt for price_item1 with "Enter the price of item 1: "
    #convert it to a numerical value
    price_item1 = int(input("Enter the price of item 1: "))
    
    #2.initialize quantities_item1 to an input function
    # prompt for quantities_item1 with "Enter the quantity of item 1: "
    #convert it to a numerical value
    quantities_item1  = int(input("Enter the quantity of item 1: "))
    
    #3.initialize price_item2 to an input function
    # prompt for price_item2 with "Enter the price of item 2: "
    #convert it to a numerical value
    price_item2 = int(input("Enter the price of item 2: "))
    
    #4.initialize quantities_item2 to an input function
    # prompt for quantities_item2 with "Enter the quantity of item 2: "
    #convert it to a numerical value
    quantities_item2 = int(input("Enter the quantity of item 2: "))
    
    
    
    #5.initialize price_item3 to an input function
    # prompt for price_item3 with "Enter the price of item 3: "
    #convert it to a numerical value
    price_item3 = int(input("Enter the price of item 3: "))
    
    #6.initialize quantities_item3 to an input function
    # prompt for quantities_item3 with "Enter the quantity of item3: "
    #convert it to a numerical value
    quantities_item3 = int(input("Enter the quantity of item3: "))
    
    self_checkout(price_item1, quantities_item1, price_item2, quantities_item2, price_item3, quantities_item3)
    
