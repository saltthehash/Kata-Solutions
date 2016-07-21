"""
Kata: Simpler Interactive Interpreter (2 kyu)

Description:

Simpler Interactive interpreter (or REPL)

You will create an interpreter which takes inputs described below and produces outputs, storing state in between each input. This is a simplified version of the Simple Interactive Interpreter kata with functions removed, so if you have fun with this kata, check out its big brother to add functions into the mix.

If you're not sure where to start with this kata, check out ankr's Evaluate Mathematical Expression kata.

Note that the
eval
command has been disabled.

Concepts

The interpreter will take inputs in the language described under the language header below. This section will give an overview of the language constructs.

Variables

Any identifier which is not a keyword will be treated as a variable. If the identifier is on the left hand side of an assignment operator, the result of the right hand side will be stored in the variable. If a variable occurs as part of an expression, the value held in the variable will be substituted when the expression is evaluated.

Variables are implicitly declared the first time they are assigned to.

Example: Initializing a variable to a constant value and using the variable in another expression (Each line starting with a '>' indicates a separate call to the input method of the interpreter, other lines represent output)

>x = 7
    7
>x + 6
    13
Referencing a non-existent variable will cause the interpreter to throw an error. The interpreter should be able to continue accepting input even after throwing.

Example: Referencing a non-existent variable

>y + 7
    ERROR: Invalid identifier. No variable with name 'y' was found."
Assignments

An assignment is an expression that has an identifier on left side of an = operator, and any expression on the right. Such expressions should store the value of the right hand side in the specified variable and return the result.

Example: Assigning a constant to a variable

x = 7
    7
In this kata, all tests will contain only a single assignment. You do not need to consider chained or nested assignments.

Operator Precedence

Operator precedence will follow the common order. There is a table in the Language section below that explicitly states the operators and their relative precedence.

Name conflicts

Because variables are declared implicitly, no naming conflicts are possible. variable assignment will always overwrite any existing value.

Input

Input will conform to the expression production in the grammar below.

Output

Output for a valid expression will be the result of the expression.

Output for input consisting entirely of whitespace will be an empty string (null in case of Java).

All other cases will throw an error.

Language

Grammar

This section specifies the grammar for the interpreter language in EBNF syntax

expression      ::= factor | expression operator expression
factor          ::= number | identifier | assignment | '(' expression ')'
assignment      ::= identifier '=' expression

operator        ::= '+' | '-' | '*' | '/' | '%'

identifier      ::= letter | '_' { identifier-char }
identifier-char ::= '_' | letter | digit

number          ::= { digit } [ '.' digit { digit } ]

letter          ::= 'a' | 'b' | ... | 'y' | 'z' | 'A' | 'B' | ... | 'Y' | 'Z'
digit           ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'

Operator Precedence

The following table lists the language's operators grouped in order of precedence. Operators within each group have equal precedence.

Category        Operators
Multiplicative  *, /, %
Additive        +, -
Assignment      =


URL: https://www.codewars.com/kata/simpler-interactive-interpreter
"""

import re
from numbers import Number
import operator as op

def tokenize(expression):
    if expression == "":
        return []

    regex = re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]

def is_number(d):
    p = re.compile(r"\A[-]?\d+(?:\.\d+)?\Z")
    m = p.search(d)
    return bool(m)

def is_operator(o):
    p = re.compile(r'\A[\+\-\*\/\%]\Z')
    m = p.search(o)
    return bool(m)

class Interpreter:
    def __init__(self):
        self.vars = {}
        self.functions = {}
        self.operators = {
            "+": op.add,
            "-": op.sub,
            "*": op.mul,
            "/": op.truediv,
            "%": op.mod
        }

    def input(self, expression):
        tokens = tokenize(expression)
        #print("tokens: %r" % tokens)
        
        if "=" in tokens:
            assert tokens[1] == "="
            new_var = tokens[0]
            tokens = tokens[2:]
            value = self.eval_postfix(self.shunting_yard(tokens))
            self.vars[new_var] = value
        else:
            value = self.eval_postfix(self.shunting_yard(tokens))
        return value

    def precedence(self, operator):
        if operator == '+' or operator == '-':
            return 2
        elif operator == '*' or operator == '/' or operator == '%':
            return 3
        else:
            raise Exception("%s is not a valid operator." % operator)
        
    def shunting_yard(self, expression):
        output = []
        operators = []
        last = ""
        for token in expression:
            if is_number(token):
                if last == "number":
                    raise Exception("ERROR: Invalid syntax: %r" % expression)
                    return
                last = "number"
                try:
                    output.append(int(token))
                except ValueError:
                    output.append(float(token))
            elif token in self.vars:
                if last == "number":
                    raise Exception("ERROR: Invalid syntax: %r" % expression)
                    return
                last = "number"              
                output.append(self.vars[token])
            elif token in self.operators:
                last = "operator"
                if operators and is_operator(operators[-1]):
                    o1 = self.precedence(token)
                    o2 = self.precedence(operators[-1])
                    while operators and operators[-1] in self.operators and o2 >= o1:
                        o2 = self.precedence(operators[-1])
                        output.append(self.operators[operators.pop()])
                operators.append(token)
            elif token == "(":
                last = "left_paren"
                operators.append(token)
            elif token == ")":
                last = "right_paren"
                while operators and operators[-1] != "(":
                    output.append(self.operators[operators.pop()])
                try:
                    par = operators.pop()
                except IndexError:
                    raise Exception("ERROR: Mismatched parentheses!")
                    return
            else:
                raise Exception("ERROR: Invalid token: %r" % token)
                return
        while operators:
            output.append(self.operators[operators.pop()])
        return output

    def eval_postfix(self, expression):
        if expression is None:
            return ""
        output = []
        for token in expression:
            if isinstance(token, Number):
                output.insert(0, token)
            else:
                right = output.pop(0)
                left = output.pop(0)
                result = token(left, right)
                output.insert(0, result)
        try:
            return output[0]
        except IndexError:
            return ""