# Variable= a container for a value. Behaves as the value that it contains

#Variable names
#1. Camel case->Each word, except the first, starts with a capital letter(myVariableName = "John")
#2.Pascal case->Each word starts with a capital letter(MyVariableName = "John")
#3.Snake Case->Each word is separated by an underscore character(my_variable_name = "John")

#variable name --->

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)


name ='Rayied'
name1="Alif"

print("Hello"+name)
#printing the datatype of the variable name
print("Datatype of the variable:")
print(type(name))
print("Hello"+name1)
#printing the datatype of the variable name1
print("Datatype of the variable:")
print(type(name1))

fname ="MD.SHAHZAD"
mname="HUSSAIN"
lname="RAYIED"
fullname=fname+" "+mname+" "+lname

print("Full Name:"+fullname)

x=str(10)# x will be '3'
y=int(3)#y will be 3
z=float(3)#z will be 3.0

print(x)
print(y)
print(z)

#multiple variables assigning one
n1="Rayied"
n2="Alif"
n3="Asif"
#print("Names : {} {} {}",format(n1,n2,n3))
print("Names : {} {} {}".format(n1,n2,n3))


#assigning many values into multiple variables
a,b,c="Orange", "Banana", "Cherry";
print("Fruits : {} {} {}".format(a,b,c))

a1=b1=c1="code"
print(a1)
print(b1)
print(c1)

#assigning many values into multiple variables(using list)
list=["Orange", "Banana", "Cherry"]
a,b,c=list
print("Fruit list : {} {} {}".format(a,b,c))

#unpack collection->If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking
fruits = ["apple", "banana", "cherry"]
x1, y1, z1 = fruits
print(x1)
print(y1)
print(z1)





