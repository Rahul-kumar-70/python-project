#Write a Python program to count the number of elements in a list within a specified range.
lst=[2,4,5,6,7,8,9,6,4,3,2]
print(lst)
lst1=[]
n=int(input("enter the 1st value:"))
m=int(input("enter the 2st value:"))
"""for i in range(lst.index(n),lst.index(m)):
    val=lst.index(n)
    for j in range(lst.index(m)-lst.index(m)):
        lst1.append(lst[val])
        val=val+1
print("Number of elements in list:",len(lst1))"""
x=lst.index(n)
if lst.count(n)>1:
    val=lst.count(n)
    for j in range(lst[x+1:]):
        if lst[lst.index(n)]==lst[lst.index(m)]:
            print('jo')