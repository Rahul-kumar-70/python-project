""" Write a Python program to create a multidimensional list (lists of lists) with zeros.
Multidimensional list: [[0, 0], [0, 0], [0, 0]]"""
n=int(input("enter the number how many u want to list in list:"))
lst=[]
for i in range(0,n):
    lst1=list()*i
    lst1.append(0)
    lst1.append(0)
    lst.append(lst1)
print(lst,end=" ")