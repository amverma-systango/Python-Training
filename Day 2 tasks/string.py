#22) Python String


# making
s1 = "hi, i made this string"


# multi line string 
# s2 = "this is the strin 
# i made it multi line 
# string"



print(s1)
# print(s2)

#---------------------------------------------
print("\n")
#---------------------------------------------

# slicing the string

# slice from  index 1 to index 5
print(s1[1:5])

# slice from index 0 to the complete length-1
print(s1[:])

# slice from index 6 to the complete length-1
print(s1[6:])

# slice from index 0 to 9
print(s1[:9])

#---------------------------------------------
print("\n")
#---------------------------------------------


# modifying the string

s3 = s1.upper()
print(s3)

print(s3.lower())

s4 = "          string have much left space         "
print(s4)
print(s4.strip())
print(s4.replace("e","E"))

#---------------------------------------------
print("\n")
#---------------------------------------------

# concatenate strings
s7 = s3+s4
print(s7)


#---------------------------------------------
print("\n")
#---------------------------------------------

print("this is a {} string and {} can see it".format("formated","you"))

print("this is a {1} string and {0} can see it. order changed lol".format("formated","you"))

#---------------------------------------------
print("\n")
#---------------------------------------------

