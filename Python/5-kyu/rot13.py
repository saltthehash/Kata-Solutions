"""
Kata: Rot13 (5 kyu)

Description:

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using "encode" in Python is considered cheating.

URL: https://www.codewars.com/kata/rot13-1
"""

import string
def rot13(message):
    key = 13
    if key < -26:
        while key < -26:
            key += 26
    elif key > 26:
        while key > 26:
            key -= 26
    new_msg = ''
    for char in message:
        if not char.isalpha():
            new_msg += char
        elif char.isupper():
            new_msg += char_shift(key, char, 65, 90)
        elif char.islower():
            new_msg += char_shift(key, char, 97, 122)
    return new_msg

def char_shift(key, char, lo, hi):
    new_let = ord(char) + key
    if new_let > hi:
        new_let = lo + (new_let - hi) - 1
    elif new_let < lo:
        new_let = hi - (lo - new_let) + 1
    return chr(new_let)