#Write a Python program to get the difference between the two lists.
lst1=[1,2,4,5,7,8,6,3]
lst2=[1,4,5,7,9]
lst3=set(lst1).symmetric_difference(lst2)
print(list(lst3))


