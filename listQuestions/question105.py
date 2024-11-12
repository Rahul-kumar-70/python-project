"""
105. Write a Python program to compute average of two given lists.
Original list:
[1, 1, 3, 4, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 4, 5, 7, 8]
Average of two lists:
3.823529411764706
"""
lst=[1, 1, 3, 4, 4, 5, 6, 7]
lst1=[0, 1, 2, 3, 4, 4, 5, 7, 8]
a=sum(lst)+sum(lst1)
print(a/(len(lst)+len(lst1)))