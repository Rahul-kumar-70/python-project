"""

106. Write a Python program to count integer in a given mixed list.
Original list:
[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
Number of integers in the said mixed list:
6
"""
lst=[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
lst1=[]
print(lst)
for i in lst:
    if type(i)==int:
        lst1.append(i)
print("Number of integers in the said mixed list:",len(lst1))
        