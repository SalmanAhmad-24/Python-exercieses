# Module
# As your program gets longer you may want to split it into several files for easier
# maintainence.You may also want to use the functions you have written in several programs
# without copying it into each program.For this purpose python has a way to put definitions
# into a file and use them in a script or interactive instance of the interpretor such a File
# is called module.


# The following function will write the fibbonaci series upto n number
def fib(n):
    a,b=0,1
    while(a<n):
        print(a,end=" ")
        a,b=b,a+b
    print()

print(fib(10))

# The following function will return the list of  fibbonaci series upto n number
def fib2(n):
    a,b=0,1
    result=[]
    while(a<n):
        result.append(a)
        a,b=b,a+b
    return result
print(fib2(10))

# Code in iterpretor:      
# Now when you open the interpretor and import the module
# >>> import Module
# output:
# 0 1 1 2 3 5 8
# None
# [0, 1, 1, 2, 3, 5, 8]
# so you get the ouput of the functions present in the Module Module 

#You can access the module functions using the module name
# >>> Module.fib(100)
# output:0 1 1 2 3 5 8 13 21 34 55 89 

# >>> Module.fib2(100)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# >>> Module.__name__
# 'Module'
# If you intend to use a function often assign it to a local variable like below 
# >>> fib=Module.fib
# >>> fib(500)

# Output: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# If you want to import some specific functions from the  module you can import them like

# >>> from Module import fib,fib2

# else if you want to import all the functions you can import them in a way like
# Note:This imports all names except those beginning with an underscore (_)
# >>>  from Module import *
# >>> fib(100)
# Output: 0 1 1 2 3 5 8 13 21 34 55 89 

# If the module name is followed by as, then the name following as is bound directly to the imported module
# >>> import Module as fib
# >>> fib.fib(100)
# Output:0 1 1 2 3 5 8 13 21 34 55 89

# This will import the module with the name fib

# The following will import the fib function in the Module module as fibonacci
# >>> from fibo import fib as fibonacci
# >>> fibonacci(500)
# Output: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 

 
