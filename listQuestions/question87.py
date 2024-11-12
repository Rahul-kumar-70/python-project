""" Write a Python program to read a matrix from the console and print the sum for each column. As input from the user, accept
matrix rows, columns, and elements separated by a space (each row).
Input rows: 2
Input columns: 2
Input number of elements in a row (1, 2, 3):
1 2
3 4
sum for each column:
4 6"""
n=int(input("enter the number of rows:"))
m=int(input("enter the number of columns:"))
print("enter m*n=",m*n,"elements")
lst=[]
for i in range(n):
    lst2=[]
    for j in range(m):
        lst1=int(input())
        lst2.append(lst1)
    lst.append(lst2)
print(lst)
s=0
for c in range(m):
    s=0
    for r in range(n):
        s=s+lst[r][c]
    print(s,end=" ")






