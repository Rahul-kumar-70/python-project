""" Write a Python program to Zip two given lists of lists.
Original lists:
[[1, 3], [5, 7], [9, 11]]
[[2, 4], [6, 8], [10, 12, 14]]
Zipped list:
[[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]"""
lst1=[[1, 3], [5, 7], [9, 11]]
lst2=[[2, 4], [6, 8], [10, 12, 14]]
for i in range(0,len(lst1)):
    for j in range(0,len(lst2[i])):
        lst1[i].append(lst2[i][j])

print(lst1)