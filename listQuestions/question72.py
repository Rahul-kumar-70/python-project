'''Write a Python program to flatten a given nested list structure.
		Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
		Flatten list:
		[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]'''
lst=[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
lst1=[]
for i in lst:
    if type(i)==int:
        lst1.append(i)
    elif type(i)==list:
        for j in i:
            lst1.append(j)
print(lst1)