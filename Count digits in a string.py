#Count digits in a string

str = str(input("Enter your string of combination with no.s: "))
count = 0

for char in str:
    if char.isdigit():
        count += 1
print("No. of digits i your string are: ", count)