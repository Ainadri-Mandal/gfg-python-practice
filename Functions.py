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
greet(str(input("Enter a string: ")))
greet()
print('-'*50)


def Sum(a = 0,b = 0):
    print(a,b,a+b)
Sum(5,6)
Sum()
Sum(int(input("Enter the value of a: ")), int(input("Enter the value of b: ")))
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



