"""
Write a Python program that checks whether a string represents an integer or not.
Expected Output:

Input a string: Python
The string is not an integer
"""
s=input("enter the string :")
if s.isalpha():
    print("The string is not an integer")
else:
    print("invalid ")