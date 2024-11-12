"""
Write a Python program to construct the following pattern, using a nested for loop.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
for l in range(n):
    for k in range(n-1,l,-1):
        print("*",end=" ")
    print()
