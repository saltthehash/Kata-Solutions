"""
Kata: Super Duper Easy

Description:

Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".

URL: https://www.codewars.com/kata/super-duper-easy

"""

def problem(a):
    if type(a) is int or type(a) is float:
        return a*50 + 6
    else:
        return "Error"