# 8) Python if...else


var_1 = int(input("Enter a number"))

# if statement
if var_1 < 0 :
	print("number is negative")

	# nested if
	if var_1%2 == 0:
		print("number is even")
	else:
		print("number is odd")

elif var_1 > 0:
	print("number is positive")

	# nested if
	if var_1%2 == 0:
		print("number is even")
	else:
		print("number is odd")

else:
	print("number is zero")

	# nested if
	if var_1%2 == 0:
		print("number is even")
	else:
		print("number is odd")