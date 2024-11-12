"""
112. Write a Python program to check whether a specified list is sorted or not.
Original list:
[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
Is the said list is sorted!
True
Original list:
[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
Is the said list is sorted!
False

"""
n=eval(input("enter the lst of elemnet:"))
res=bool()
for i in range(len(n)-1):
    if n[i]<=n[i+1]:
        res=True
    else:
        res=False
print(res)




