"""Write a Python program to round the numbers in a given list, print the minimum and maximum numbers and multiply the
numbers by 5. Print the unique numbers in ascending order separated by space.
Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
Minimum value: 4
Maximum value: 22
Result:
20 25 45 55 60 70 80 90 110"""
lst=[22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
lst1=[]
lst3=[]
for i in lst:
    lst1.append(round(i)*5)
minv=min(lst)
maxv=max(lst)
print(round(minv))
print(round(maxv))
lst1.sort()
print(lst1)