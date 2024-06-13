'''
dictionary is a set of key-value pairs. Dictionaries are unordered, like sets, 
however any value can be retrieved from a dictionary if you know the key.
'''

dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
print(dict_york.values())
print(dict_york.keys())

# We can retrieve individual values from a dictionary by providing the key associated with the value
print(dict_york['Address'])
print(dict_york['Postal Code'])

'''
Dictionary keys can be any immutable values (i.e. not permitted for value to be changed). Types of 
values include: strings, numbers, and tuples.
'''

dict_york['Country'] = 'Canada'
print(dict_york)
print(dict_york.values())
print(dict_york.keys())

dict_york['Province'] = 'BC'
print(dict_york)
print(dict_york.values())
print(dict_york.keys())

'''
WARNING: Dictionary keys must be unique. Attempting to add a key that already 
exists in the dictionary will overwrite the existing value for that key!
'''

dict_york['Province'] = 'ON'
print(dict_york)
print(dict_york.values())
print(dict_york.keys())

list_of_keys = list(dict_york.keys())
print(list_of_keys[0])
print(list_of_keys[0:2])

list_of_keys = list(dict_york.keys())
for key in list_of_keys:
    print(key)
for value in dict_york.values():
    print(value)