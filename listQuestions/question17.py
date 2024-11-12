#Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers
#  between 1 and 30 (both included).
lst=[1,3,4,6,7,8,9,10,22,25,27,28,29,30]
lst1=[]
lst1=lst[len(lst)-6:len(lst)-1]
lst1.insert(0,lst[0])
sq=0
for i in lst1:
    sq=i**2
    print(sq,end=" ")
