"""
Kata: Capitals first!

Description: 

Create a function that takes an input String and returns a String, where all the uppercase words of the input String are in front and all the lowercase words at the end. The order of the uppercase and lowercase words should be the order in which they occur.

If a word starts with a number or special character, skip the word and leave it out of the result.

Input String will not be empty.

For an input String: "hey You, Sort me Already!" the function should return: "You, Sort Already! hey me"


URL: https://www.codewars.com/kata/capitals-first

"""

import re
def capitals_first(string):
    words = re.split(' ', string)
    capitals = []
    for i in xrange(len(words)-1, -1, -1):
        if not words[i][0].isalpha():
            words.remove(words[i])
        elif not words[i][0].islower():
            capitals.append(words.pop(i))
    capitals.reverse()
    return ' '.join(capitals + words)