# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 14:29:48 2021

@author: Administrator
"""

'''knowledge about pizza:
    1.The regular sized pizza 
        will be 16 inches round, 6 slices and would serve 3 if each person has 2 slices.
    2.The larger pizza 
        will be 18 inches round, 8 slices, and serve 4 if each person has 2 slices.
        
    Based on what I have read in the problem statement and its example output,
     the pizza size here we use is the larger pizza:
         total_pieces = num_pizza * 8


'''


'''(STEP ONE: a clear problem statement):
Write a program to evenly divide pizzas. Prompt for the
number of people, the number of pizzas, and the number of
slices per pizza. Ensure that the number of pieces comes out
even. Display the number of pieces of pizza each person
should get. If there are leftovers, show the number of leftover
pieces.


(STEP TWO: input, output, process):
    input:
        1.for num_people: 8
        2. for num_pizza : 2
        
    process:
        1.prompt for num_people with "How many people? "
        2.prompt for num_pizza with "How many pizzas do you have? "
        3. initialize total_pieces to (num_pizza * 8)
        4. initialize pieces_per_person to (total_pieces / num_people)
        5. initialize num_leftover to total_pieces - (num_people*pieces_per_person)
        
        6. display: "{num_people} people with {num_pizza} pizzas".format(num_people = num_people, num_pizza = num_pizza)
                    "Each person gets {pieces_per_person} pieces of pizza.".format(pieces_per_person = pieces_per_person)
                    "There are {num_leftover} leftover pieces.".format(num_leftover = num_leftover)
    Example Output:
        How many people? 8
        How many pizzas do you have? 2 
        
        8 people with 2 pizzas
        Each person gets 2 pieces of pizza.
        There are 0 leftover pieces.


(STEP THREE: DESIGN AT LEAST FOUR TEST):
    test 1: for testing the normal occasion
        input:
             1.for num_people: 8
             2. for num_pizza : 2
         expected display:
            How many people? 8
            How many pizzas do you have? 2 
            
            8 people with 2 pizzas
            Each person gets 2 pieces of pizza.
            There are 0 leftover pieces.
             

(STEP FOUR: WRITE THE ALGORITHM INTO PSEUDOCODE):
     these pseudocodes are displayed following the symbol #
     DONE             
'''
#1.initialize num_people to input function,
#prompt for num_people with "How many people? "
#convert it to int
num_people = int(input("How many people? "))

#2.initialize num_pizza to input function,
#prompt for num_pizza with "How many pizzas do you have? "
#convert it to int
num_pizza = int(input("How many pizzas do you have? "))

#3. initialize total_pieces to (num_pizza * 8)
total_pieces = num_pizza * 8
     
# 4. initialize pieces_per_person to (total_pieces / num_people)
pieces_per_person = int((total_pieces / num_people))
      
#5. initialize num_leftover to total_pieces - (num_people*pieces_per_person)
num_leftover = int(total_pieces - (num_people*pieces_per_person))

#6. display: "{num_people} people with {num_pizza} pizzas".format(num_people = num_people, num_pizza = num_pizza)
#"Each person gets {pieces_per_person} pieces of pizza.".format(pieces_per_person = pieces_per_person)
#"There are {num_leftover} leftover pieces.".format(num_leftover = num_leftover)
print("{num_people} people with {num_pizza} pizzas".format(num_people = num_people, num_pizza = num_pizza))
print("Each person gets {pieces_per_person} pieces of pizza.".format(pieces_per_person = pieces_per_person))
print("There are {num_leftover} leftover pieces.".format(num_leftover = num_leftover))