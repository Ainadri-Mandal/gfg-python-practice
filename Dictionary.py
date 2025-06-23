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
