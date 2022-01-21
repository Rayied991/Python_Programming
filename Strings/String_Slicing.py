# Slicing= create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]-> step optional(how much increasing index by between start and stop)

#slice index
name="MD. SHAHZAD HUSSAIN RAYIED"

fname=name[0:11]#start index is inclusive , stopping index is exclusive
# (no error)fname=name[:11]#start index is inclusive , stopping index is exclusive

lname=name[12:27]
# lname=name[12:](no error)
print(fname)
print(lname)

funky_name=name[0:27:1]
funky_name1=name[0:27:2]
print(funky_name)
print(funky_name1)

reversed_name=name[::-1]
print("Reversed Name :",reversed_name)

#slice function

#negative indexing
website="http://google.com"
website1="http://wikipedia.com"
slice=slice(7,-4)
print(website[slice])#returns website name
print(website1[slice])#returns website name