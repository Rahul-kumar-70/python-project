"""Write a Python program to split a given list into two parts where the length of the first part of the list is given.
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Length of the first part of the list: 3
Splited the said list into two parts:
([1, 1, 2], [3, 4, 4, 5, 1])"""
lst=[1, 1, 2, 3, 4, 4, 5, 1]
lst1=[]
lst2=[]
n=int(input("enter the number u want to Length of the first part of the list:"))
for i in range(0,n):
    lst1.append(lst[i])
for j in range(n+1,len(lst)):
    lst2.append(lst[j])
t1=(lst1,lst2)
print(t1)