#length method
# To get the length of a string, use the len() function.
name="Rayied "
print("The length of the string : ",len(name))
print(name.find("d"))#returns index of the character

#starts with->Returns true if the string starts with the specified value
print("Starts with R :",name.startswith("R"))#returns true
#capitalize string
n1="rayied"
print("Capitalize : "+n1.capitalize())

#upper method-> makes the whole string upper case
print("Upper case  : ",n1.upper())

#lower method-> makes the whole string lower case
print("Lower case  :",name.lower())

#islower()->eturns True if all characters in the string are lower case
print("Is lower case :",name.lower().islower())

#isupper->Returns True if all characters in the string are upper case
print("Is upper case : ",name.upper().isupper())

#isdigit -> returns true or false
dg="121"
print("Is digit : ",dg.isdigit())#returns true
dg1="Hello"
print("Is digit : ",dg1.isdigit())#returns false

#isalpha -> check string contains only alphabetical letters
print("Is alpha : ",name.isalpha())#returns true
al="Hello@"
print("Is alpha : ",al.isalpha())#returns false

#count-> count how many characters in the string
print("Count : ",name.count("a"))#returns 1

#replace -> replace character with string
print("Replacement : ",name.replace("a","o"))#returns Rayied

#show string multiple times by multiplying the string
print("Three times : ",(name*3))

#strip()->remove whitespaces from beginning or the end of the string
a="Hello, World! "
print(a.strip())#returns Hello,World

#split()->The split() method returns a list where the text between the specified separator becomes the list items.
print(a.strip().split(","))# returns ['Hello', ' World!']
#Check strng-> To check if a certain phrase or character is present in a string, we can use the keyword in.
#way-1
txt="Hello Python"
print("Python" in txt)#returns true

#way-2
if "Python" in txt:
    print("Yes, 'Python' is present")

#Check if not->To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")