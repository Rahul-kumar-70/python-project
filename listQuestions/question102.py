"""
102. Write a Python program to extract specified size of strings from a give list of string values.
	Original list:
	['Python', 'list', 'exercises', 'practice', 'solution']
	length of the string to extract:
	8
	After extracting strings of specified length from the said list:
	['practice', 'solution']
"""
lst=['Python', 'list', 'exercises', 'practice', 'solution']
print(lst)
lst1=[]
n=int(input("length of the string to extract:"))
for i in lst:
    if len(i)==n:
        lst1.append(i)
print(lst1)