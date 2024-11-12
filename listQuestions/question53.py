# Write a Python program to create a list with infinite elements.
n=int(input("enter a value how many u want:"))
lst=[]
for i in range(0,n+1):
   lst.append(i)
print(list(lst))