# Write a Python program to remove duplicates from a list.
lst=[1,5,7,9,1,3,4,5,6,7,8]
"""val=[]
for i in lst:
    if not i in val:
        val.append(i)
print(val)"""
lst1=set(lst)
print(list(lst1))