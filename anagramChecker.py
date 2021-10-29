# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 07:04:58 2021

@author: Administrator
"""

'''Create a program that compares two strings and determines
if the two strings are anagrams. The program should prompt
for both input strings and display the output as shown in
the example that follows.


Example Output
Enter two strings and I'll tell you if they
are anagrams:
Enter the first string: note
Enter the second string: tone
"note" and "tone" are anagrams.


'''

def isAnagram(s1, s2):
    s1_list = []
    for e1 in s1:
        s1_list.append(e1)
    if len(s1) != len(s2):
        return False
    else:
        for e2 in s2:
            if e2 not in s1_list:
                return False
                break
    return True
 
if __name__ == '__main__':       
    prompt = print('Enter two strings and I\'ll tell you if theyare anagrams: ')
    s1 = input('Enter the first string: ')
    s2 = input('Enter the second string: ')
    is_anagram = isAnagram(s1, s2)
    
    if is_anagram:
        print('\"note\" and \"tone\" {} anagrams.'.format('are'))
    else:
        print('\"note\" and \"tone\" {} anagrams.'.format('are not'))
        