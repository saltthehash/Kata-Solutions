"""
Kata: Design a Simple Automaton (Finite State Machine) (4 kyu)

Description:

Create a finite automaton that has three states. Finite automatons are the same as finite state machines for our purposes.

Our simple automaton, accepts the language of A, defined as {0, 1} and should have three states,
q1, q2, and q3.

q1 is our start state. We begin reading commands from here.
q2 is our accept state. We return true if this is our last state.

q1 moves to q2 when given a 1, and stays at q1 when given a 0.
q2 moves to q3 when given a 0, and stays at q2 when given a 1.
q3 moves to q2 when given a 0 or 1.

Our automaton should return whether we end in our accepted state, or not (true/false.)

Here's an example.

a = Automaton()
# Do anything you need to set up this automaton's states.
is_accepted = a.read_commands(["1", "0", "0", "1", "0"])

We make these transitions based on the input of ["1", "0", "0", "1", "0"],

1 q1 -> q2
0 q2 -> q3
0 q3 -> q2
1 q2 -> q2
0 q2 -> q3

We end in q3, which is not our accept state, so return false.

The input of ["1", "0", "0", "1", "0"] would cause us to return false, as we would end in q3.

I have started you off with the bare bones of the Automaton object.

class Automaton(object):

    def __init__(self):
        self.states = []

    def read_commands(self, commands):
        # Return True if we end in our accept state, False otherwise

my_automaton = Automaton()

# Do anything necessary to set up your automaton's states, q1, q2, and q3.

You will have to design your state objects, and how your Automaton handles transitions. Also make sure you set up the three states, q1, q2, and q3, for the myAutomaton instance. The test fixtures will be calling against myAutomaton.

As an aside, the automaton accepts an array of strings, rather than just numbers, or a number represented as a string, because the language an automaton can accept isn't confined to just numbers. An automaton should be able to accept any 'symbol.'

Here are some resources on DFAs (the automaton this Kata asks you to create.)

http://www.cs.odu.edu/~toida/nerzic/390teched/regular/fa/dfa-definitions.html
http://en.wikipedia.org/wiki/Deterministic_finite_automaton
http://www.cse.chalmers.se/~coquand/AUTOMATA/o2.pdf 

URL: https://www.codewars.com/kata/design-a-simple-automaton-finite-state-machine

"""

q1 = 1
q2 = 2
q3 = 3

class Automaton(object):

    def __init__(self):
        self.state = q1

    def read_commands(self, commands):
        # Return True if we end in our accept state, False otherwise
        print commands
        self.state = q1
        for c in commands:
            if self.state == q1:
                if c == '1':
                    self.state = q2
            elif self.state == q2:
                if c == '0':
                    self.state = q3
            elif self.state == q3:
                self.state = q2
        if self.state == q2: return True
        else: return False


my_automaton = Automaton()
