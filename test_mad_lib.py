# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 08:10:47 2021

@author: Administrator
"""
from mad_lib import mad_lib

# all_lower_case = "abcdefghijklmnopqrstuvwxyz"
# all_upper_case = all_lower_case.upper()
# print(all_upper_case)


'''(STEP THREE: DESIGN AT LEAST FOUR TEST):
    test 1: for testing the normal occasion, all inputs are string
        input:
            (1) for your_noun: dog
            (2) for a verb: walk
            (3) for an adjective: blue
            (4) for an adverb: quickly
        expected output:
        
            Do you walk your blue dog quickly? That's hilarious!
            
        actual output:
            Do you walk your blue dog quickly? That's hilarious!

'''
# your_noun = "dog"
# your_verb = "walk"
# your_adj = "blue"
# your_adv = "quickly"
# mad_lib(your_noun, your_verb, your_adj, your_adv)



'''test 2: for dealing the exception where user inputs something that is not composed of letters
        input: * for your_noun
                or
                *for your_verb
                or
                *for your_adj
                or
                *for your_adv
        expected output: "You should input an English word, not some random symbols! "
        actual output:

'''
your_noun = "*"
your_verb = "walk"
your_adj = "blue"
your_adv = "quickly"
mad_lib(your_noun, your_verb, your_adj, your_adv)

