"""Write a Python program to generate combinations of n distinct objects taken from the elements of a given list.
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] Combinations of 2 distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]"""
lst=[1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0,len(lst)):
    lst1=list()
    lst1.append(lst[i])
    for j in range(i+1,len(lst)):
        lst1.append(lst[j])
        print(lst1,end=" ")
        lst1.pop()
