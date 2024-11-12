#Write a Python program to get the smallest number from a list.
"""lst=[10,20,30,2,4,5,6,-1,-10]
min=0
for i in lst:
    if min>=i:
        min=i
        continue
print("smallest number in lst:",min)"""

#2nd method
"""lst=[10,20,30,2,4,5,6,-1,-10]
lst.sort()
print(lst[0])"""
lst=[10,20,30,2,4,5,6,-1,-10]
print(min(lst))