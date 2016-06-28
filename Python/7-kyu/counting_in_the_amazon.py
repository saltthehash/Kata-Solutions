"""
Kata: Counting in the Amazon (7 kyu)

Description:

The Arara are an isolated tribe found in the Amazon who count in pairs. For example one to eight is as follows:

1 = anane
2 = adak
3 = adak anane
4 = adak adak
5 = adak adak anane
6 = adak adak adak
7 = adak adak adak anane
8 = adak adak adak adak

Take a given number and return the Arara's equivalent.

e.g.

count_arara(3) # -> 'adak anane'

count_arara(8) # -> 'adak adak adak adak'

https://en.wikipedia.org/wiki/Arara_people


URL: https://www.codewars.com/kata/counting-in-the-amazon
"""

def count_arara(n):
    if n%2 == 0: return 'adak '*((n-2)/2) + 'adak'
    else: return 'adak '*(n/2) + 'anane'