# 15) Anonymous Function

num = int(input("enter a number- "))
x = lambda num: "even" if num%2==2 else "odd"

print("this will print even or odd, and the number is- ", x)
