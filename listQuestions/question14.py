# Write a Python program to print the numbers of a specified list after removing even numbers from it.
lst=[1,2,4,6,7,8,9,11,13]
lst1=[]
for i in lst:
    if i%2==0:
        continue
    else:
        lst1.append(i)
print(lst1)
        