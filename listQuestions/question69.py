'''Write a Python program to remove duplicates from a list of lists.
		Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
		New List : [[10, 20], [30, 56, 25], [33], [40]]'''
lst=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
lst1=[]
for i in lst:
    if not i in lst1:
        lst1.append(i)
print(lst1)