"""Write a Python program to find a list with maximum and minimum lengths.
Original list:
[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
List with maximum length of lists:
(3, [13, 15, 17])
List with minimum length of lists:
(1, [0])
Original list:
[[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
List with maximum length of lists:
(3, [3, 5, 7])
List with minimum length of lists:
(1, [0])
Original list:
[[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
List with maximum length of lists:
(4, [1, 34, 5, 7])
List with minimum length of lists:
(1, [12])"""

lst=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
lst.sort()
a=(len(lst[0]),lst[0])
print(a)
b=(len(lst[-1]),lst[-1])
print(b)
