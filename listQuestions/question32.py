# Write a Python program to check whether a list contains a sublist.
lst=[1,2,3,[1,2,3]]
for i in lst:
    if type(i)==list:
        res=True
    else:
        res=False
print(res)