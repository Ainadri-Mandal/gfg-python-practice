#Reverse a string

str = str(input("Enter a string of your choice to reverse it: "))
reverse = ""

for char in str:
    reverse = char + reverse
print("Your reversed string is: ", reverse)