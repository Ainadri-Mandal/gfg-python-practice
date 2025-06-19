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
print("------------------")
#Comparison Operators

x=5
y=7

print('is x equal to y -', x==y)
print('is x not equal to y -', x!=y)
print('is x greater than y -', x>y)
print('is x less than y -', x<y)
print('is x less than or equal to y -', x<=y)
print('is x greater than or equal to y -', x>=y)
print("------------------")
# LEFT SHIFT

a = 5  # Binary: 0b101
result = a << 1  # Binary: 0b1010 (Left shift by 1 position)
print("Left shift of 5 is : ",result)
print("------------------")

# RIGHT SHIFT

a = 20  #binary - 0b10100
result = a >> 2  #shifts right by 2 position- 0b00101->5
print("Right shift of 20 is : ",result)
print("------------------")

#TYPECASTING

#int
print(3.14)
print(int(3.14))
print(int('1454'))    #only when no. is in string it can be converted into an integer NO CHARACTER for str to int coversion
print(int(False))
print(int(False + True + True))
print("----------------------")
#float
print(float(3))
print(float(True))
print((float('10.5')))
print("----------------------")

#String
print(str(132))
print(str(123.13))
print(str(True))
print("----------------------")

#Bool
print((bool(1)))
print((bool(1252353646)))
print((bool(-635436)))
print(bool(0))
print((bool(0.0)))
print(bool(525353.8866))
print((bool('Ainadri')))
print(bool('A'))
print("----------------------")

print("--------EXCEPTIONS--------")
print(int(float('3.14'))) #This requires a two step process to be done
print(float(int(3.14)))   #We will not get 3.14 back we will get 3.0


#STRING FUNCTIONS
#Concatenation
print('Ainadri'+ ' ' + 'Mandal')
#String Replication
print('Ainadri'* 5)
print('-' * 20)
#String Length
print(len('AinadriMandal'))
print(len('Ainadri Mandal'))
print('-' * 20)
#String Slicing
print('Ainadri Mandal'[0])
print('Ainadri Mandal'[-14])
print('Ainadri Mandal'[0:7])
print('Ainadri Mandal'[8:14])
print('Ainadri Mandal'[3:])
print('Ainadri Mandal'[:8])
print('-' * 20)

#String Case Conversion
print('Ainadri Mandal'.lower())
print('Ainadri Mandal'.upper())
print('-' * 20)

#String Stripping
print('   Ainadri Mandal    ')
print('   Ainadri Mandal    '.strip())
print('   Ainadri       Mandal    '.strip())
print('-' * 20)

#String Replacing
print('Ainadri Mandal')
print('Ainadri Mandal'.replace('a','-'))
print('-' * 20)

#String Count
print('Ainadri Mandal')
print('Ainadri Mandal'.count('a'))
print('Ainadri Mandal'.lower().count('a'))
print('-' * 20)

#String Find
print('Ainadri Mandal')
print('Ainadri Mandal'.find('Ain'))
print('Ainadri Mandal'.find('Man'))
print('-' * 20)
#String Check
print('Ainadri'.isalpha())
print('1345'.isdigit())
print('A M'.isupper())
print('ainadri'.islower())
print('-' * 20)

#String Capitalization
print('aINADRI Mandal')
print('aINADRI Mandal'.capitalize())
print('-' * 20)

#Checkfor start and end
print('Ainadri Mandal')
print('Ainadri Mandal'.startswith('Ain'))
print('Ainadri Mandal'.endswith('dal'))
print('-' * 20)

#String length aligning and positioning
print('Ainadri Mandal'.center(20, "-"))
print('Ainadri Mandal'.rjust(20, '-'))
print('Ainadri Mandal'.ljust(20, '-'))
print('-' * 20)

#String Formatting

#Default order
str = "{} {} {}".format('Ainadri', 'is', 'Engineer')
print("The default string is: ", str)

#Positional Formatting
str1 = "{1} {0} {2}".format('Ainadri', 'is', 'Engineer')
print('\nPrint String in Positional order:', str1)

#Keyword Formatting
str2 = '{l} {f} {g}'.format(g='Ainadri', f = 'is', l="Engineer")
print('\nPrint string in order of keywords: ', str2)
print('-' * 20)

#Variable
#Ways to assign values to a variable

a=5
b=10
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a**b)

a = 5
b = 4
c = 6
d = 8
#or we can also write it as

a, b, c, d = 7, 5, 8, 3
print(a,b,c,d)

#FOR LOOP

#Using range()
for i in range(5):
    print(i)
print('-' * 20)
for i in range(1, 10, 2):    #You can also specify start, stop, and step:
    print(i)
print('-' * 20)

#Looping through a List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print('-' * 20)

#Looping through a String
for char in "hello":
    print(char)
print('-' * 20)
#Loop with else
for i in range(3):
    print(i)
else:
    print("Loop completed")
print('-' * 20)

#Using break and continue
for i in range(5):
    if i == 3:         #break — exit the loop early:
        break
    print(i)
print('-' * 20)
for i in range(5):
    if i == 3:         #continue — skip current iteration:
        continue
    print(i)
print('-' * 20)

#Looping through a Dictionary
my_dict = {"a": 1, "b": 2}
for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)
print('-' * 20)

#Using enumerate()
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(index, name)
print('-' * 20)

#Using zip()
names = ["Alice", "Bob"]     #To loop over two (or more) sequences at once:
scores = [85, 92]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")
print('-' * 20)

#Nested for Loops
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
print('-' * 20)

#DATA STRUCTURES
# LIST

lst = ['Ainadri', 'Soumya', 'Subhankar', 'Jhimli', 'Aindrila', 'Rimli']

print(lst)

print(lst[0])
print(lst[4])
print(lst[-1])
print('-'* 50)

#Modify the values in list using indexing
print(lst)
lst[2] = 'Dorankar'
print(lst)
print('-'* 50)

#Slicing
print(lst)
print("The slicing value is : ",lst[1:4])
print('-'* 50)

#Reverse a string
print(lst)
print(lst[::-1])
print(lst[::-2])

#Appending
print('-'* 50)
print(lst)
lst.append("Priyankar")
print(lst)
print('-'* 50)

#Removing

print(lst)
lst.remove("Priyankar")
print(lst)
print('-'* 50)

#Sorting

lst = [3,5,7,4,3,5,7,4,43,9]
print(lst)
print(sorted(lst))
print('-'* 50)

#Find the element

lst = ['Ainadri', 'Soumya', 'Subhankar', 'Jhimli', 'Aindrila', 'Rimli']
print("The index of Ainadri in the list is: ",lst.index('Aindrila'))
print('-'* 50)

#Count the element in the list
print(lst)
lst = ['Ainadri', 'Soumya', 'Aindrila', 'Subhankar', 'Aindrila', 'Jhimli', 'Aindrila', 'Rimli']
print(lst)
print("The count of Aindrila in the updated list is: ",lst.count("Aindrila"))
print('-'* 50)

#Extending the list

lst.extend(['Ankit', 'Ankush', 'Pragya', 'Swati'])
print(lst)
print('-'* 50)

#Find the maximum and the minimum in the list


