"""Write a Python program to sort a given list of lists by length and value.
Original list:
[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
Sort the list of lists by length and value:
[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]"""

lst=[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
lst.sort()
lst1=[]
d={}
for v in lst:
    d[len(v)]=v

val=list(d.keys())
for v in val:
    for j in lst:
        if v==len(j):
            lst1.append(j)
print(lst1)
