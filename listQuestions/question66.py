''' Write a Python program to find the list in a list of lists whose sum of elements is the highest.
	Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
	Expected Output: [10, 11, 12]'''
lst=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
max=0
t=0
for i in lst:
    sum=0
    for j in i:
        sum=sum+j
        if max<sum:
            max=sum
            t=i
print(t)
