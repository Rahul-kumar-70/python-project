"""Write a Python program to scramble the letters of a string in a given list.
Original list:
['Python', 'list', 'exercises', 'practice', 'solution']
After scrambling the letters of the strings of the said list:
['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']"""
import random
lst=['Python', 'list', 'exercises', 'practice', 'solution']
lst2=[]
for i in lst:
    lst1=list(i)
    random.shuffle(lst1)
    lst1=''.join(lst1)
    lst2.append(lst1)
print(lst2)


