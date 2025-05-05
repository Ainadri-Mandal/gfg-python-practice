print("hello world")
print("i am ainadri mandal")
print(type(23423))
print(type(1.56))
print(type(True))
print(type("hello world"))

# Functionalities in print statement
print('a')
print('b')
print('c')
print('a-','b-','c')
print('--------------------------------------------------')

print('a', end= '-')
print('b', end= '-')
print('c')
print('--------------------------------------------------')

print('a','b','c', sep=',')

a = 2 + 4j
b = 3 - 5j
print("Type of a: ", type(a))
print("Type of b: ", type(b))
print('--------------------------------------------------')

String1 = 'Geeks'
print("String with the use of Single Quotes: ", String1)
String2 = "I'm a Geek"
print("String with the use of Double Quotes including single quotes: ", String2, type(String2))
String3 = '''I'm a Geek and I live in a world of "Geeks"'''
print("String with the use of Triple Quotes: ", String3, type(String3))
String4 = '''Geeks 
			For 
			Life'''
print("Creating a multiline String: ", String4)

print('--------------------------------------------------')
#list , tuples, set , dictionary

list1 = [1.0, 2,'gfg',"Geeks"]
print(list1)
print(type(list1))

tup1 = (1, 'hi', 3.0)
print(tup1)
print(type(tup1))

set1= {1,4,5,"Geeks", 6.0}
print(set1)
print(type(set1))

Dict1 = {}
print("Empty Dictionary: ", Dict1, type(Dict1))
dict2 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("Numeric key dictionary: ",dict2)
dict3 = {'Name': 'Geeks', 1: [1,2,3,4]}
print("Mixed Key Dictionary: ",dict3)
dict4 = dict({(1,'Geeks'),(2, 'For'), (3, 'Geeks')})
print("Dictionary using dict function: ",dict4)
print('--------------------------------------------------')

#OPERATORS
# 1. ARITHMETIC OPERATORS
#ADDITION
print(2+3)
print(2.5 + 3.5)
print(2.5 + 3)
print(True + True)
print("------------------")
#SUBTRACTION
print(2-3)
print(2.5 - 3.5)
print(2.5 - 3)
print(True - True)
print("------------------")
#MULTIPLICATION
print(2*3)
print(2.5 * 3.5)
print(2.5 * 3)
print(True * True)
print("------------------")
#DIVISION
print(3/2)
print(2.5 / 5.0)
print(2.5 / 1)
print(True / True)
print("------------------")
#FLOOR DIVISION
print(3//2)
print(2.5 // 5.0)
print(2.5 // 1)
print(True // True)
print("------------------")
#MODULO
print(3%2)
print(2.5 % 5.0)
print(2.5 % 1)
print(True % True)
print("------------------")
#EXPONENTIATION
print(3**2)
print(2.5 ** 5.0)
print(2.5 ** 1)
print(True ** True)
print("------------------")
#ABS
print(abs(-35))
#ROUND
print("Rounding of the no. 3.4467567 upto 2 decimals is: ",round(3.4467567, 2))
print("------------------")
#POW
print("The power of 3 to the power 5 is: ",pow(3,5))

