# String Format
# we cannot combine strings and numbers like this
# age = 36
# txt = "My name is Rayied, I am " + age#error
# print(txt)

# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are

age1=36
txtt="My name is Rayied, and I am {}"
print(txtt.format(age1))


# The format() method takes unlimited number of arguments, and are placed into the respective placeholders
name="Rayied"
height=35.78
txt1="I am {} and I am {} years old and Height is {}"
print(txt1.format(name,age1,height))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#Escape character
txt = "I am  \"Rayied\" from Bangladesh"
print(txt)