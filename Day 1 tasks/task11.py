# 11. break and continue


# normal loop
print("normal loop")
i = 0 

while i<10:
	print("i = ",i)
	i+=1


# loop with break
print("loop with break")
i = 0 

while i<10:
	if(i==5):
		break
	print("i = ",i)
	i+=1


# loop with continue
print("loop with continue")
i = 0 

while i<10:
	if(i==5):
		i+=1
		continue

	print("i = ",i)
	i+=1