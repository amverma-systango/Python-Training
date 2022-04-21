# try will run the code in it and generate exception if the
# exception occure
# and hand over working to the except block


# here the code will generate exception
try:
    print("lets check if an error is there")
    a = 1/0
except: # this block will run if the exception occure
    print("oops the error accure")
else:   # this block will run if the exception dont occure in try block
    print("Nothing went wrong")
finally:    # this block will run regardless if the error accure or not
    print("i will run regard less")



# this will not generate any exception

try:
    print("lets check if an error is there")
except: # this block will run if the exception occure
    print("oops the error accure")
else:   # this block will run if the exception dont occure in try block
    print("Nothing went wrong")
finally:    # this block will run regardless if the error accure or not
    print("i will run regard less")