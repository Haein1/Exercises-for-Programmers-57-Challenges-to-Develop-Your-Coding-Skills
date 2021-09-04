# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 10:01:30 2021

@author: Administrator
"""

'''Create a program that prompts for an input string and displays output 
that shows the input string and the number of characters the string contains.(STEP ONE)

Input: a string,  called word
Process:
        1. prompt for word with "What is the input string? "
        2. display  output that contains both word and its length
Example Output
What is the input string? Homer
Homer has 5 characters. (STEP TWO)


(STEP THREE: DESIGN AT LEAST FOUR TEST):
    1.
     input: nothing
     expected output: "You must enter something into the program!"
     actual output:
         
     (I can think only this exception)
     
     
 (STEP FOUR: WRITE THE ALGORITHM INTO PSEUDOCODE):
     these pseudocodes are displayed following the symbol #
     DONE
     
 
(STEP FIVE: WRITE THE CODE):
    
  
'''

# 4. according your need or OOP requirments, 
#consider to make this code into one function
def counting_characters_numbers():
    
    # 1. Initialize word to input function.
    #    Plus,prompt for the input with "What is the input string? "
    word = input("What is the input string? ")
    
    # 2. Initialize nummbers_of_characters to len(word)
    numbers_of_characters = len(word)
    
    # 3. if numbers_of_characters == 0:
    #    prompt for the user with "You must enter something into the program!"
    # otherwise:
    #    display: word + " has " + numbers_of_characters + "characters."
    
    if numbers_of_characters == 0:
        print("You must enter something into the program!")
    else:
        print("{} has {} characters.".format(word, numbers_of_characters))


if __name__ == "__main__":
    counting_characters_numbers()
