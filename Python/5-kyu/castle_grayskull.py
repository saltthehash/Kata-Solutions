"""
Kata: By the Power Set of Castle Grayskull (5 kyu)

Description:

Write a function that returns all of the sublists of a list or Array.

Your function should be pure; it cannot modify its input.

Example:

power([1,2,3])
# => [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

For more details regarding this, see the power set entry in wikipedia.


URL: https://www.codewars.com/kata/by-the-power-set-of-castle-grayskull
"""

from itertools import combinations
def power(a):
    n = len(a)
    l = []
    for i in xrange(n+1):
        for c in combinations(a, i):
            l.append(list(c))
    return l