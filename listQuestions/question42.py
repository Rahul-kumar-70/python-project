'''Write a Python program to find missing and additional values in two lists.
	Sample data : Missing values in second list: b,a,c
	Additional values in second list: g,h'''
lst=['a','b','c','d','e','f','g']
lst1=['d','e','g','h','i','j']
lst2=[]
lst3=[]
for i in lst:
    for j in lst1:
        if i not in j:
           lst2.append(i)
        if i in j:
            lst3.append(i)
print(lst2)
print(lst3)
