"""
114. Write a Python program to extract the nth element from a given list of tuples.
Original list:
[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
Extract nth element ( n = 0 ) from the said list of tuples:
['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
Extract nth element ( n = 2 ) from the said list of tuples:
[99, 96, 94, 98]
"""
lst=[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
lst1=[]
lst2=[]
for i in lst:
    lst1.append(i[0])
    lst2.append(i[2])
print("Extract nth element ( n = 0 ) from the said list of tuples:",lst1)
print("Extract nth element ( n = 2 ) from the said list of tuples:",lst2)


