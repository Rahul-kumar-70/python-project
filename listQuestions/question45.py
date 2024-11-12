# Write a Python program to convert a pair of values into a sorted unique array.
l = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]
l2=[]
for i in l:
    for j in i:
        l2.append(j)
l2.sort()
print(list(set(l2)))
    