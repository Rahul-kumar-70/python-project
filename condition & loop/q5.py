# Write a Python program that accepts a word from the user and reverses it.
s=input("enter the any word:")
if s.isalpha():
    print(s[::-1])
else:
    print("invalid string")