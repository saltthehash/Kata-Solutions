"""
Kata: Validate Sudoku with size `NxN` (4 kyu)

Description:

Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled out correctly.

The data structure is a multi-dimensional Array, ie:

[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]

Rules for validation

    Data structure dimension: NxN where N > 0 and √N == integer
    Rows may only contain integers: 1..N (N included)
    Columns may only contain integers: 1..N (N included)
    'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)


URL: https://www.codewars.com/kata/validate-sudoku-with-size-nxn
"""

from math import sqrt

class Sudoku(object):
    
    def __init__(self, board):
        self.board = board
        self.n = len(self.board)
        self.sqrtn = int(sqrt(self.n))
    
    def is_valid(self):
        # Check size and contents
        for row in self.board:
            if len(row) != self.n:
                return False
            for n in row:
                # Make sure every entry is an integer and is in range
                if not type(n) is int or not self.in_range(n):
                    return False

        # Check rows and columns
        for n in xrange(self.n):
            if not self.valid_row(n) or not self.valid_col(n):
                return False
        # Check squares
        for i in xrange(self.sqrtn):
            for j in xrange(self.sqrtn):
                if not self.valid_square(i,j):
                    return False
        return True

    def in_range(self, n):
        return n >= 1 and n <= self.n
        
    
    def valid_row(self, i):
        valid = [False]*self.n
        row = self.board[i]
        for n in row:
            try:
                valid[n-1] = True
            except IndexError:
                return False
        return all(valid)
    
    def valid_col(self, j):
        valid = [False]*self.n
        col = [row[j] for row in self.board]
        for n in col:
            try:
                valid[(n-1)] = True
            except IndexError:
                return False
        return all(valid)
    
    def valid_square(self, ni, nj):
        ni *= self.sqrtn
        nj *= self.sqrtn
        valid = [False]*self.n
        for i in xrange(ni, ni+self.sqrtn):
            for j in xrange(nj, nj+self.sqrtn):
                n = self.board[i][j]
                try:
                    valid[n-1] = True
                except IndexError:
                    return False
        return all(valid)