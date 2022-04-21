#20) Python List


# its a python list
var_1 = [1, 2, 2, "three", 4, "five", "bla bla"]

# list are like array but it can contain element of different type





## accessing elements

# the way of accessing the element is same as array
print(var_1[4])
 
# python list also support negative indexing
print(var_1[-3])





## slicing

# python list is sliced this way
print(var_1[1:4]) # slice from index 1 to 4(excluded)

print(var_1[:3]) # slice from index 0 to 3(excluded)

print(var_1[:]) # basically entire list

print(var_1[3:]) # slice from index 3 to the end of the list

print(var_1[::2]) # slice on jump of 2






## changing the items

print(var_1[0])
var_1[0] = "one"
print(var_1[0])


print(var_1[0:2])
var_1[0:2] = ["i am 1", "i am 2"]
print(var_1)


print(var_1[0:2])
var_1[0:2] = ["again changed"]
print(var_1)







## inserting item

var_1.insert(0, "hi")
print(var_1)

print("")

# it will inset the element at last
var_1.append("i am last")
print(var_1)

print("")

# extend will insert all the element of other iterable to the list
var_2 = ["we", "are", "now", "in", "family", "too"]
var_1.extend(var_2)
print(var_1)

print("")


var_3 = ("well", "few", "more")
var_1.extend(var_3)
print(var_1)

print("")

var_1.extend(["dont", "forget", "us"])
print(var_1)







## removing the items

print("")

# using the pop will delete last index element
x = var_1.pop()
print(x, "gone")
print(var_1)

print("")

# using pop and specifying the index 
x = var_1.pop(5)
print(x, "gone")
print(var_1)

print("")

# removing element using remove function and specifing the index
var_1.remove(2)
print(x)
print(var_1)

print("")

# deleting the element in list using the del
print(var_1)
del var_1[-1]
print(var_1)


print("")

# emptying the entire list
print(var_1)
var_1.clear()
print(var_1)










