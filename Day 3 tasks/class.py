
# the basic class
class myClass:

    """
    this is a basic class
    """



m1 = myClass()
print(m1.__doc__)
print(m1.__dir__())



# ----------------------------------------
print("\n")
# ----------------------------------------

#class with constructor

class myClassWithConstructor:

    """
    this is the class with constructor
    """
    
    def __init__(self):
        print("hello i ran when the class's instance is being initialised")


m2 = myClassWithConstructor()
print(m2.__doc__)
print(m2.__dir__())



# ----------------------------------------
print("\n")
# ----------------------------------------

#class having the instance variable

class myClassWithInstanceVariable:

    """
    this is the class with constructor and instance variable
    """
    
    def __init__(self, msg):
        self.message = msg
        print(self.message)


m3 = myClassWithInstanceVariable("a new message is here")
print(m3.__doc__)
print(m3.__dir__())


# ----------------------------------------
print("\n")
# ----------------------------------------


class myClassWithClassVariable:

    """
    this is my class with class variable

    class variable are shared amoung all the
    instances of the class

    any changes in the class variable is shared in
    all the instances
    """

    iAmShared = 8



m4 = myClassWithClassVariable()
m5 = myClassWithClassVariable()

print(m4.iAmShared, m5.iAmShared)
myClassWithClassVariable.iAmShared = 50
print(m4.iAmShared, m5.iAmShared)


# ----------------------------------------
print("\n")
# ----------------------------------------



class MyClassWithMemberMethod:

    def sayHello(self):
        print("hello everyone")




m6 = MyClassWithMemberMethod()
m6.sayHello()
print(m2.__doc__)
print(m2.__dir__())



# ----------------------------------------
print("\n")
# ----------------------------------------












        
