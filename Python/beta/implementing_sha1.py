"""
Kata: Implementing SHA-1

Description:

SHA-1 is arguably the most widely used hash algorithm in the world at the moment. However, due to speculation that the hash algorithm will be broken soon, it will be eventually phased out. Nonetheless, it is definitely worth learning since it is extremely similar to its successor, SHA-2, which is still believed to be secure. If you would like to learn more about SHA-1, I'd recommend scanning the Wikipedia page but even better is this lecture on how SHA-1 works.

Here is a general outline of the algorithm:

Initial constants/variables:

    H0 = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0], these will serve as the initial hash values, also called registers. They will also be reffered to individually as A, B, C, D, and E, respectively.

    K = [0x5A827999, 0x6ED9EBA1, 0x8F1BBCDC, 0xCA62C1D6], these will serve as constants used in the compression phase

The Four Functions:

    F1(B, C, D) = (B & C) | ((~B) & D)
    F2(B, C, D) = B ^ C ^ D
    F3(B, C, D) = (B & C) | (B & D) | (C & D)
    F4(B, C, D) = B ^ C ^ D

Note: & is the bitwise AND operator, | is the bitwise OR operator, ^ is the bitwise XOR (exclusive OR) operator, and ~ is the bitwise NOT operator.

Pre-Processing:

    Given an input M, determine its length in bits.
    Break the input M into 512-bit chunks, maintaining the original order.
    At the end of the last chunk, add a 1-bit (unless the chunk is already 512-bits, in which case start a new chunk with a 1 bit).
    Pad this chunk with enough 0 bits so that the chunk has exactly 64 bits left at the end. In other words, fill the chunk until it is 448 bits long.
    Complete the last chunk by appending a 64-bit representation of the original bit length measured at the beginning.

Compression: Repeat the following steps for each chunk in order:

    Split the current chunk into 16 32-bit words. However, you will need a total of 80 words. Compute the following 64 words using the following formula where leftrotate is a function that rotates the bits of its first argument by an amount specified in its second: w[i] = leftrotate(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1)

    Save the current values of H0 aka A, B, C, D, and E.
    The compression function consists of 80 rounds, which is split into four equal 20-round stages. A, B, C, D, and E are fed into the compression function and are modified. Parts of the compression function depend on what stage it is.
    At the end of 80 rounds, add the new A, B, C, D, and E values to their values from the start of the 80 rounds, applying modulo 2^32. The following is a depiction of a round in the compression function:


https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/SHA-1.svg/365px-SHA-1.svg.png
An SHA-1 stage

The F represents one of the F functions (F1 for stage 1, F2 for stage 2, etc.), the <<<n represents a left bit rotation by n bits, the red crossed squares represent addition modulo 2^32, Kt represents the K constant for the t'th stage, and Wt stands for the Wth word of the chunk.

Completion:

    Once every chunk has been processed, concatenate the bits of A, B, C, D, and E together and the resulting value is the hash value. You can also convert the 5 registers into hex strings and concatenate those, since hash values are often given in hex string format.

Implement this without cheating! No using built-in hash libraries/modules! Assume that message input is always a string.

URL: https://www.codewars.com/kata/56f2f3dfe40b70a005001389

Note: I authored this kata.
"""

from math import log, floor

def left_rotate(x, n):
  return ((x << n) | (x >> (32-n))) & 0xFFFFFFFF

def log2(x):
  return log(x)/log(2)

def bit_len(x):
  return int(floor(log2(x)) + 1)

def str_to_int(s):
  n = 0
  for c in s:
    n <<= 8
    n += ord(c)
  return n

def int_to_str(n):
  s = ''
  for i in xrange((bit_len(n)/8) + 1):
    a = n & 0xFF
    s = chr(a) + s
    n >>= 8
  return s

class SHA1(object):

  f = [lambda B,C,D: (B & C) | ((~B) & D),
     lambda B,C,D: B ^ C ^ D,
     lambda B,C,D: (B & C) | (B & D) | (C & D),
     lambda B,C,D: B ^ C ^ D
  ]

  K = [0x5A827999,
     0x6ED9EBA1,
     0x8F1BBCDC,
     0xCA62C1D6
  ]

  H0 = [0x67452301,
      0xEFCDAB89,
      0x98BADCFE,
      0x10325476,
      0xC3D2E1F0
  ]

  def update(self, message):
    if hasattr(self, 'message'):
      self.message += message
    else:
      self.message = message

  def digest(self):
    self.process()
    self.H = SHA1.H0
    for i in xrange(self.n_blocks):      
      a0, b0, c0, d0, e0 = self.H
      for j in xrange(80):
        self.round(i, j)
      self.H[0] = (self.H[0] + a0) & 0xFFFFFFFF
      self.H[1] = (self.H[1] + b0) & 0xFFFFFFFF
      self.H[2] = (self.H[2] + c0) & 0xFFFFFFFF
      self.H[3] = (self.H[3] + d0) & 0xFFFFFFFF
      self.H[4] = (self.H[4] + e0) & 0xFFFFFFFF

    hash_val = "%08x%08x%08x%08x%08x" % (self.H[0], self.H[1], self.H[2], self.H[3], self.H[4])
    return hash_val

  def process(self):
    length = len(self.message)
    orig_bit_length = length * 8
    self.n_blocks = (length/64) + 1 + ((length % 64) / 56)
    total_bit_length = self.n_blocks * 512
    bit_length_length = bit_len(orig_bit_length)
    bl_byte_space = bit_length_length/8

    if bit_length_length % 8 != 0:
      bl_byte_space += 1
    bl_bit_space = bl_byte_space*8
    bit_shift = bl_bit_space
    self.blocks = []
    m = 0
    lbits = 0
    started_padding = False
    for i in xrange(self.n_blocks):
      W = []
      for j in xrange(16):
        word = 0
        for k in xrange(4):
          s = 8 * k
          word <<= 8
          if m < length:
            c = ord(self.message[m])
            word += c
          else:
            if not started_padding:
              word += 0x80
              started_padding = True
            else:
              curr_len = ((m + 1) * 8)
              if (total_bit_length - curr_len) <= bl_bit_space:
                byte = (orig_bit_length & (0xFF << (bl_bit_space - lbits))) >> bit_shift
                word += byte
                lbits += 8
                bit_shift -= 8
          m += 1
        W.append(word)
      for j in xrange(16, 80):
        w_rot = W[j-16] ^ W[j-14] ^ W[j-8] ^ W[j-3]
        W.append(left_rotate(w_rot, 1))
      self.blocks.append(W)

  def round(self, block_n, round_n):
    i = block_n
    j = round_n
    t = round_n/20
    A, B, C, D, E = self.H
    W = self.blocks[i][j]
    F = self.f[t](B, C, D)
    K = self.K[t]
    rotated_A = left_rotate(A, 5)
    temp = E + F + rotated_A + W + K & 0xFFFFFFFF
    self.H = [temp, A, left_rotate(B, 30), C, D]