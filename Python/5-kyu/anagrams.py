"""
Kata: Where my anagrams at? (5 kyu)

Description:

What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

URL: https://www.codewars.com/kata/where-my-anagrams-at
"""

from itertools import permutations
def anagrams(word, words):
    perms = [''.join(p) for p in permutations(word, len(word))]
    return [w for w in words if w in perms]