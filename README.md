# DataEngineering204
A place to store my study notes and projects
Python Introducion notes
# this is a comment in python
***
This is also a comment
*** 
Data types
Numbers
- integers (whole numbers)
- floating point (decimals)
Strings
- anything involving characters or text
Boolean
- True or False

Print(type(x)) will print the data type

Maths operators
- + * / % 

Strings
- each character is represented by a unicode
- you can use “double” or ‘single’ quotes
- each char also has an index, starting from 0: print(‘x’[n]) will retrieve whatever char is in the stated index. -1 index starts from the end of the string.
- print(len(x)) returns the total amount of characters in the string 

Boolean
- Booleans values are capitalised
- they are generated from equality operators (==, !=, >, <, >=, <=)
- 0 = False, anything other than 0 = True
- string = True, empty string (“”) = False
- print(2 < “2”) wont work as you cant compare an integer to a string/Unicode.
- print(2 < len(2)) this will work as the len() function produces an integer from counting the unicode characters.

Variables
- a reserved memory location that allows us to store data and objects
- variable name = data
Variable rules
- the name cannot start with a literal/core data type (numbers, strings, bools)
- use_snake_casing
- they are mutable, we can change them

Concatentation
first_name = “Kat”
last_name = “McNeill”
full_name = first_name + ‘ ‘ + last_name
¬¬- a space needs to be added in with ‘’
- to an integer value into a string, you must type cast:
age = 25
print(‘you are ’ + str(age) + ‘ years old’)
- if you need to use quotation marks in a string, you use the escape backslash character infront of the character you want to be ignored by the IDE
Text = “someone said that, \”text can be tricky\””

String Methods
- string method are used after a string variable.likethis()
.capitalize() Capitalizes the sentences 
.upper() MAKES EVERYTHING CAPS. 
.lower() makes everything lowercase. 

Returns bools
.isupper()
.islower()
.isnumeric()
.isalpha() are all characters in the alpabet?
.count(‘x’) how many times is the character present
.find(‘x’) character index
.startswith(‘x’) good for filtering items in a string, finds strings starting with x
.endswith(“x”)
.replace(‘part to replace’, ‘what to replace it with’)
.split() splits a string into separate words

Control flow

