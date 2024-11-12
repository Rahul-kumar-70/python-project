"""
107. Write a Python program to remove a specified column from a given nested list.
Original Nested list:
[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
After removing 1st column:
[[2, 3], [4, 5], [1, 1]]
Original Nested list:
[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
After removing 3rd column:
[[1, 2], [-2, 4], [1, -1]]

"""
lst=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
n=int(input("enter the column  u want to remove of the element:"))
lst1=[]
for i in lst:
   i.pop(n)
   lst1.append(i)
print(lst1)