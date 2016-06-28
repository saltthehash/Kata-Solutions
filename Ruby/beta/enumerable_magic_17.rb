=begin

Kata: Enumerable Magic #17 - Sort that List by Value!

Description:

Create a method sort_by that accepts a list and a block, and returns a new list sorted by the return values of the block.

If you need help, here's a reference:

http://www.rubycuts.com/enum-sort-by

URL: https://www.codewars.com/kata/545ac6fe85166a42c8000f37

=end

def sort_by list, &block
 return list.sort_by(&block)
end
