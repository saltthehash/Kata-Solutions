=begin

Kata: Enumerable Magic #22 - First Elements of an Array

Description:

Create a method first that accepts a list and an optional parameter n. If n is unspecified, it returns just the first element of the list. If n is specified, it returns that number of elements from the beginning of the list.

If you need help, here's a reference:

http://www.rubycuts.com/enum-first


URL: https://www.codewars.com/kata/enumerable-magic-number-22-first-elements-of-an-array

=end

def first list, n=nil
  if n == nil  
    return list[0]
  else  
    return list[0...n]
  end
end