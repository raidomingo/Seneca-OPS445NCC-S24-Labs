s1 = {'Prime', 'Ix', 'Secundus', 'Caladan'}
s2 = {1, 2, 3, 4, 5}
s3 = {4, 5, 6, 7, 8}

# This will fail becuause sets has no order
# print(s1[0])

print('Ix' in s1)
print('Geidi' in s1)

'''
Sets can be combined, but it is important to note that any 
duplicate values (shared among sets) will be deleted.
'''

print(s2)
print(s3)

# This is how you get a set containing only UNIQUE values (no duplicates) from both sets
print(s2 | s3)         # returns a set containing all values from both sets
print(s2.union(s3))    # same as s2 | s3

'''
Instead of combining sets, we can display values that are common to both sets. This is 
known in mathematical terms as an intersection between the lists
'''

print(s2 & s3)             # returns a set containing all values that s2 and s3 share
print(s2.intersection(s3)) # same as s2 & s3

'''
Sets can also have their values compared against other sets. First find out what items 
are in s2 but not in s3. This is also called a difference:
'''

print(s2)
print(s3)
print(s2 - s3)             # returns a set containing all values in s2 that are not found in s3
print(s2.difference(s3))   # same as s2 - s3

'''
In order to see every difference between both sets, you need to find the symmetric difference. 
This will return a set that shows all numbers that both sets do not share together:
'''

print(s2 ^ s3)                     # returns a set containing all values that both sets DO NOT share
print(s2.symmetric_difference(s3)) # same as s2 ^ s3

'''
the set() function can convert lists into sets, and the list() function can convert sets into lists. 
The operations in this section can only be applied to sets, so if you need to perform a union, intersection, 
or difference between lists, you need to convert them to sets first.
'''

l2 = [1, 2, 3, 4, 5]
l3 = [4, 5, 6, 7, 8]
temporary_set = set(l2).intersection(set(l3))
new_list = list(temporary_set)  # '''set()''' can make lists into sets. '''list()''' can make sets into lists.
print(new_list)

import lab4a
set1 = {1,2,3,4,5}
set2 = {2,1,0,-1,-2}
print(lab4a.join_sets(set1,set2))
# Will output {-2, -1, 0, 1, 2, 3, 4, 5}
print(lab4a.match_sets(set1,set2))
# Will output {1, 2}
print(lab4a.diff_sets(set1,set2))
# Will output {-2, -1, 0, 3, 4, 5}

import lab4b
list1 = [1,2,3,4,5]
list2 = [2,1,0,-1,-2]
print(lab4b.join_lists(list1,list2))
# Will output [0, 1, 2, 3, 4, 5, -2, -1]
print(lab4b.match_lists(list1,list2))                                                                                                                 
# Will output [1, 2]
print(lab4b.diff_lists(list1,list2))                                                                                                                  
# Will output [0, 3, 4, 5, -2, -1]