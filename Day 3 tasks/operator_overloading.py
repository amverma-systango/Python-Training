# Operator overloading

"""

 in python operator overloading can be done by
 overriding the dunder method which corresponds
 to the operator


 Addition	          __add__(p2)
 Subtraction	          __sub__(p2) 
 Multiplication	          __mul__(p2)
 Power	                  __pow__(p2)
 Division	          __truediv__(p2)
 Floor Division	          __floordiv__(p2)
 Remainder (modulo)	  __mod__(p2)
 Bitwise Left Shift	  __lshift__(p2)
 Bitwise Right Shift	  __rshift__(p2)
 Bitwise AND	          __and__(p2)
 Bitwise OR	          __or__(p2)
 Bitwise XOR	          __xor__(p2)
 Bitwise NOT	          __invert__()

 Less than	          __lt__(p2)
 Less than or equal to	  __le__(p2)
 Equal to	          __eq__(p2)
 Not equal to	          __ne__(p2)
 Greater than	          __gt__(p2)
 Greater than or equal to __ge__(p2)


"""


class MyUniqueClass:

    def __init__(self, num):
        self.num = num


    def __add__(self, other):
        result = (self.num + other.num)+100
        return result

    def __sub__(self, other):
        result = (self.num - other.num)-100
        return result

    def __mul__(self, other):
        result = (self.num * other.num)*100
        return result

    def __truediv__(self, other):
        result = (self.num / other.num)/100
        return result

    def __lt__(self, other):

        if self.num < other.num :
            return True
        else:
            return False




muc1 = MyUniqueClass(5)
muc2 = MyUniqueClass(9)


print( muc1 + muc2 )
print( muc2 - muc1 )
print( muc1 * muc2 )
print( muc2 / muc1 )

print( muc1 < muc2 )
print( muc2 < muc1 )


        
        
