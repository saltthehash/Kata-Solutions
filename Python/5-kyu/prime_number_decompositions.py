"""
Kata: Prime number decompositions (5 kyu)

Description:

You have to code a function getAllPrimeFactors wich take an integer as parameter and return an array containing its prime decomposition by ascending factors, if a factors appears multiple time in the decomposition it should appear as many time in the array.

exemple: getAllPrimeFactors(100) returns [2,2,5,5] in this order.

This decomposition may not be the most practical.

You should also write getUniquePrimeFactorsWithCount, a function which will return an array containing two arrays: one with prime numbers appearing in the decomposition and the other containing their respective power.

exemple: getUniquePrimeFactorsWithCount(100) returns [[2,5],[2,2]]

You should also write getUniquePrimeFactorsWithProducts an array containing the prime factors to their respective powers.

exemple: getUniquePrimeFactorsWithProducts(100) returns [4,25]

Errors, if:

    n is not a number
    n not an integer
    n is negative or 0

The three functions should respectively return [], [[],[]] and [].

Edge cases:

    if n=0, the function should respectively return [], [[],[]] and [].
    if n=1, the function should respectively return [1], [[1],[1]], [1].
    if n=2, the function should respectively return [2], [[2],[1]], [2].

The result for n=2 is normal. The result for n=1 is arbitrary and has been chosen to return a usefull result. The result for n=0 is also arbitrary but can not be chosen to be both usefull and intuitive. ([[0],[0]] would be meaningfull but wont work for general use of decomposition, [[0],[1]] would work but is not intuitive.)


URL: https://www.codewars.com/kata/prime-number-decompositions
"""

def gen_primes(n):
    D = {}
    q = 2
    
    while q <= n:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def getAllPrimeFactors(n):
    if n == 0 or not str(n).isdigit(): return []
    if n > 0 and n <= 2: return [n]
    ps = []
    for p in gen_primes(n/2):
        while n%p == 0:
            ps.append(p)
            n /= p
    return ps
  

def getUniquePrimeFactorsWithCount(n):
    if n == 0 or not str(n).isdigit(): return [[],[]]
    if n > 0 and n <= 2: return [[n],[1]]
    np = []
    ps = []
    for p in gen_primes(n/2):
        if n%p != 0: continue
        ni = 0
        while n%p == 0:
            ni += 1
            n /= p
        np.append(ni)
        ps.append(p)
    return [ps, np]

def getUniquePrimeFactorsWithProducts(n):
    if n == 0 or not str(n).isdigit(): return []
    if n > 0 and n <= 2: return [n]
    pf = []
    for p in gen_primes(n/2):
        if n%p != 0: continue
        pi = 1
        while n%p == 0:
            pi *= p
            n /= p
        pf.append(pi)
    return pf