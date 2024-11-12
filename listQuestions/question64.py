#Write a Python program to iterate over two lists simultaneously.
lst1=[1,2,3,4,5,6,7,8]
lst2=[8,7,6,5,4,3,2,1]
lst3=[]
for i in range(0,len(lst1)):
    lst3.append(lst1[i])
    for j in range(0,len(lst2)):
        if i!=j:
            continue
        else:
            lst3.append(lst2[j])
print(lst3)
