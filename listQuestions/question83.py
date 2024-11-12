"""Write a Python program to round every number in a given list of numbers and print the total sum multiplied by the length of the list.
Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
Result:
243"""
lst=[22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
res=0
for i in lst:
    res=round(i)*len(lst)+res
print(res)

