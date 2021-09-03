# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 22:31:57 2021

@author: Administrator
"""
def saying_hello():
    '''This function prompts for your name and prints a greeting using your name
    
    Assumes that users' names only include   [all_lower_letters = 'abcdefghijklmnopqrst'
    all_capital_letters = all_lower_letters.upper() ] in English,
        and that the length of users' name is not greater than 10
    
    '''
    
    #step four: write the algorithm into pseudoode (done)
    #step five: write the code
    all_lower_letters = 'abcdefghijklmnopqrst'
    all_capital_letters = all_lower_letters.upper()
    
    #Initialize name to user's input, prompt for the user's input with "What is your name?"
    name = input("What is your name? ")
    
    #deal with some invalid input
    
    exist = True # using flag to symbolize whether a condition is true or false   
    for l in name:
        if (l in all_lower_letters) or (l in all_capital_letters):
            exist = True
        else:
            exist = False
            
    
    suitable_length = True   
    if (len(name) > 10):
        suitable_length = False
    else: 
        suitable_length = True 
        
      
        
    if exist and suitable_length:
        # Display "Hello,", name, "nice to meet you!"
        print("Hello,", name + ",", "nice to meet you!")  
    else:
        print("Sorry, your name is invalid or too long!")
           
        

if __name__ == "__main__":
    saying_hello()
    
    

