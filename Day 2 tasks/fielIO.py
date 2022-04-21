# file I/O

## opne

# f = open("fileOperationExperiment.txt","r")
f = open("fileOperationExperiment.txt","r+")



# reading from file
# print(f.read())

# readin certain number of character
# print(f.read(15))

# reading a line
print(f.readline())

# closing the line
f.close()



## creating and writing in the file

# f2 = open("IOExperimentfile2.txt", "w")
# f2 = open("IOExperimentfile2.txt", "w+")
f2 = open("IOExperimentfile2.txt", "a")

f2.write("see if the file is created or not part 3")

f2.close()