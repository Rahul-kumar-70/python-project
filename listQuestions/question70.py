'''Write a Python program to find the items starts with specific character from a given list.
		Expected Output:
		Original list:
		['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
		Items start with a from the said list:
		['abcd', 'abc', 'acjd']
		Items start with d from the said list:
		['dagfa']
		Items start with w from the said list:
		[]'''
s=input("enter the character:")
lst=['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
lst1=[]
for i in lst:
    if i[0]==s:
        lst1.append(i)
print("Items start with {} from said list:{}".format(s,lst1))