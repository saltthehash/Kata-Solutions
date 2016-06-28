"""
Kata: Dbftbs Djqifs ("Caeser Cipher" with 1 letter shift) (6 kyu)

Description:

Caesar Ciphers are one of the most basic forms of encryption. It consists of a message and a key, and it shifts the letters of the message for the value of the key.

Your task is to create a function encryptor that takes 2 arguments - key and message - and returns the encrypted message.

A message 'Caesar Cipher' and a key of 1 returns 'Dbftbs Djqifs'.

A message 'Caesar Cipher' and a key of -1 returns 'Bzdrzq Bhogdq'.

Make sure to only shift letters, and be sure to keep the cases of the letters the same. All punctuation, numbers, spaces, and so on should remain the same.

Also be aware of keys greater than 26 and less than -26. There's only 26 letters in the alphabet!


URL: https://www.codewars.com/kata/dbftbs-djqifs
"""

def encryptor(key, message):
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