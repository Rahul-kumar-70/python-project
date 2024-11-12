"""A chocolate factory is packing chocolates into the packets. The chocolate packets here represent an array of N number of
integer values. The task is to find the empty packets(0) of chocolate and push it to the end of the conveyor belt(array).
Example 1:
N=8 and arr = [4,5,0,1,9,0,5,0].
There are 3 empty packets in the given set. These 3 empty packets represented as O should be pushed towards the end of the array
Input:
8-Value of N
[4,5,0,1,9,0,5,0] - Element of arr[0] to arr[N-1], While input each element is separated by newline
Output: 45195000"""
n=int(input("enter the no of packets:"))
lst=[]
for i in range(0,n):
    c = input("enter the chocolates in packet:")
    for j in c.split():
        lst.append(int(j))
print(lst)
for k in range(0,len(lst)):
    if 0 in lst:
        lst.remove(0)
        lst.append(0)
    else:
        print("not empty packets")
print(lst)
