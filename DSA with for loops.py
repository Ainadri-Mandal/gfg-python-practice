#sum of 1st n natural no.s
n = int(input("Enter the the no.: "))
total = 0

for i in range(1, n+1):
    total += i
print("The sum of your input n natural no.s are: ", total)
print('-' * 50)
#Find Maximum Element in a List
list1 = [1, 45, 35, 6, 8, 29, 50, 37, 67, 45, 36]
max_val = list1[0]

for num in list1:
    if num > max_val:
        max_val = num
print("The maximum value of the list is : ", max_val)
print('-' * 50)
# Count Frequency of a Specific Element

arr = list(map(int, input("Enter the no.s to be in the array separated by space: ").split()))
target = int(input("Enter a no. to see the frequency in your list: "))
count = 0

for num in arr:
    if target == num:
        count += 1
print(f"Input {target} has appeared {count} times in the list.")

