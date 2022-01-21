import math
# Python has also a built-in module called math, which extends the list of mathematical functions
# The min() and max() functions can be used to find the lowest or highest value in an iterable

x=min(5,10,15,20,25)
y=max(25,30,35,40,45)

print("Minimum value is :",x)
print("Maximum value is :",y)

# The abs() function returns the absolute (positive) value of the specified number

z=abs(-7.25)
print("Absolute Value : ",z)

#pow function
a=pow(4,3)
print("4^3 = ",a)

#sqrt->returns the square root of a number
b=math.sqrt(16)
print("Square root of 16 = ",b)

#ceil->rounds a number upwards to its nearest integer
#floor->rounds a number downwards to its nearest integer

c=math.ceil(1.4)
d=math.floor(1.4)

print("Ceil value : ",c)#returns 2
print("Floor value : ",d)#returns 1

