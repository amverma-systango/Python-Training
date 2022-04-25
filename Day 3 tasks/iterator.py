
myIterable = [78 , 96, 34, 7, 52, 64]

myIter = iter(myIterable)

# i can use next method, to fetch one value
print(next(myIter))

# or i can use the next dunder method to fetch the value either way the result is same
print(myIter.__next__())
print(myIter.__next__())
print(next(myIter))





# ----------------------------------------
print("\n")
# ----------------------------------------


# making the iterator other way
# usinig __iter__() dunder method

myIterable2 = [78 , 96, 34, 7, 52, 64]

myIter2 = myIterable2.__iter__()

print(myIter2.__next__())
print(next(myIter2))









        
