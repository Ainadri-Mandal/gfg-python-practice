class person:
    name = 'Ainadri'
    age = 25

p1 = person()   # p1 is an object of class person()
print(p1)
print(p1.name)
print(p1.age)
print('-'*50)

p1.name = 'Rimli'
p1.age = 21
print(p1.name)
print(p1.age)
print('-'*50)

p2 = person()  # p2 object will take the default value of name and age already given if no input is given
print(p2.name)
print(p2.age)

print('-'*50)

# class mathematics:
#     name = 'Ainadri'
#
#     def greet(self):
#         print('Hello')
# math = mathematics()
# math.greet()
# print(math.name)


class mathematics:
    name = 'Ainadri'

    def greet(self):
        print('Hello')
        return 'Hi'

    def factorial(self,n):
        s = 1
        for i in range(1,n+1):
            s*=i
        return  s
    def lst_mul(self,lst):
        s = 1
        for i in lst:
            s*=i
        return s
    def lst_dot(self,lst_1,lst_2):
        return [lst_1[i] * lst_2[i] for i in range(len(lst_1))]

math = mathematics()
print(math.greet())
print('-'*50)

print(math.factorial(5))
print('-'*50)
print(math.lst_mul([3,4,5]))
print('-'*50)
print(math.lst_dot([1,2,3],[4,5,6]))
print('-'*50)

# METHODS

class person:

    def __init__(self, name, age):   #__init__ is a special method in a class.
        # It automatically runs when you create a new object.
        self.name = name
        self.age = age

    def run(self):
        print(self.name)
        print('run!')

p1 = person('Ainadri', 21)
p2 = person('Aindrila', 21)
p3 = person('Jhimli',23)

print('-'*50)
p2.run()
p1.run()
print('-'*50)



class agent:

    def __init__(self, name, age):
        print("Welcome to the game!")
        self.name = name
        self.age = age
        self.health = 100
        self.alive = True

    def curr_health(self):
        print('Current Health of', self.name, 'is', self.health)
        print('run!')

    def punched(self):
        self.health -= 10

    def shooted(self):
        self.health -= 50

    def is_alive(self):
        if self.health <= 0:
           self.alive = False

    def info(self):
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Health : ", self.health)
        print("Alive  : ", self.alive)

p1 = agent('Ainadri', 21)
p1.curr_health()
p1.punched()
p1.punched()
p1.shooted()
p1.info()
print('-'*50)

p2 = agent('Ankur', 24)
p2.curr_health()
p2.punched()
p2.shooted()
p2.shooted()
p2.info()
print('-'*50)

#Inheritance
class boss(agent):

    def blow_fire(self):
        print("blow fire!")

bs = boss('Maxfinn', 1000)
bs.info()
bs.blow_fire()
print(bs)