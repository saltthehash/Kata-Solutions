"""
Kata: Can you get the loop? (3 kyu)

Description:

You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.

Your objective is to determine the length of the loop.

For example in the following picture the tail's size is 3 and the loop size is 11.

http://i42.tinypic.com/27wrmed.png

// Use the `getNext' method or 'next' property to get the following node.

node.getNext()
node.next


URL: https://www.codewars.com/kata/52a89c2ea8ddc5547a000863

"""
def loop_size(node):
    current = node
    i = 1
    # Label visited nodes as visited
    # and with their number
    setattr(current, "visited", True)
    setattr(current, "n", i)
    # While the next node hasn't been labeled with visited
    # label it and move to the next node
    while not hasattr(current.next, "visited"):
        current = current.next
        setattr(current, "visited", True)
        i += 1
        setattr(current, "n", i)
    # Compute the loop size
    n = (i+1)-current.next.n
    return n