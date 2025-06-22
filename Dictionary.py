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



