"""
Kata: NIM (4 kyu)

Description:

This kata explores writing an AI for a two player, turn based game called NIM.

The Board

The board starts out with several piles of straw. Each pile has a random number of straws.

Pile 0: ||||

Pile 1: ||

Pile 2: |||||

Pile 3: |

Pile 4: ||||||

...or more concisely: [4,2,5,1,6]
The Rules

The players take turns picking a pile, and removing any number of straws from the pile they pick
A player must pick at least one straw
If a player picks the last straw, she wins!
The Task

In this kata, you have to write an AI to play the straw picking game.

You have to encode an AI in a function choose_move (or chooseMove, or choose-move) that takes a board, represented as a list of positive integers, and returns

[pile_index, number_of_straws]
Which refers to an index of a pile on the board, and some none-zero number of straws to draw from that pile.

The test suite is written so that your AI is expected to play 50 games and win every game it plays.


URL: https://www.codewars.com/kata/nim/
"""
def calc_nim_sum(game_state):
    """Calculates the digital sum aka nim sum"""
    # Compute bit strings for each number
    pile_bins = [bin(pile)[2:] for pile in game_state]
    
    # Want to find the max length to make each the same length
    # by appending extra 0s to the left
    lens = [len(pile) for pile in pile_bins]
    max_len = max(lens)
    pile_bins = ["0"*(max_len - len(pile))+pile for pile in pile_bins]
    
    # Computing the nim sum as a bit string
    result = ""
    for i in xrange(max_len):
        res = 0
        for pile in pile_bins:
            res += int(pile[i])
            res %= 2
        result += str(res)
    return result
        
        
def choose_move(game_state):
    """Chooses a move to play given a game state"""
    # First get nim sum
    nim_sum = calc_nim_sum(game_state)
    
    # Now find the first 1-bit in the sum
    first_one = nim_sum.find("1")
    first_one_ind = len(nim_sum) - first_one - 1
    
    # Want to pick pile that has most sticks
    # after dropping all bits from each pile number
    # before first 1-bit in nim sum (via modulo)
    mod = 2**(first_one_ind+1)
    mod_piles = [pile % mod for pile in game_state]
    max_mod = -1
    max_mod_ind = -1
    for i, m_pile in enumerate(mod_piles):
        if m_pile > max_mod:
            max_mod = m_pile
            max_mod_ind = i
    
    # Now to convert the original pile number back to binary
    # and calculate the desired new pile binary
    # such that the new nim sum is all 0s
    max_mod_bin = bin(game_state[max_mod_ind])[2:]
    max_mod_bin = "0"*(len(nim_sum)-len(max_mod_bin))+max_mod_bin
    new_pile_bin = ""
    for i in xrange(len(nim_sum)):
        if nim_sum[i] == "1":
            new_pile_bin += str((int(max_mod_bin[i])+1)%2)
        else:
            new_pile_bin += max_mod_bin[i]
            
    # Compute the number of sticks taken from the chosen pile
    # by subtracting new pile from old pile (difference = number taken)
    take = game_state[max_mod_ind] - int(new_pile_bin, base=2)
    return (max_mod_ind, take)