#sum of 1st n natural no.s
n = int(input("Enter the the no.: "))
total = 0

for i in range(1, n+1):
    total += i
print("The sum of your input n natural no.s are: ", total)

#Find Maximum Element in a List
list = [1, 45, 35, 6, 8, 29, 50, 37, 67, 45, 36]
max_val = list[0]

for num in list:
    if num > max_val:
        max_val = num
print("The maximum value of the list is : ", max_val)

# Count Frequency of a Specific Element