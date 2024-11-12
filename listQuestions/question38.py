'''Write a Python program to change the position of every n-th value with the (n+1)th in a list.
	Sample list: [0,1,2,3,4,5]
	Expected Output: [1, 0, 3, 2, 5, 4]
'''
lst=[0,1,2,3,4,5]
lst1=[]
for i in range(1,len(lst),2):
    for j in range(0,len(lst),2):
        if len(str(j))==1:
            lst1.append(j)
