""" Write a Python program that accepts a string and calculates the number of digits and letters.
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2"""
s=input("enter the string and digit:")
countL=0
countD=0
for i in s:
    if i.isalpha():
        countL+=1
    elif i.isdigit():
        countD+=1
    else:
        continue
print("Letters:",countL)
print("Digits:",countD)