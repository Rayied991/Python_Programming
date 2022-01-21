# Python 3.6 uses the input() method.
#
# Python 2.7 uses the raw_input() method.
# to take input

#input method

username=input("Enter a Username? :")
# age=input("How old are you? :")
# age=age+1//cannot perform math

age = int(input("How old are you? :"))#typecasted
age=age+1

height=float(input("How tall are you? :"))
print("Hello ",username)
# print("I am "+age+" Years old")#error
print("I am "+str(age)+" Years old")
print("I am ",age," Years old")
print("I am ",height," cm tall")