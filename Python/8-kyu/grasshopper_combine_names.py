"""
Kata: Grasshopper - Combine strings (8 kyu)

Description:
Combine strings function

Create a function named combineNames(combine_names in python, ruby) that accepts two parameters (first and last name). The function should return the full name.

Example:

combine_names('James', 'Stevens')

returns:

'James Stevens'

URL: https://www.codewars.com/kata/grasshopper-combine-strings
"""

def combine_names(first, last):
    assert isinstance(first, str) and isinstance(last, str)
    return first + ' ' + last