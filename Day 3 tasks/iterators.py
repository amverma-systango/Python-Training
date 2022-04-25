# 1) Python Iterator

## Iterable

"""
    if a data type/object in python is having a __iter__ dunder method 
    then it is an iterable.

    or if the object/data type can be looped over its a iterable
"""

a = 20
b = 30.36
c = "this is a string"
l1 = [78,55,99]
s1 = {1,2,3}
t1 = (1,2,3)
d1 = { "1":"one", "2":"two", "3":"three" }


print("__iter__" in dir(a) if "__iter__ method present" else "__iter__ method not present")
print("")
print("__iter__" in dir(b) if "__iter__ method present" else "__iter__ method not present")
print("")
print("__iter__" in dir(c) if "__iter__ method present" else "__iter__ method not present")
print("")
print("__iter__" in dir(l1) if "__iter__ method present" else "__iter__ method not present")
print("")
print("__iter__" in dir(s1) if "__iter__ method present" else "__iter__ method not present")
print("")
print("__iter__" in dir(t1) if "__iter__ method present" else "__iter__ method not present")
print("")
print("__iter__" in dir(d1) if "__iter__ method present" else "__iter__ method not present")



"""
    so i made it confirmed
"""



## iterator 

"""
    iterator is an object which can return a data one at a time while iterating over it
""" 



## making a iterator 

# someIterator = l1.__iter__()

# print(someIterator.__next__())
# print(someIterator.__next__())
# print(someIterator.__next__())
# print(someIterator.__next__()) # this giving eror


someIterator = iter(s1)

print(next())
print(next())
print(next())