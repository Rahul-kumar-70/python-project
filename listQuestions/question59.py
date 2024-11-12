#Write a Python program to check whether the n-th element exists in a given list.
lst=[3,4,5,7,9,1,11,12,13]
print("given List:",lst)
for i in lst:
    if i==len(lst)-1:
        break
print(i)
