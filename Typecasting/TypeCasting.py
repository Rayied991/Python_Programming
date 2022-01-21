#typecasting->convert the datatype of the value to another datatype

x=1 #int
y=2.7 #float
z="3" #string

# converting y and z to int and x=float
x=float(x)
y=int(y)
z=int(z)
print("After typecasted x : ",x)
print("After typecasted y : ",(y+3))
print("After typecasted Z*3 : ",(z*3))

# print("X is = "+x)#error
print("X is : "+str(x))
print("Y is : "+str(y))
print("Z is : "+str(z))
