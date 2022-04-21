#31) Python Class

class MyClass:

    '''
    A Python class variable is shared by all object instances of a class.
    Class variables are declared when a class is being constructed. 
    '''
    school = "some school on mars"

    # the constructor
    def __init__(self, name):
        '''
        instance member variable are individual of each member
        '''
        self.name = name

    def someFunction(self):
        print("i made a funciton in the class")

    

obj1 = MyClass("Aman")
print(obj1.name)
print(obj1.school)




# deleting the object

del obj1