"""
Kata: Playing with passphrases (6 kyu)

Description:

Everyone knows passphrases. One can choose passphrases from poems, songs, movies names and so on but frequently they can be guessed due to common cultural references. You can get your passphrases stronger by different means. One is the following:

choose a text in capital letters including or not digits and non alphabetic characters,

    shift each letter by a given number but the transformed letter must be a letter (circular shift),
    replace each digit by its complement to 9,
    keep such as non alphabetic and non digit characters,
    downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
    reverse the whole result.

Example:

your text: "BORN IN 2015!", shift 1

1 + 2 + 3 -> "CPSO JO 7984!"

4 "CpSo jO 7984!"

5 "!4897 Oj oSpC"

With longer passphrases it's better to have a small and easy program. Would you write it?

https://en.wikipedia.org/wiki/Passphrase

URL: https://www.codewars.com/kata/playing-with-passphrases

"""

def shift_char(c, n):
    cd = ord(c) + n
    if cd > ord('Z'):
        cd = cd - ord('Z') + ord('A') - 1
    elif cd < ord('A'):
        cd = cd + ord('Z') - ord('A')
    return chr(cd)

def shift_digit(d):
    d = int(d)
    d = 9 - d
    return str(d)
    
def play_pass(s, n):
    p = ''
    for i, c in enumerate(s):
        if c.isdigit():
            p += shift_digit(c)
        elif c.isalpha():
            if i % 2 == 0:
                p += shift_char(c, n).upper()
            else:
                p += shift_char(c, n).lower()
        else:
            p += c
    return p[::-1]