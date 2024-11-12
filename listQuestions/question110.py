"""
110. Write a Python program to find the item with maximum occurrences in a given list.
Original list:
[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
Item with maximum occurrences of the said list:
2
"""
lst=[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
d={}
for i in lst:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
a=max(d.values())
for j in d:
    if a==d[j]:
        print(j)
