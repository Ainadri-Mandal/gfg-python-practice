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