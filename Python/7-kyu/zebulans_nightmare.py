"""
Kata: Zebulan's Nightmare (7 kyu)

Description:

Zebulan has worked hard to write all his python code in strict compliance to PEP8 rules. In this kata, you are a mischevious hacker that has set out to sabatoge all his good code.

Your job is to take PEP8 compatible function names and convert them to camelCase. For example:

zebulansNightmare('camel_case') == 'camelCase'
zebulansNightmare('zebulans_nightmare') == 'zebulansNightmare'
zebulansNightmare('get_string') == 'getString'
zebulansNightmare('convert_to_uppercase') == 'convertToUppercase'
zebulansNightmare('main') == 'main'

URL: https://www.codewars.com/kata/zebulans-nightmare
"""

import re

def zebulansNightmare(functionName):
    A = re.findall(r'_[a-z]', functionName)
    B = [b[1].upper() for b in A]
    for a, b in zip(A,B):
        functionName = re.sub(a, b, functionName)
    return functionName