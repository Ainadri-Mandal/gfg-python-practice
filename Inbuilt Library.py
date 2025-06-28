# Math Library

import math

x = 10.8
print(math.ceil(x))   #ceil stands for ceiling = rounding up
print(math.floor(x))   #floor stands for rounding down
print(math.trunc(x))    # trunc cuts off the decimal part
print('-'*50)


x = 3
print(math.exp(x))
print(math.log10(x))
print('-'*50)


x = 90
print(math.sin(x))
print(math.cos(x))
print(math.radians(x))
print('-'*50)

print(math.pi)
print(math.e)
print('-'*50)

print(10, math.factorial(10))
print('-'*50)

# Random library
import random

print(random.random())
print(random.randint(1,11))
print(random.choice([1,2,3,4,5]))  #picks one item.
print(random.sample([1,2,3,4,5], 2))   #picks without replacement (no repeats).
#random.sample(population, k) returns a new list of k unique elements randomly selected from the given population.
print(random.uniform(1.0,3.0))  #returns a random floating-point number between a and b
print('-'*50)


#DATETIME LIBRARY
import datetime

print(datetime.datetime.now())
print(datetime.datetime(2024,10,28,10,30))
print(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))

date_1 = datetime.datetime(2023,10,20,10,30,8)
date_2 = datetime.datetime.now()
print(date_1 - date_2)

# printing the date time in words

now = datetime.datetime.now()
formatted = now.strftime("%A, %B , %d, %Y at %I:%M %p")
print(formatted)

# | Code | Meaning                     | Example  |
# |------|-----------------------------|----------|
# | %A   | Full weekday name           | Saturday |
# | %B   | Full month name             | June     |
# | %d   | Day of the month (01–31)    | 28       |
# | %Y   | 4-digit year                | 2025     |
# | %I   | Hour (12-hour clock, 01–12) | 02       |
# | %M   | Minute                      | 45       |
# | %p   | AM/PM                       | PM       |

print('-'*50)

# COLLECTIONS LIBRARY
from collections import Counter, defaultdict, OrderedDict

lst = [1,2,3,4,5,5,5,6,6,7]
print(Counter(lst))
#Counter is like a dictionary that counts how many times each element appears in a list (or any iterable)
print('-'*50)

d = defaultdict(int)
d['a'] += 1
print(d)

# defaultdict is like a regular dict, but it provides a default value for missing keys.
#
# In this case, defaultdict(int) means:
#
# If a key is missing, it automatically starts with int() → which is 0.
print('-'*50)

d = OrderedDict()
d['One'] = 1
d['Two'] = 2
print(d)
print('-'*50)

# STRINGS
import  string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print('-'*50)

print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print('-'*50)

print(string.punctuation)
