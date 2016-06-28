"""
Kata: Printing Array elements with Comma delimiters (8 kyu)

Description:

Input: Array of elements

["h","o","l","a"]

Output: String with comma delimited elements of the array in th same order.

"h,o,l,a"

URL: https://www.codewars.com/kata/printing-array-elements-with-comma-delimiters
"""

def print_array(arr):
    return ",".join([str(e) for e in arr])