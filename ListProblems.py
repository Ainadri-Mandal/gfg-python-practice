#Square all the elements of the list
lst = [1,2,3,4,5,6]
print(lst)
lst = [i**2 for i in lst]
print(lst)
lst = [i**2 for i in lst]
print(lst)
print('-'*50)

#Finding the first 10 even numbers
print("The list of 1st 10 even no.s are: ",[i for i in range(11) if i%2 == 0])
print('-'*50)

# To find the n no. of even no.s by taking input n from user
n = int(input("Enter a limit to find the even no.s within: "))
print(f"The list of even no.s within {n} range is: ",[i for i in range(n) if i%2 == 0])
print('-'*50)

#WITH MULTI DIMENSIONAL LISTS
print("Here the range to 5 is printed 3 times: ",[[j for j in range(5)] for i in range(3)])
#here j list is printed 5 times due to range 5 in i list
print('-'*50)

#Example 2

lst = [[1,2,3],[4,5,6],[7,8,9]]
print("The elements of all the rows in list are : ",[j for i in lst for j in i])