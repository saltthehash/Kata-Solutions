"""
Kata: HTML Generator (7 kyu)

Description:

Another rewarding day in the fast-paced world of WebDev. Man, you love your job! But as with any job, somtimes things can get a little tedious. Part of the website you're working on has a very repetitive structure, and writing all the HTML by hand is a bore. Time to automate! You want to write some functions that will generate the HTML for you.

To organize your code, make of all your functions methods of a class called HTMLGen. Tag functions should be named after the tag of the element they create. Each function will take one argument, a string, which is the inner HTML of the element to be created. The functions will return the string for the appropriate HTML element.

For example,

In JavaScript:

var g = new HTMLGen();
var paragraph = g.p('Hello, World!');
var block = g.div(paragraph);

// The following are now true
paragraph === '<p>Hello, World!</p>'
block === '<div><p>Hello, World!</p></div>'

In Python:

g = HTMLGen();
paragraph = g.p('Hello, World!')
block = g.div(paragraph)

# The following are now true
paragraph == '<p>Hello, World!</p>'
block == '<div><p>Hello, World!</p></div>'

Your HTMLGen class should have methods to create the following elements:

    a
    b
    p
    body
    div
    span
    title
    comment

Note: The comment method should wrap its argument with an HTML comment. It is the only method whose name does not match an HTML tag. So, g.comment('i am a comment') must produce <!--i am a comment-->.


URL: https://www.codewars.com/kata/html-generator
"""

class HTMLGen:
    def a(self, text):
        return '<a>'+text+'</a>'
    def b(self, text):
        return '<b>'+text+'</b>'
    def p(self, text):
        return '<p>'+text+'</p>'
    def body(self,text):
        return '<body>'+text+'</body>'
    def div(self,text):
        return '<div>'+text+'</div>'
    def span(self,text):
        return '<span>'+text+'</span>'
    def title(self,text):
        return '<title>'+text+'</title>'
    def comment(self,text):
        return '<!--'+text+'-->'