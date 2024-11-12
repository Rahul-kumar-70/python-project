"""Write a Python program that takes two digits m (row) and n (column) as input and generates a
two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note :
i = 0,1.., m-1
j = 0,1, n-1.

Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]"""
lst=[]
m=int(input("enter the no of rows:"))
n=int(input("enter the no of column:"))
for i in range(m):
    lst.append(list())
    for j in range(n):
        lst[i].append(i*j)
print(lst)
