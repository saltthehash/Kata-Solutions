"""
Kata: Find divisors number (7 kyu)

Description:

Find the number of divisors of a positive integer n.

Example:

divisors(4) -> 3 -- 1, 2, 4
divisors(5) -> 2 -- 1, 5
divisors(12) -> 6 -- 1, 2, 3, 4, 6, 12
divisors(30) -> 8 -- 1, 2, 3, 5, 6, 10, 15, 30

URL: https://www.codewars.com/kata/find-divisors-number
"""

def divisors(n):
    if n < 3: return 1
    nd = 2
    for d in xrange(2,(n/2)+1):
        if n%d == 0: nd += 1
    return nd