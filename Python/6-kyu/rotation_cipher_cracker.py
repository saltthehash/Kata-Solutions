"""
Kata: Rotation Cipher Cracker (6 kyu)

Description:

Rotation ciphers are very vulnerable to brute force attacks. There are only 25 possible ways to decrypt the message.

Example Encoded Message:ymjxvznwwjqnxhzyj

Possible Decoded Messages:

znkywaoxxkroyiazk, aolzxbpyylspzjbal, bpmaycqzzmtqakcbm,
cqnbzdraanurbldcn, drocaesbbovscmedo, espdbftccpwtdnfep,
ftqecguddqxueogfq, gurfdhveeryvfphgr, hvsgeiwffszwgqihs,
iwthfjxggtaxhrjit, jxuigkyhhubyiskju, kyvjhlziivczjtlkv,
lzwkimajjwdakumlw, maxljnbkkxeblvnmx, nbymkocllyfcmwony,
ocznlpdmmzgdnxpoz, pdaomqennaheoyqpa, qebpnrfoobifpzrqb,
rfcqosgppcjgqasrc, sgdrpthqqdkhrbtsd, thesquirreliscute,
uiftrvjssfmjtdvuf, vjguswkttgnkuewvg, wkhvtxluuholvfxwh,
xliwuymvvipmwgyxi

If you scan through the list you will see only a few that contain an english word longer than two characters. thesquirreliscute is the only one that could be completely seperated into english words to form the message "the squirrel is cute".

Your job for this kata is to make a function that will give all possible decoded messages given the encoded message and suspected contents.

decode('ymjxvznwwjqnxhzyj','squirrel') # returns ['thesquirreliscute']
decode('lzwespnsdmwakafxafalq','max')  # returns ['maxftqotenxblbgybgbmr', 'themaxvalueisinfinity']

URL: https://www.codewars.com/kata/rotation-cipher-cracker
"""

from numpy import array
def decode(msg,contents):
  msgs = []
  chars = array(map(ord, msg))
  for i in xrange(1,26):
      new_chars = chars + i
      for i, c in enumerate(new_chars):
          if c > 122:
              new_chars[i] = 97 + (c-122) - 1
          elif c < 97:
              new_chars[i] = 122 - (97-c) + 1
      new_msg = ''.join(map(chr, new_chars))
      if contents in new_msg:
          msgs.append(new_msg)
  return msgs