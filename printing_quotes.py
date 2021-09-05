# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 11:01:36 2021

@author: Administrator
"""

'''Quotation marks are often used to denote the start and end
of a string. But sometimes we need to print out the quotation
marks themselves by using escape characters(a backslash:\).


(STEP ONE: a clear problem statement):
    Create a program that prompts for a quote and an author.
    Display the quotation and author as shown in the example
    output.
    

(STEP TWO: input, output, process):
    input: string type
        1. a quote: These aren't the droids you're looking for.
        2. an author: Obi-Wan Kenobi
    process: 
        1. prompt for your_quote with "What is the quote? ";
        2. prompt for its_author with "Who said it? "
    final ecpected output:
        What is the quote? These aren't the droids you're looking for.
        Who said it? Obi-Wan Kenobi
        Obi-Wan Kenobi says, "These aren't the droids
        you're looking for."
    
    
(STEP THREE: DESIGN AT LEAST FOUR TEST):
    test 1:
     input: "These aren't the droids you're looking for." for your quote
             "Obi-Wan Kenobi" for its_author
     expected output: 
            What is the quote? These aren't the droids you're looking for.
            Who said it? Obi-Wan Kenobi
            Obi-Wan Kenobi says, "These aren't the droids
            you're looking for."
     actual output:
         
     test 2:
         input: at least it is empty for one variable
         expected output: You should input something for the quote or its author
         actual output:
             
             
             
(STEP FOUR: WRITE THE ALGORITHM INTO PSEUDOCODE):
     these pseudocodes are displayed following the symbol #
     DONE
         
(STEP FIVE: WRITE THE CODE):   

'''
# 4. according oop, you can, if needed, convert this code into some functionality 

def printing_quotes():
    '''Create a program that prompts for a quote and an author.
    Display the quotation and author as shown in the example
    output.
    
    input: string type
        1. a quote: These aren't the droids you're looking for.
        2. an author: Obi-Wan Kenobi
    process: 
        1. prompt for your_quote with "What is the quote? ";
        2. prompt for its_author with "Who said it? "
    final ecpected output:
        What is the quote? These aren't the droids you're looking for.
        Who said it? Obi-Wan Kenobi
        Obi-Wan Kenobi says, "These aren't the droids
        you're looking for."
    
    '''

    #1.Initialize your_quote to the user's input
    # prompt for your_quote with "What is the quote? "
    your_quote = input("What is the quote? ")
    #2.Initialize its_author to the user's input
    #prompt for its_author with "Who said it? "
    its_author = input("Who said it? ")
    
    # deal with the occasion that variables are empty
    if (len(your_quote) != 0) and (len(its_author) != 0):
        #3. display: its_author + "says, "+"\"" + your_quote +"\""
        print(its_author + " says, "+"\"" + your_quote +"\"")  
    else:
        print("You should input something for both the quote and its author.")
    

if __name__ == "__main__":
    printing_quotes()
