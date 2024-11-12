"""
115. Write a Python program to check if the elements of a given list are unique or not.
Original list:
[1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
Is the said list contains all unique elements!
False
Original list:
[2, 4, 6, 8, 10, 12, 14]
Is the said list contains all unique elements!
True
"""
lst=[1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
res=bool()
lst.sort()
for i in range(len(lst)-1):
    if lst[i]==lst[i+1]:
        res=False
        break
    else:
        res=True
print(res)