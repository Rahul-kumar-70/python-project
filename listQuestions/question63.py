''' Write a Python program to insert a given string at the beginning of all items in a list.
	Sample list : [1,2,3,4], string : emp
	Expected output : ['emp1', 'emp2', 'emp3', 'emp4']'''
lst=[1,2,3,4,5]
lst1=[]
st='emp'
for i in lst:
    lst1.append(st+str(i))
print(lst1)


