# Count all the vowels in the string taking user input
str = str(input("Enter Your String to count the vowels: "))
vowels = "aeiouAEIOU"
count = 0
for char in str:
    if char in vowels:
        count += 1
print("No. of Vowels in your string are: ", count)