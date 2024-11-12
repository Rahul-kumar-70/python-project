"""Write a Python program to count the number of unique sublists within a given list.
Original list:
[[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
Number of unique lists of the said list:
{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
Original list:
[['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
Number of unique lists of the said list:
{('green', 'orange'): 2, ('black',): 1, ('white',): 1}"""
lst=[[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
d={}
for i in lst:
    t=tuple(i)
    if t not in d:
        d[t]=1
    else:
        d[t]+=1
print(d)

