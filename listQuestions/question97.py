"""Write a Python program to remove sublists from a given list of lists that contain an element outside a given range.
Original list:
[[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
After removing sublists from a given list of lists, which contains an element outside the given range:
[[13, 14, 15, 17]]"""
lst=[[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
for i in lst:
    for j in i:

