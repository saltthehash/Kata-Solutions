"""
Kata: Binary Addition (7 kyu)

Description:

Implement a function that successfully adds two numbers together and returns their solution in binary. The conversion can be done before, or after the addition of the two.

The binary number returned should be a string!


URL: https://www.codewars.com/kata/binary-addition
"""

def add_binary(a,b):
    c = a+b
    s = ''
    while c > 0:
        s = str(c%2) + s
        c /= 2
    return s