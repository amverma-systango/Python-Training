#24) Python Dictionary

# key value pair
# no duplicate key allowed



# creation

d1 = {
  "k1": "v1",
  "k2": 2.5,
  "k3": 3
}

print(d1)


#---------------------------------------------
print("\n")
#---------------------------------------------



## Accessing

# like indexing
print(d1["k2"])


# using get Function
print(d1.get("k3"))


# getting all the keys in dictionary 
print(d1.keys())


# getting all the values in dictionary
print(d1.values())

# getting all items(key:value) pairs
print(d1.items())

#---------------------------------------------
print("\n")
#---------------------------------------------

## adding 

d1["k4"] = 2020
print(d1)

# using update
d1.update({"k5": 9875641564.68645684})
print(d1)

#---------------------------------------------
print("\n")
#---------------------------------------------

## deleting
print(d1)
d1.popitem()
print(d1)

del d1["k2"]
print(d1)