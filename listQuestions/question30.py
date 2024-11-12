#Write a Python program to get the frequency of the elements in a list.

lst=[1,2,3,4,5,5,4,3,2,1,6,7,8,9]
lst1={}
for i in lst:
    if i in lst1:
        lst1[i]+=1
    else:
        lst1[i]=1
print("frequency of value:",lst1)


