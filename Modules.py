# MODULES
#Calling another python file to working file and importing the functions from the previous file instead of defining the functions again in the new file.
#This is called Module

# Importing the modules

from Functions import greet, arithmetic, Sum, sq, cu, sum_func
#from Functions import*     # to import every function from the file

greet('Ainadri')

print("Sum function in Modules are: ")
print(Sum(6,7))

print("Arithmetic function in Modules are: ")
print(arithmetic(6,7))

lst = [45,74,56,4,7,2]
print("Using sq function: ", sq(lst))
print("Using cu function: ", cu(lst))
print("Using sum_func function: ", sum_func(lst))
