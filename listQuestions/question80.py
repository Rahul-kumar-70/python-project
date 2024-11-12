"""Write a Python program to insert an element at a specified position into a given list.
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
After inserting an element at kth position in the said list:
[1, 1, 12, 2, 3, 4, 4, 5, 1]"""
lst=[1, 1, 2, 3, 4, 4, 5, 1]
print("Given Lst:",lst)
ind=int(input("enter the index you want to add:"))
val=int(input("enter the value u want to add in the list:"))
lst.insert(ind,val)
print(lst)