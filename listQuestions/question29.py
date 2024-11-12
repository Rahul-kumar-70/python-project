# Write a Python program to get unique values from a list
"""lst=[1,3,5,6,8,2,4,5,6,8,9,2]
lst1=set(lst)
print(lst)
print(list(lst1))"""

 # 2nd method
lst=[1,3,5,6,8,2,4,5,6,8,9,2]
num=[]
for i in lst:
    if i not in num:
        num.append(i)
print(num)