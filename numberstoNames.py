# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 16:05:15 2021

@author: Administrator
"""

'''Write a program that converts a number from 1 to 12 to the
corresponding month. Prompt for a number and display the
corresponding calendar month, with 1 being January and
12 being December. For any value outside thatrange, display
an appropriate error message.


Example Output
Please enter the number of the month: 3
The name of the month is March.

'''

#SOLUTION TWO
number = input('Please enter the number of the month: ')
# month = ''
number_month = {
        '1': 'Monday',
        '2': 'Feburary',
        '3': 'March',
        '4': 'April',
        '5': 'May',
        '6': 'June',
        '7': 'July',
        '8': 'August',
        '9': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }

for n in number_month.keys():
    if number ==  n:
        print(number_month.get(n))
        
if number not in number_month.keys():
    print('ERROR!')
    


#SOLUTION ONE
# for month in number_month.values():
#     print(month)

# if number == '1':
#     month = 'January'
# elif number == '2':
#     month = 'Feburary'
# elif number == '3':
#     month = 'March'
# elif number == '4':
#     month = 'April'
# elif number == '5':
#     month = 'May'
# elif number == '6':
#     month = 'June'
# elif number == '7':
#     month = 'July'
# elif number == '8':
#     month = 'August'
# elif number == '9':
#     month = 'September'
# elif number == '10':
#     month = 'October'
# elif number == '11':
#     month = 'November'
# elif number == '12':
#     month = 'December'
# else:
#     month = '###ERROR!!Your input is not in the range from 1 to 12!###'
    
# print('The name of the month is {}.'.format(month))
