# Write a Python program to find all the values in a list are greater than a specified number.
lst=[5,1,2,3,7,9,8,11,10]
n=5
lst1=[]
for i in lst:
    if i>n:
        lst1.append(i)
print(lst1)
        