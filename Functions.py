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
