from linecache import clearcache

my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))
print('-'*50)

#Adding
print(my_set)
my_set.add(6)
print(my_set)
print('-'*50)

# Popping
print(my_set)
popped_element = my_set.pop()
print(popped_element)
print('-'*50)

# Remove
print(my_set)
my_set.discard(3)
print(my_set)
print('-'*50)

#Iterating
for i in my_set:
    print(i)
print('-'*50)

#Checking the values
print(2 in my_set)
print(3 in my_set)
print(4 in my_set)
print('-'*50)

# Set Operations
set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8}
print('Union : ', set_1 | set_2)
print('Intersection : ', set_1 & set_2)
print('Difference : ', set_1 - set_2)
print('Symmetric Difference : ', set_1 ^ set_2)
print('-'*50)

# Clearing
print(my_set)
my_set.clear()
print(my_set)


#TUPLE




