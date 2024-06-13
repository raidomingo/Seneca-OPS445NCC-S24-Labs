course_name = 'Open System Automation'
course_code = 'OPS445'
course_number = 445

print(course_name)
print(course_code)
print(str(course_number))
print(course_name + ' ' + course_code + ' ' + str(course_number))

'''
the print() function, you can display special characters. One such 
special character is the is the newline character (denoted by the symbol: \n).
'''
print('Line 1\nLine 2\nLine 3\n')

# Strings have many built-in functions that we can use to manipulate text.
print(course_name.lower())         # Returns a string in lower-case letters
print(course_name.upper())         # Returns a string in upper-case letters
print(course_name.swapcase())      # Returns a string with upper-case and lower-case letters swapped
print(course_name.title())         # Returns a string with upper-case first letter of each word, lowercase for remaining text
print(course_name.capitalize())    # Returns a string with upper-case first letter only, lowercase for remaining text

lower_name = course_name.lower()    # Save returned string lower-case string inside new string variable
print(lower_name)

'''
If a string contains many values separated by a single character, such as a space, the string can be split on 
those values and create a list of values
'''
lower_name.split(' ')       # Provide the split() function with a character to split on
# The above example will return a list of strings, which we can access just like all of lists

list_of_strings = lower_name.split(' ')     # Split string on spaces and store the list in a variable
print(list_of_strings)                      # Display list
print(list_of_strings[0])                   # Display first item in list

print(list_of_strings[0].upper())           # Use the function after the index to affect a single string within a list
first_word = list_of_strings[0]
print(first_word)

''''
The index that is used to access items within a list, can also be used to access characters within a string. For practice, 
let's create a new string, and start accessing the strings index:
'''

course_name = 'Open System Automation'
course_code = 'OPS445'
course_number = 445
print(course_code[0])                          # Print the first character in course_code
print(course_code[2])                          # Print the third character in course_code
print(course_code[-1])                         # Print the last character in course_code
print(str(course_number)[0])                   # Turn the integer into a string, return first character in that string, and print it
print(course_code[0] + course_code[1] + course_code[2])

'''
ou can use a technique that uses index numbers of a string to cut-out or "parse" smaller portions of text within a string. This term
 is referred to as a substring.
'''

print(course_name[0:4])                 # Print the first four characters (values of index numbers 0,1,2, and 3) 
first_word = course_name[0:4]           # Save this substring for later use
print(course_code[0:3])                 # Print the first three characters (values of index numbers 0,1,and 2)

course_name = 'Open System Automation'
print(course_name[12:])                        # Print the substring '12' index until end of string
print(course_name[5:])                         # Print the substring '5' index until end of string
print(course_name[-1])                         # Print the last character

'''
With negative indices, -1 would represent the last character, -2 index would represent the second last character, etc.:
'''

course_name = 'Open System Automation'
print(course_name[-1])
print(course_name[-2])

course_name = 'Open System Automation'
print(course_name[-10:])                            # Return the last ten characters
print(course_name[-10:-6])                          # Try and figure out what this is returning 
print(course_name[0:4] + course_name[-10:-6])       # Combine substrings together
substring = course_name[0:4] + course_name[-10:-6]  # Save the combined substring as a new string for later
print(substring)