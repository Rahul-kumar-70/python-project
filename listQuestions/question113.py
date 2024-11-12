"""
113. Write a Python program to remove duplicate dictionary from a given list.
Original list with duplicate dictionary:
[{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
After removing duplicate dictionary of the said list:
[{'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
"""
lst=[{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
d=[]
data=[tuple(i.items())  for i in lst]
for j in data:
    for k in j:
