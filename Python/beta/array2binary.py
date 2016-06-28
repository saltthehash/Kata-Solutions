"""
Kata: Array2Binary addition

Description:

Given an array containing only integers, add all the elements and return the binary equivalent of that sum.

If the array contains any non-integer element (e.g. an object, a float, a string and so on), return false.

Note: The sum of an empty array is zero.

arr2bin(1,2) == '11'
arr2bin(1,2,'a') == False

URL: https://www.codewars.com/kata/559576d984d6962f8c00003c

"""

def arr2bin(arr):
    n_sum = 0
    for n in arr:
        if type(n) is not int:
            return False
        n_sum += n
    return bin(n_sum)[2:]