"""
Kata: Simple RSA Implementation

Description:

RSA is a widely used public-key cryptosystem. Like other public-key encryption systems, RSA takes in data and encrypts it using a publicly available key. The private key is then used to decrypt the data. It is useful for sending data to servers because anyone can encrypt their own data, but only the server containing the private key can decrypt it. The driving force behind the difficulty in breaking an RSA encryption is the complexity of prime factorization of very large numbers. In this kata, you will implement an RSA object that can encrypt and decrypt data. For the sake of simplity, we will just use numbers instead of string/text data.

Here is the basic outline of how RSA works (see this link) for more details):

    Pick 2 prime numbers called p and q
    Compute the modulus n by taking the product of p and q (i.e., n = p * q)
    Compute the totient of n, which can be found by the formula phi(n) = (p - 1)(q - 1)
    Pick a positive integer e smaller that is coprime to the totient (see here for an explanation of coprimes). This will be the exponent used in the public key.
    Compute the modular multiplicative inverse of e (mod n) and this will be the exponent used in the private key. For details on modular multiplicative inverses, click here.
    To encrypt a number m into a ciphered number c, use the following formula: c = m^e (mod n)
    To decrypt a number c back into the original number m, use the following formula: m = c^d (mod n)

Note: Since e is generally a much smaller number than d, encryption is much quicker than decryption. In real practice (and in this kata), you will need to implement an optimized decryption method, as the formula given above will probably take too long for some of the more difficult test cases.

Using this, create a class that when initialized with a given p, q, and e, will encrypt and decrypt numbers. You may assume that the test cases will only test valid numbers, but if you are up for the challenge, include primality and coprimality testing! The class should have encrypt and decrypt methods, and its initalizer should take p, q, and e (respectively) as input arguments. You may want to add some utility functions as well (such as Euler's totient function, etc.)

URL: https://www.codewars.com/kata/56f1e42f0cd8bc1e6e001713

Note: I authored this kata.
"""

def phi(p, q):
  return (p-1)*(q-1)

def mmi(a, n):
  t = 0
  new_t = 1
  r = n
  new_r = a
  while new_r != 0:
    quotient = r / new_r
    (t, new_t) = (new_t, t - quotient * new_t) 
    (r, new_r) = (new_r, r - quotient * new_r)
  if t < 0:
    t += n
  return t

class RSA(object):

  def __init__(self, p, q, e):
    self.n = p*q
    self.totient = phi(p,q)
    self.e = e
    self.d = mmi(e, self.totient)

  def encrypt(self, m):
    c = (m**self.e) % self.n
    return c

  def decrypt(self, c):
    d = self.d
    n = self.n
    if c < 1 or d < 0 or n < 1:
      return
    m = 1
    while d > 0:
      if d % 2 == 1:
        m = (m * c) % n
      c = (c * c) % n
      d /= 2
    return m