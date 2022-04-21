# tuple

# it is ordered
# it is unmutable
# allow duplicate




# making the tuple

tp = (78, 95, 12, 45, 36, 99)
print(tp)

# making a tuple with one item
# its trick

tp2 = (16)
print(type(tp2))

tp3 = (16,)
print(type(tp))


#---------------------------------------------
print("\n")
#---------------------------------------------


# accessing tuple
# same as list


print(tp[2])

print("\n")

print(tp[-2])

print("\n")

print(tp[2:4])


#---------------------------------------------
print("\n")
#---------------------------------------------


# joining tuple

tp5 = tp + tp3
print(tp5)


#---------------------------------------------
print("\n")
#---------------------------------------------


#multiply a tuple
tp6 = tp5*3
print(tp5*3)


#---------------------------------------------
print("\n")
#---------------------------------------------

print(tp6.count(16)) # give total count of the given element in tuple

print(tp6.index(12)) # gives the index of first appearence