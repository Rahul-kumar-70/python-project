"""Write a Python program to find the maximum and minimum values in a given heterogeneous list.
Original list:
['Python', 3, 2, 4, 5, 'version']
Maximum and Minimum values in the said list:
(5, 2)"""
lst=['Python', 3, 2, 4, 5, 'version']
lst1=[]
for i in lst:
    if str(i).isdigit():
        lst1.append(i)
maxv=max(lst1),min(lst1)
print(tuple(maxv))