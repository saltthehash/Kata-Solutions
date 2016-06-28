"""
Kata: String chunks (7 kyu)

Description:

You should write a function that takes a string and a positive integer n, splits the string into parts of n length and returns them in an array. It is ok for the last element to have less characters than n.

If n is not a valid size(> 0) (or is absent), you should return an empty array.

If n is greater than the lenght of the string, you should return an array with the only element being the same string.

Examples:

string_chunk('codewars', 2) # ['co', 'de', 'wa', 'rs']
string_chunk('thiskataeasy', 4) # ['this', 'kata', 'easy']
string_chunk('hello world', 3) # ['hel', 'lo ', 'wor', 'ld']
string_chunk('sunny day', 0) # []

URL: https://www.codewars.com/kata/55b4f9906ac454650900007d
"""

def string_chunk(s, n = 0):
    if n < 1 or not isinstance(n, int): return []
    return [s[i:i+n] for i in xrange(0,len(s),n)]