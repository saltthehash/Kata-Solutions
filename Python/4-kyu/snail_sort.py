"""
Kata: Snail Sort (4 kyu)

Description:
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

This image will illustrate things more clearly:
http://www.haan.lu/files/2513/8347/2456/snail.png

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as [[]]


URL: https://www.codewars.com/kata/snail
"""

def snail(array):
    snail = []
    n = len(array)
    n2 = n*n
    row_len = n
    col_len = n
    row_start = 0
    col_start = 0
    count = 0
    n_count = 0
    if not array[0]:
        return []
    while True:
        ## Move right
        for c in xrange(col_start, col_start + row_len):
            snail.append(array[row_start][c])
            count += 1
            n_count += 1
            if n_count >= n2: return snail
        col_start += (count - 1)
        row_start += 1
        col_len -= 1
        count = 0
        ## Move down
        for r in xrange(row_start, row_start + col_len):
            snail.append(array[r][col_start])
            count += 1
            n_count += 1
            if n_count >= n2: return snail
        row_start += (count - 1)
        col_start -= 1
        count = 0
        row_len -= 1
        ## Move left
        for c in xrange(col_start, col_start - row_len, -1):
            snail.append(array[row_start][c])
            count += 1
            n_count += 1
            if n_count >= n2: return snail
        col_start -= (count - 1)
        row_start -= 1
        col_len -= 1
        count = 0
        ## Move up
        for r in xrange(row_start, row_start - col_len, -1):
            snail.append(array[r][col_start])
            count += 1
            n_count += 1
            if n_count >= n2: return snail
        row_start -= (count - 1)
        col_start += 1
        count = 0
        row_len -= 1