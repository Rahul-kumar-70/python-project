"""Write a Python program to extract a given number of randomly selected elements from a given list.
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Selected 3 random numbers of the above list:
[4, 4, 1]"""
import random as r
lst=[1, 1, 2, 3, 4, 4, 5, 1]
res=[r.choice(lst),r.choice(lst),r.choice(lst)]
print(res)