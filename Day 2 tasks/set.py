#23) Python Set

# unordered
# unchangable
# duplicate not allowed if inserted duplicates are removed automatically





##creating
s1 = {85, 96, 31 ,74 ,12, 58, 436}
print(s1)


#----------------------------------------------
print("\n")
#---------------------------------------------


## Accessing element

# cannot access data with index in set because its unordered

for x in s1:
    print(x)


#----------------------------------------------
print("\n")
#---------------------------------------------


## adding a element in the set

s1.add("lets add something new")
print(s1)


## adding the iterable
s1.update(["this", "is", "the", "list", "added", "but", "any", "iterable", "would", "work"])
print(s1)


#----------------------------------------------
print("\n")
#---------------------------------------------

## removing item

# with remove
s1.remove("the")
print(s1)

# with pop()
x = s1.pop()
print(x)

# with clear
s1.clear()
print(s1)


#----------------------------------------------
print("\n")
#---------------------------------------------

