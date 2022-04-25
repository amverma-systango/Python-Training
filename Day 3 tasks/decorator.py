# decorator

'''

'''



# this is a usual closure function


def parent_function(msg):

    def child_function():
        print(msg)

    return child_function


say_jai_shree_ram = parent_function("Jai Shree Ram")


say_jai_shree_ram()




#-----------------------------------------
print("\n")
#-----------------------------------------



# how decorator function works


def parent_function(someFunction):

    def child_function():
        print("before, today and always be")
        return someFunction()

    print("Jai sanatan")
    
    return child_function 

  
def someOtherFunction():
    print("Ram is the King of World")


# this is the original way writing the decorator
y = parent_function(someOtherFunction)
y()


#-----------------------------------------
print("\n")
#-----------------------------------------



# this is another way of writing the decorator
# and an easy one

@parent_function
def someOtherFunction2():
    print("Ram is the King of World as i always say")


someOtherFunction2()



