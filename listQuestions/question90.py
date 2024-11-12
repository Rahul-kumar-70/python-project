"""Write a Python program to count the number of lists in a given list of lists.
Original list:
[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
Number of lists in said list of lists:
4
Original list:
[[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
Number of lists in said list of lists:
3"""
lst=[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
lst1=[[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
print("original list:")
print(lst)
print("Number of lists in said list of lists:",len(lst))
print("original list:")
print(lst1)
print("Number of lists in said list of lists:",len(lst1))