"""
Kata: First Variation on Caeser Cipher (5 kyu)

Description:

The action of a Caesar cipher is to replace each plaintext letter with a different one a fixed number of places up or down the alphabet.

This program performs a variation of the Caesar shift. The shift increases by 1 for each character (on each iteration).

If the shift is initially 1, the first character of the message to be encoded will be shifted by 1, the second character will be shifted by 2, etc...
Coding: Parameters and return of function "movingShift"

param s: a string to be coded

param shift: an integer giving the initial shift

The function "movingShift" first codes the entire string and then returns an array of strings containing the coded string in 5 parts (five parts because, to avoid more risks, the coded message will be given to five runners, one piece for each runner).

If possible the message will be evenly split between the five runners; if not possible, parts 1, 2, 3, 4 will be longer and part 5 shorter. The fifth part can have length equal to the other ones or shorter. If there are many options of how to split, choose the option where the fifth part has the longest length, provided that the previous conditions are fulfilled. If the last part is the empty string this empty string must be shown in the resulting array.

For example, if the coded message has a length of 17 the five parts will have lengths of 4, 4, 4, 4, 1. The parts 1, 2, 3, 4 are evenly split and the last part of length 1 is shorter. If the length is 16 the parts will be of lengths 4, 4, 4, 4, 0. Parts 1, 2, 3, 4 are evenly split and the fifth runner will stay at home since his part is the empty string.

You will also implement a "demovingShift" function with two parameters
Decoding: parameters and return of function "demovingShift"

1) an array of strings: s (possibly resulting from "movingShift", with 5 strings)

2) an int shift

"demovingShift" returns a string.
Example:

u = "I should have known that you would have a perfect answer for me!!!"

movingShift(u, 1) returns :

v = ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"]

(quotes added in order to see the strings and the spaces, your program won't write these quotes, see Example Test Cases)

and demovingShift(v, 1) returns u.
Ref:

Caesar Cipher : http://en.wikipedia.org/wiki/Caesar_cipher

URL: https://www.codewars.com/kata/5508249a98b3234f420000fb
"""

def moving_shift(s, shift):
    new_s = ''
    for c in s:
        if not c.isalpha():
            new_s += c
        elif c.isupper():
            new_s += char_shift(shift, c, 65, 90)
        elif c.islower():
            new_s += char_shift(shift, c, 97, 122)
        shift += 1
        if shift > 26: shift -= 26
    if len(s) % 5 == 0:
        sl = len(s)/5
    else:
        sl = (len(s)/5)+1
    strs = []
    for i in xrange(4):
        a = i*sl
        b = a + sl
        strs.append(new_s[a:b])
    strs.append(new_s[b:])
    print strs
    return strs

def char_shift(key, char, lo, hi):
    new_let = ord(char) + key
    if new_let > hi:
        new_let = lo + (new_let - hi) - 1
    elif new_let < lo:
        new_let = hi - (lo - new_let) + 1
    return chr(new_let)

def demoving_shift(s, shift):
    s = ''.join(s)
    new_s = ''
    for c in s:
        if not c.isalpha():
            new_s += c
        elif c.isupper():
            new_s += char_shift(-shift, c, 65, 90)
        elif c.islower():
            new_s += char_shift(-shift, c, 97, 122)
        shift += 1
        if shift > 26: shift -= 26
    return new_s