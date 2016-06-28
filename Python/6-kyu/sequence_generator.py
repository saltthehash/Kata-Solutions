"""
Kata: Sequence generator (6 kyu)

Description:

Write a generator sequence_gen ( sequenceGen in JavaScript) that, given the first terms of a sequence will generate a (potentially) infinite amount of terms, where each subsequent term is the sum of the previous x terms where x is the amount of initial arguments (examples of such sequences are the Fibonacci, Tribonacci and Lucas number sequences).
Examples

fib = sequence_gen(0, 1)
fib.next() = 0 # first term (provided)
fib.next() = 1 # second term (provided)
fib.next() = 1 # third term (sum of first and second terms)
fib.next() = 2 # fourth term (sum of second and third terms)
fib.next() = 3 # fifth term (sum of third and fourth terms)
fib.next() = 5 # sixth term (sum of fourth and fifth terms)
fib.next() = 8 # seventh term (sum of fifth and sixth terms)

trib = sequence_gen(0,1,1)
trib.next() = 0 # first term (provided)
trib.next() = 1 # second term (provided)
trib.next() = 1 # third term (provided)
trib.next() = 2 # fourth term (sum of first, second and third terms)
trib.next() = 4 # fifth term (sum of second, third and fourth terms)
trib.next() = 7 # sixth term (sum of third, fourth and fifth terms)

lucas = sequence_gen(2,1)
[lucas.next() for _ in range(10)] = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]

Note: You can assume you will get at least one argument and any arguments given will be valid (positive or negative integers) so no error checking is needed.

Note for Ruby users: sequence_gen should return an Enumerator object.

Any feedback/suggestions would much appreciated.

URL: https://www.codewars.com/kata/sequence-generator

"""

from collections import deque
def sequence_gen(*args):
    a = deque(args)
    for i in a:
        yield i
    while True:
        s = sum(a)
        yield s
        a.popleft()
        a.append(s)