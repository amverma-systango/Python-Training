#32) Inheritance

# single level inheritance
class A:

    def __init__(self):
        print("hi i am A")

class B(A):

    def __init__(self):
        super(). __init__() # i am calling the parent class constructor 
        print("hello i am B")



#objA = A()
#objB = B()




# ------------------------------------------------------

# multi level inheritance
class C:

    def __init__(self):
        print("hi i am C")

class D(C):

    def __init__(self):
        super(). __init__() # i am calling the parent class constructor 
        print("hello i am D")

class E(D):

    def __init__(self):
        super(). __init__() # i am calling the parent class constructor 
        print("aloha amigo ame class E")
    


# objE = E()


# ------------------------------------------------------

# multiple inheritance
class F:

    def __init__(self):
        print("call me F")

class G():
    def __init__(self):
        print("its me G")

class H(F,G):

    def __init__(self):
        # F.super(). __init__() # i am calling the parent class constructor 
        # G.super(). __init__() 
        print("hey i am H")
    
# objH = H()


# ------------------------------------------------------

# herirchical inheritance
class I:

    def __init__(self):
        
        print("call me I")

class J(I):
    def __init__(self):
        super(). __init__()
        print("its me J")

class K(I):

    def __init__(self):
        super(). __init__()
        print("hey i am K")

objJ = J()    
objK = K()