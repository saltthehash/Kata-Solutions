=begin

Kata: Enumerable Magic #28 - The Least and the Greatest, part 2

Description:

Create a method minmax_by that accepts a list and a block. The method should return an array containing the min and max list elements, based on their return values from the block

Here's a simple example:

minmax([3,2,5,4]){|item| item}  #=> [2,5] 
minmax([2,14,7,9]){|item| item.to_s}  #=> [14,9]

If you need help, here's a reference:

http://www.rubycuts.com/enum-minmax-by


URL: https://www.codewars.com/kata/545b127c85166a9fe2001431
	
=end

def minmax_by list, &block
  new_list = list.map(&block)
  new_list.sort!
  new_list.map! { |item|
    unless item == nil
      item.to_i
    end
  }
  return [new_list.first, new_list.last]
end