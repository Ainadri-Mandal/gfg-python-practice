print('A')
print("ASCII code if A is : ",ord('A'))
print("ASCII code if 0 is : ",ord('0'))
print('-'* 50)
# You can perform this for only one char at a time

#chr function
#to reverse from ASCII to char

print("The value of 78 as char : ",chr(78))
print("The value of 30 as char : ",chr(30))
print('-'* 50)


for i in range(33,127):
    print(i, chr(i))
print('-'* 50)

# Problem Statement - Caesar Cipher Encryption and Decryption. The Caesar cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

def encrypt(message, shift):
    return ''.join(chr(ord(char) + shift) for char in message)

def decrypt(encrypted_message, shift):
    return ''.join(chr(ord(char) - shift) for char in encrypted_message)

encrypted = encrypt("Hey Geek! What's your progress?", 5)
print("Encrypted Message:", encrypted)

decrypted = decrypt(encrypted, 5)
print("Decrypted Message:", decrypted)