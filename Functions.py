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
def Sum(a = 0,b = 0):
    return a+b, a-b, a*b, a/b

s = Sum(10,5)
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

def sum_func():
    lst_1 = sq(lst)
    lst_2 = cu(lst)
    return [lst_1[i] + lst_2[i] for i in range(len(lst_1))]
print(sum_func())

print('-'*50)
