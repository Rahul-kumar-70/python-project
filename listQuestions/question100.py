"""Write a Python program to extract common index elements from more than one given list.
Original lists:
[1, 1, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 7]
[0, 1, 2, 3, 4, 5, 7]
Common index elements of the said lists:
[1, 7]"""
lst1=[1, 1, 3, 4, 5, 6, 7,8]
lst2=[0, 1, 2, 3, 4, 5, 7,8]
lst3=[0, 1, 2, 3, 4, 5, 7,8]
lst4=[]
for i in range(len(lst1)):
    for j in range(len(lst2)):
       for k in range(len(lst3)):
           if i==j==k and (lst1[i]==lst2[j]==lst3[k]):
               res=lst4.append(lst1[i])
print(lst4)
