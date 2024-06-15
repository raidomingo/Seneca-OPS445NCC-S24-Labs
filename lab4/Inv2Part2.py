text = 'Seneca'
letter = text[1]
print(letter)

'''
'text' is a string object which contains a sequence of characters. You can access any characters 
from a string object one at a time with the bracket operator '[1]'. The number (or expression) in the square 
brackets is called an index and it must be an integer. Note that the first letter in an string object 
has an index of 0. The use of index in Python is usually consider as an offset from the beginning of the string; 
and the offset of the first character is zero.
'''

text = 'Seneca'
offset = 0
length = len(text)
while offset < length:
    print(offset, text[offset])
    offset = offset + 1


text = "Seneca"
for letter in text:
    print(letter)

def find(text,char):
    for letter in text:
        if letter == char:
             return True
    return False

if __name__ == '__main__':
    s1 = 'Seneca'
    print(s1,'contains letter s? ->',find(s1,'s'))
    print(s1,'contains letter S? ->',find(s1,'S'))

def is_vowel(char):
    if char in 'aeiou':
        return True
    return False
      
if __name__ == '__main__':
    text = 'Seneca'
    vowel_count = 0
    for char in text:
        if is_vowel(char):
             vowel_count = vowel_count + 1
    print('There are',vowel_count,'vowel(s) in',text)


import lab4e

print(lab4e.is_digits('65'))
# will output True
print(lab4e.is_digits('1F'))
# will print False
print(lab4e.is_digits('-12'))
# will print False

