"""Write a Python program to read a square matrix from the console and print the sum of the matrix's primary diagonal.
Accept the size of the square matrix and elements for each column separated with a space (for every row) as input from the user.
Input the size of the matrix: 3
2 3 4
4 5 6
3 4 7
Sum of matrix primary diagonal:
14"""
"""n=int(input("enter the no of row and columns:"))
lst=[]
for i in range(n):
    lst1=[]
    for j in range(n):
        lst2=int(input("enter the element:"))
        lst1.append(lst2)
    lst.append(lst1)
print(lst)
sum=0
for k in range(len(lst)):
    sum=sum+lst[k][k]
print("Sum of matrix primary diagonal:",sum)"""

"""import numpy as np
d=np.array([2,3,4,4,5,6,3,4,7]).reshape(3,3)
print(d)
a=d[(0,1,2),(0,1,2)]
print(sum(a))"""
