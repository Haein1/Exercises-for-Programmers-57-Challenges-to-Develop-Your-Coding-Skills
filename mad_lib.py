# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 07:42:12 2021

@author: Administrator
"""

'''Mad libs are a simple game where you create a story template with blanks for words. 
You, or another player, then construct a list of words and place them into the story, 
creating an often silly or funny story as a result.

(STEP ONE: a clear problem statement):
    Create a simple mad-lib program that prompts for a noun,
    a verb, an adverb, and an adjective and injects those into a
    story that you create.
    

(STEP TWO: input, output, process):
    input: string type
        (1) for your_noun: dog
        (2) for a verb: walk
        (3) for an adjective: blue
        (4) for an adverb: quickly

    process:
        (1) prompt for your_noun with "Enter a noun: "
        (2) prompt for your_verb with "Enter a verb: "
        (3) prompt for your_adj with "Enter an adjective: "
        (4) prompt for your_adv with "Enter an adverb: "
        (5) dispaly: "Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!"".format(verb=your_verb, adjective = your_adj, noun = your_noun, adverb = your_adv )
    final ecpected output:
        Enter a noun: dog
        Enter a verb: walk
        Enter an adjective: blue
        Enter an adverb: quickly
        Do you walk your blue dog quickly? That's hilarious!
        
        
(STEP THREE: DESIGN AT LEAST FOUR TEST):
    test 1: for testing the normal occasion, all inputs are string
        input:
            (1) for your_noun: dog
            (2) for a verb: walk
            (3) for an adjective: blue
            (4) for an adverb: quickly
        expected output:
            Enter a noun: dog
            Enter a verb: walk
            Enter an adjective: blue
            Enter an adverb: quickly
            Do you walk your blue dog quickly? That's hilarious!
            
        actual output:

            
    test 2: for dealing the exception where user inputs something that is not composed of letters
        input: * for your_noun
                or
                *for your_verb
                or
                *for your_adj
                or
                *for your_adv
        expected output: "You should an English word, not some random symbols! "
        actual output:
            
    test 3: for dealing with the exception where user inputs capital letters, at least for one variable
        input:
            DOG for your_noun
            or
            WALK for your_verb
            or
            BLUE for your_adj
            or
            QUICKLY for your_adv
            
        expected output: "All of your inputs should be lowercase letters!"
        
     
(STEP FOUR: WRITE THE ALGORITHM INTO PSEUDOCODE):
     these pseudocodes are displayed following the symbol #
     DONE
     
'''
#7.according OOP, you can, if needed, integate these code into a function
def mad_lib(your_noun, your_verb, your_adj, your_adv):
    
    
    
    
    
    #4. for dealing the exception where user inputs something that is not composed of letters
    '''
    define a function called is_all_letter:
        parameter: your_noun, your_verb, your_adj, your_adv
        
        initialize a variable all_lower_case to "abcdefghijklmnopqrstuvwxyz"
        
        for every n_letter in your_noun:
            if n_letter not in all_lower_case:
                all_noun_letter = False
                break out of the for loop
            otherwise:
                all_noun_letter = True
        
        for every v_letter in your_verb:
            if v_letter not in all-lower-case:
                all_verb_letter = False
                break out of the for loop
            otherwise:
                all_verb_letter = True
                
        for every adj_letter in your_adj:
            if adj_letter not in all_lower_case:
                all_adj_letter = False
                break out of the for loop
            otherwise:
                all_adj_letter = True
                
        for every adv_letter in your_adv:
            if adv_letter not in all_lower_case:
                all_adv_letter  = False
                break out of the for loop
            otherwise:
                all_adv_letters = True
                
        return (all_noun_letter and all_verb_letter and all_adj_letter and all_adv_letter)
                
    
    '''
    def is_all_letter(your_noun, your_verb, your_adj, your_adv):
        all_letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for  n_letter in your_noun:
            if n_letter not in all_letter:
                all_noun_letter = False
                break 
            else:
                all_noun_letter = True
        
        for v_letter in your_verb:
            if v_letter not in all_letter:
                all_verb_letter = False
                break
            else:
                all_verb_letter = True
                
        for  adj_letter in your_adj:
            if adj_letter not in all_letter:
                all_adj_letter = False
                break
            else:
                all_adj_letter = True
                
        for  adv_letter in your_adv:
            if adv_letter not in all_letter:
                all_adv_letter  = False
                break
            else:
                all_adv_letter = True
                
        return (all_noun_letter and all_verb_letter and all_adj_letter and all_adv_letter)
        
        
    #5.for dealing with the exception where user inputs capital letters, at least for one variable
    '''define a function called have_capitals:
        parameter: your_noun, your_verb, your_adj, your_adv
        
        initialize a variable all_upper_case to all_lower_case.upper()
        
        for every n_letter in your_noun:
            if n_letter in all_upper_case:
                n_have_capitals = True
                break out of the for loop
            otherwise:
                n_have_capitals = False
                
        for every v_letter in your_verb:
            if v_letter in all_upper_case:
                v_have_capitals = True
                break out of the for loop
            otherwise:
                v_have_capitals = False
                
        for every adj_letter in your_adj:
            if adj_letter in all_upper_case:
                adj_have_capitals = True
                break out of the for loop
            otherwise:
                adj_have_capitals = False
                
        for every adv_letter in your_adv:
            if adv_letter in all_upper_case:
                adv_have_capitals = True
                break out of the for loop
            otherwise:
                adv_have_capitals = False
                
                
        return (n_have_capitals and v_have_capitals and adj_have_capitals and adv_have_capitals)
        
    
    
    '''
    # def have_capitals(your_noun, your_verb, your_adj, your_adv):
    #     all_lower_case = "abcdefghijklmnopqrstuvwxyz"
    #     all_upper_case = all_lower_case.upper()
    #     for n_letter in your_noun:
    #         if n_letter in all_upper_case:
    #             n_have_capitals = True
    #             break 
    #         else:
    #             n_have_capitals = False
                
    #     for v_letter in your_verb:
    #         if v_letter in all_upper_case:
    #             v_have_capitals = True
    #             break 
    #         else:
    #             v_have_capitals = False
                
    #     for adj_letter in your_adj:
    #         if adj_letter in all_upper_case:
    #             adj_have_capitals = True
    #             break
    #         else:
    #             adj_have_capitals = False
                
    #     for adv_letter in your_adv:
    #         if adv_letter in all_upper_case:
    #             adv_have_capitals = True
    #             break 
    #         else:
    #             adv_have_capitals = False
                
                
    #     return (n_have_capitals and v_have_capitals and adj_have_capitals and adv_have_capitals)
        
    
    
    
    #6.
    '''
        if not is_all_letter:
            print("You should an English word, not some random symbols! ")
        elif have_capitals:
            print("All of your inputs should be lowercase letters!")
        else:
            #dispaly:
            #"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!"".format(verb=your_verb, adjective = your_adj, noun = your_noun, adverb = your_adv )
    
    '''
    if not is_all_letter(your_noun, your_verb, your_adj, your_adv):
        print("You should input an English word, not some random symbols! ")
    # elif have_capitals(your_noun, your_verb, your_adj, your_adv):
    #     print("All of your inputs should be lowercase letters!")
    else:
            #dispaly:
        print("Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!".format(verb=your_verb, adjective = your_adj, noun = your_noun, adverb = your_adv ))
    

if __name__ == "__main__":
    #1.Initialize your_noun to the input function
    #prompt your_noun with "Enter a noun: "
    your_noun = input("Enter a noun: ")
    
    #2.Initialize your_verb to the input function
    #prompt your_verb with "Enter a verb: "
    your_verb = input("Enter a verb: ")
    
    #3.Initialize your_adj to the input function
    #prompt your_adj with "Enter an adjective: "
    
    your_adj = input("Enter an adjective: ")
    #4.Initialize your_adv to the input function
    #prompt your_adv with "Enter an adverb: "
    your_adv = input("Enter an adverb: ")
    
    mad_lib(your_noun, your_verb, your_adj, your_adv)
    
    
