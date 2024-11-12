#Write a Python program to insert an element before each element of a list.
lst=[1,2,3,4,5,6,7,8,9]
for i in range(0,len(lst)+len(lst),2):
    lst.insert(i, 10)
print(lst)
