# Strings in python are surrounded by either single quotation marks, or double quotation marks.
#assigning string to a variable
name ="Rayied"
print("Hello ",name)

#Multiline Strings
# You can assign a multiline string to a variable by using three quotes(double or single)

a="""This is multiline Strings"""
print(a)

#Strings are arrays
'''Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.'''

str="Hello World"
print(str[1])#e

#looping through string
for x in "banana":
  print(x)
