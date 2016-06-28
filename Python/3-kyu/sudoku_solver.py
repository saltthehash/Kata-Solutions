"""
Kata: Sudoku Solver (3 kyu)

Description:

Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.

The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.

For Sudoku rules, see the Wikipedia article.

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku(puzzle)
# Should return
# [[5,3,4,6,7,8,9,1,2],
#  [6,7,2,1,9,5,3,4,8],
#  [1,9,8,3,4,2,5,6,7],
#  [8,5,9,7,6,1,4,2,3],
#  [4,2,6,8,5,3,7,9,1],
#  [7,1,3,9,2,4,8,5,6],
#  [9,6,1,5,3,7,2,8,4],
#  [2,8,7,4,1,9,6,3,5],
#  [3,4,5,2,8,6,1,7,9]]

URL: https://www.codewars.com/kata/sudoku-solver
"""

def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    solver = Sudoku(puzzle)
    solver.solve()
    return solver.board

class Sudoku(object):

    def __init__(self, board):
        self.board = board
        self.possible_answers = [[[]]*9]*9

    def set_possible_answers(self, r, c):
        ## Get row, column, and square elements
        row = self.get_row(r)
        col = self.get_col(c)
        square = self.get_square(r, c)
        ## Initialize set of all possible answers (1-9)
        poss_set = set(range(1,10))
        ## Create a removal set from the elements in row, col, and square
        remove_set = set(row + col + square)
        ## Set difference removes ineligible elements to form actual possible answers
        new_poss = list(poss_set - remove_set)
        self.possible_answers[r][c] = new_poss

    def solve(self):
        ## Repeating process while the solution is still incomplete
        while not self.is_complete:
            for row in xrange(9):
                for col in xrange(9):
                    ## Only looking at zero-elements (unfilled squares)
                    if self.board[row][col] == 0:
                        self.set_possible_answers(row, col)
                        ## If length of possible answers is 1, theres only 1 possible solution
                        if len(self.possible_answers[row][col]) == 1:
                            ## Remove solution from possible answers and fill in the blank
                            self.board[row][col] = self.possible_answers[row][col].pop()

    @property
    def is_complete(self):
        # Check if the board is complete
        # i.e. see if there are no zero elements left
        for row in self.board:
            if 0 in row:
                return False
        return True

    def get_row(self, r):
        return [n for n in self.board[r] if n != 0]

    def get_col(self, c):
        return [row[c] for row in self.board if row[c] != 0]

    def get_square(self, r, c):
        ## Given the row and column indices of an element,
        ## get the elements of the square it belongs to.
        sq = []
        i = r/3 
        j = c/3
        ri = xrange(i*3, (i*3)+3)
        rj = xrange(j*3, (j*3)+3)
        for ni in ri:
            for nj in rj:
                n = self.board[ni][nj]
                if n != 0:
                    sq.append(n)
        return sq