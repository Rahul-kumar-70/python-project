#Write a Python program to select the odd items of a list.
lst=[1,3,5,7,'python','html','css','js']
lst1=[]
for val in lst[::2]:
    lst1.append(val)
print(lst1)
    