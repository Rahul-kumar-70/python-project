"""
101. Write a Python program to sort a given matrix in ascending order according to the sum of its rows.
	Original Matrix:
	[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
	Sort the said matrix in ascending order according to the sum of its rows
	[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
	Original Matrix:
	[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
	Sort the said matrix in ascending order according to the sum of its rows
	[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
"""
lst=[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
lst1=[]
for i in lst:
    lst1.append(sum(i))
lst1.sort()
for j in range(len(lst)):
    if lst1[j]==sum(lst[j]):
        print(lst[j])

print(lst1)