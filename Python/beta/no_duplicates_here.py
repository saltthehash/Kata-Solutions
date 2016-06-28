"""
Kata: No Duplicates Here

Description:

Return the array/list passed into the function with all duplicates removed.

The items in the returned array should be sorted alphabetically, with numbers before strings.

The function should remove any null, undefined and invalid values from the array (in JS: all falsey values (NaN, false, undefined, null etc.) have to be removed). If the variable is not an array/list, the function should return a string “Not an array”.

URL: https://www.codewars.com/kata/no-duplicates-here

"""

def list_de_dup(list_):
    # Check if the list is a list
    if type(list_) is not list:
        return "Not an array"
    # Remove None values without removing 0 or False
    f_list = [item for item in list_ if item is not None]
    # Sort the list to have duplicates next to each other in the list
    f_list.sort()
    # Create a list of indices of duplicate entries
    rm_inds = []
    for i in xrange(len(f_list)):
        if i < len(f_list)-1 and f_list[i] == f_list[i+1]:
            rm_inds.append(i)
    # Reverse sort the indices to remove them without changing the indices of items below the popped item
    rm_inds.sort(reverse=True)
    for ind in rm_inds:
        f_list.pop(ind)
    return f_list