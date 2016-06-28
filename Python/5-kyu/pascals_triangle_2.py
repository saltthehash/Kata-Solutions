"""
Kata: Pascal's Triangle #2 (5 kyu)

Description:

Here you will create the classic pascal's triangle. Your function will be passed the depth of the triangle and you code has to return the corresponding pascal triangle upto that depth

The triangle should be returned as a nested array.

for example:

pascal(5) # should return [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

To build the triangle, start with a single 1 at the top, for each number in the next row you just take the two numbers above it and add them together (except for the edges, which are all "1"). eg

          [1]
        [1   1]
       [1  2  1]
      [1  3  3  1]

here you get the 3 by adding the 2 and 1 above it.

URL: https://www.codewars.com/kata/pascals-triangle-number-2
"""

def pascal(p):
    P = [[1],[1, 1]]
    if p < 3: return P[0:p]
    while len(P) < p:
        last = P[-1]
        layer = [1]
        for i in xrange(len(last)-1):
            layer.append(last[i]+last[i+1])
        layer.append(1)
        P.append(layer)
    return P