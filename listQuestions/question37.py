# Write a Python program to find common items from two lists.
lst=[1,2,3,5,7,8,9]
lst1=[1,3,5,7,8,9]
lst2=[]
for i in lst:
    for j in lst1:
        if i in j:
            lst2=[i]
print(lst)
print(lst1)
print("common items from both list:{}".format(lst2))