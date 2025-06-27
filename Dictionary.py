#DICTIONARY
dct = {1 : 'Ainadri', 2 : 'Soumya', 3 : 'Subhankar', 4 : 'Aindrila', 5 : 'Dorankar'}
print("The first Dictionary is : " , dct)
print('-' * 50)

#Accesing the elements in dictionary
print(dct)
print("The 1st & 2nd element of the dictionary are: ",dct[1],',', dct[2])
print(dct.get(2))
print('-' * 50)

#Adding and updating the key value pairs
print(dct)
dct[6] = 'Sana'    #adding
print("The updated dct is : ",dct)
dct[6] = 'Priyankar'   #updating
print("The dictionary after updating the value of key: ",dct)
del dct[6]     #deleting
print("Deleting the key value pair is: ", dct)
print('-' * 50)

#Cleaning the dictionary
print(dct)
dct.clear()
print("Dictionary after clearing: ",dct)
print('-' * 50)

#Iterating through the dictionary
dct = {1 : 'Ainadri', 2 : 'Soumya', 3 : 'Subhankar', 4 : 'Aindrila', 5 : 'Dorankar'}
print(dct)
print(dct.keys())
print(dct.values())


for k in dct.keys():
    print(k, dct[k])
print('-' * 50)

print("Dct items in tuples format : ",dct.items())
for i in dct.items():
    print(i)
print('-' * 50)

for k,v in dct.items():
    print(k,v)      #This loops over the (key, value) pairs (tuples) in the dictionary, and prints key (k) and value (v).
print('-' * 50)

#Check if key is present
print(dct)
print(1 in dct)
print(10 in dct)
print('1' in dct)
print('-' * 50)

#dct Updating in dictionaries

dct_1 = {1: 'A', 2: 'B', 3 : 'C' }
dct_2 = {1 : 'a', 2 : 'b', 3 : 'c'}

dct_1.update(dct_2)  #dct_1 keys & value are updated by k and v of dct_2
print("The dict_1 gets overwritten by the values of dict_2 : ",dct_1)       # As both the dict have same keys so it was overwritten by dict_2
print('-' * 50)

dct_2 = {4 : 'a', 5 : 'b', 6 : 'c'}
dct_1.update(dct_2)
print("The updated dct_1 is after changing the keys in dict_2 : ",dct_1)

#Merging using | operator
merged = dct_1 | dct_2
print("Merged dictionary using | operator (only works on py 3.9+) :",merged)
print('-' * 50)

#Dictionary methods
# dict.clear() - Remove all the elements from the dictionary
#
# dict.copy() - Returns a copy of the dictionary
#
# dict.get(key, default = “None”) - Returns the value of specified key
#
# dict.items() - Returns a list containing a tuple for each key value pair
#
# dict.keys() - Returns a list containing dictionary’s keys
#
# dict.update(dict2) - Updates dictionary with specified key-value pairs
#
# dict.values() - Returns a list of all the values of dictionary
# pop() - Remove the element with specified key
#
# popItem() - Removes the last inserted key-value pair
#
# dict.setdefault(key,default= “None”) - set the key to the default value if the key is not specified in the dictionary
#
# dict.has_key(key) - returns true if the dictionary contains the specified key.
#
# dict.get(key, default = “None”) - used to get the value specified for the passed key.


# MULTI DIMENSIONAL DICTIONARY

dct = { 1 : {'name' : 'Ainadri', 'phone': 123456789},
        2 : {'name' : 'Subhankar', 'phone': 123456789},
        3 : {'name' : 'Soumya', 'phone': 123456789}}
print(dct)
print('-' * 50)

#Accesing the Elements
print(dct)
print(dct[1])
print(dct[1]['name'])

#Adding
print(dct)
dct[4] = {'name': 'Jhimli', 'phone': 123456789}
print(dct)
print('-' * 50)

#Updating
print(dct)
dct[2]['name'] = 'Dorankar'
print("The name is updated from Subhankar to Dorankar in Roll No. 2 : ",dct)
print('-' * 50)

#Deleting
print(dct)
del dct[4]
print(dct)
print('-' * 50)


#Going through the data

print(dct)

print(dct)

for i in dct.keys():
    print(i, dct[i]['name'],dct[i]['phone'])
print('-' * 50)

#Going a level deeper with marks

data = { 1 : {'name' : 'Ainadri', 'phone': 123456789, 'marks': {'Hindi': 45, "Maths": 40 , 'Science': 42}},
         2 : {'name' : 'Subhankar', 'phone': 123456789, 'marks': {'Hindi': 24, "Maths": 45 , 'Science': 40}},
         3 : {'name' : 'Soumya', 'phone': 123456789, 'marks': {'Hindi': 35, "Maths": 38 , 'Science': 40}}}
print(data)

for i in data.keys():
    print(i, data[i]['name'], data[i]['marks'])
    print(i,data[i]['name'],data[i]['marks']['Hindi'])
print('-' * 50)

#DICTIONARY COMPREHENSIONS

print("Print the dictionary for key i and its square as value: ",{i : i**2 for i in range(1,6)})
print('-' * 50)

#Dictionaries with conditions
print("Print only even cubes in a dictionary: ",{i : i**3 for i in range(1,11) if i%2 == 0})

#Dictionaries from list
lst = ['Apple','Banana', 'Grapes']
dct = {item : len(item) for item in lst}
print(dct)
print('-' * 50)
#in reverse
print({len(item) :item  for item in lst})

#Special keys from lists

lst1 = ['a','b','c','d']
lst2 = [1,2,3,4]

print({lst2[i] : lst1[i] for i in range(len(lst2))})
print('-' * 50)

#Matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
final_dct = { matrix[i][j]: (i,j) for i in range(3) for j in range(3)}
print(final_dct)

print('-' * 50)

