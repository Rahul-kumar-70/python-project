"""Write a Python program to check if a nested list is a subset of another nested list.
Original list:
[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
[[1, 3], [13, 15, 17]]
If the one of the said list is a subset of another.:
True
Original list:
[[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
[[[3, 4], [5, 6]]]
If the one of the said list is a subset of another.:
True
Original list:
[[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
[[[3, 4], [5, 6]]]
If the one of the said list is a subset of another.:
False"""

"""lst=[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
lst1=[[1, 3], [13, 15, 17]]"""
lst=input("enter the list:")
lst1=input("enter the subset :")
count=0
for i in range(len(lst1)):
    for j in range(len(lst)):
        if lst1[i]==lst[j]:
            count+=1
            if count==len(lst1):
                res=True
            else:
                res=False
print(res)
