"""
108. Write a Python program to extract a specified column from a given nested list.
Original Nested list:
[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
Extract 1st column:
[1, 2, 1]
Original Nested list:
[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
Extract 3rd column:
[3, -5, 1]
"""
lst=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
lst1=[]
n=int(input("enter the column  u want to remove of the element:"))
for i in lst:
    a=i.pop(n)
    lst1.append(a)
print(lst1)