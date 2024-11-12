"""Write a Python program to count the number of sublists that contain a particular element.
Original list:
[[1, 3], [5, 7], [1, 11], [1, 15, 7]]
Count 1 in the said list:
3
Count 7 in the said list:
2
Original list:
[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
Count 'A' in the said list:
3
Count 'E' in the said list:
1"""
lst=[[1, 3], [5, 7], [1, 11], [1, 15, 7]]
lst1=[]
for i in lst:
    for j in i:
        lst1.append(j)

print(lst)
n=int(input("enter the u want to count the repeat elements:"))
for j in range(0,len(lst1)):
    if n in lst1:
        res=lst1.count(n)
    else:
        res="not found"
print(res)