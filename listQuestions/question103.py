"""
103. Write a Python program to extract specified number of elements from a given list, which follows each other continuously.
	Original list:
	[1, 1, 3, 4, 4, 5, 6, 7]
	Extract 2 number of elements from the said list which follows each other continuously:
	[1, 4]
	Original lists:
	[0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
	Extract 4 number of elements from the said list which follows each other continuously:
	[4]
"""
lst=[1, 1, 3, 4, 4, 5, 6, 7]
n=int(input("enter the number u want to extract :"))
lst1=[]
for i in range(len(lst)):
    if (lst[i] in lst)==n:
        lst1.append(lst[i])
print(lst1)
