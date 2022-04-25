'''
A closure—unlike a plain function—allows
the function to access those captured variables
through the closure’s copies of their values or references,
even when the function is invoked outside their scope.
'''


def parentFunction( s ):

    def childFunction():
        print(s)

    return childFunction        

x = parentFunction("its me Aman oh wait call me CyberCommando")
x()




def nth_power(expo):

    def power_of(base):
        return pow(base, expo)

    return power_of

cube = nth_power(3)
print(cube(4))
