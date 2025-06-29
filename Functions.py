from Dictionary import matrix


def greet():
    print("Hello")
greet()

print([greet() for i in range(4)])
print('-'*50)

for i in range(5):
    greet()
print('-'*50)

g_var = 12
def func():
    l_var = 5
    print(g_var,l_var)
func()
print('-'*50)

#Passing the parameters
def greet(n='-----'):
    print('Hello',n)

greet('Ainadri')
# greet(str(input("Enter a string: ")))
greet()
print('-'*50)


def Sum(a = 0,b = 0):
    print(a,b,a+b)
Sum(5,6)
Sum()
# Sum(int(input("Enter the value of a: ")), int(input("Enter the value of b: ")))
print('-'*50)

#Return
def Sum(a = 0,b = 0):
    return a+b

s = Sum(10,5)
print(s)
print('-'*50)

#Multi Return
def arithmetic(a = 0,b = 0):
    return a+b, a-b, a*b, a/b

s = arithmetic(10,5)
print(s)
print('-'*50)

# Multilevel Functions
lst = [1,2,3,4,5]

def sq(lst):
    return [i**2 for i in lst]

def cu(lst):
    return [i**3 for i in lst]

print("Multilevel Functions")
print(sq(lst))
print(cu(lst))

def sum_func(input_list = None):
    if input_list is None:
        input_list = lst
    lst_1 = sq(input_list)
    lst_2 = cu(input_list)
    return [lst_1[i] + lst_2[i] for i in range(len(lst_1))]
print(sum_func())

print('-'*50)


#SPECIAL FUNCTIONS

#ZIP FUNCTION

lst1 = ['Ainadri', 'Soumya', 'Subhankar']
lst2 = [25, 22, 27]

print(list(zip(lst1,lst2)))
print('-'*50)

matrix = [(1,2,3),(4,5,6),(7,8,9)]
print([list(row) for row in zip(matrix)])
# To get the transpose of the matrix
print([list(row) for row in zip(*matrix)])

# *matrix unpacks the rows as separate arguments.
# zip(*matrix) transposes the matrix.
# The asterisk is essential here — it lets zip() work on rows as separate inputs.

print([list (row) for row in zip(*[list(row) for row in zip(*matrix)])])
print('-'*50)

#Printing the dot product of the two matrix
lst_1 = [2,4,6]
lst_2 = [1,3,5]

print(sum([i*j for i,j in zip(lst_1, lst_2)]))
print('-'*50)

lst = [1,2,3,4,5,6,7,8,9]

#FILTER FUNCTION
def is_even(n):
    return n%2 == 0
print(list(filter(is_even, lst)))
print('-'*50)

#lAMBDA FUNCTION
add_num = lambda x,y : x*y
print(add_num(2,5))
print('-'*50)

num = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x : x%2 == 0, num)))
print('-'*50)

#MAP FUNCTION
num = [1,2,3,4,5,6,7,8,9]    #You want to apply the same operation to every item in a list/tuple.
def sqr(x):
    return x**2
print(list(map(sqr,num)))
print('-'*50)

names = ['Ainadri', 'Soumya', 'Subhankar' ]

print(list(map(lambda x : len(x) , names)))
