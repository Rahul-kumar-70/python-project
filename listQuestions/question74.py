''' Write a Python program to pack consecutive duplicates of a given list elements into sublists.
	Original list:
	[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
	After packing consecutive duplicates of the said list elements into sublists:
	[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]'''
"""lst=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
lst1=[]
t=0
for i in range(0,len(lst)-5):
    lst2 = [] * i
    i=t
    lst2.append(lst[i])
    for j in range(i+1,len(lst)):
        if lst[i]==lst[j]:
            #lst2=[]*i
            lst2.append(lst[j])
           # lst1.append(lst2)
        else:
            t=j
            break
            lst2=[]*i
            lst2.append(lst[i])
            lst1.append(lst2)
    lst1.append(lst2)
print(lst1)
"""
lst=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
lst1=[]
lst2=[]
for i in range(len(lst)):
    lst2=list()
    lst2.append(lst[i])
    for j in range(i+1,len(lst)):
        if lst[i]==lst[j]:
            lst2.append(lst[j])
        else:
            i=j
            break
            lst1.append(l)
    print(lst1)

