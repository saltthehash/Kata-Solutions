"""
Kata: Simple Pig Latin (5 kyu)

Description:

Move the first letter of each word to the end of it, then add 'ay' to the end of the word.

pig_it('Pig latin is cool') # igPay atinlay siay oolcay

URL: https://www.codewars.com/kata/simple-pig-latin
"""

def pig_it(text):
    words = text.split(' ')
    pl_words = []
    for w in words:
        if w.isalpha():
            if len(w) > 1:
                pl_words.append(w[1:]+w[0]+'ay')
            else:
                pl_words.append(w + 'ay')
        else:
            pl_words.append(w)
    pl_text = ' '.join(pl_words)
    return pl_text