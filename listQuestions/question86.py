"""Write a Python program to create a 3X3 grid with numbers.
3X3 grid with numbers:
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]"""
lst=[]
for i in range(0,3):
    lst1=list()*i
    for j in range(1,4):
        lst1.append(j)
    lst.append(lst1)
print(lst)