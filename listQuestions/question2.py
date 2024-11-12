#Write a Python program to multiply all the items in a list.
lst=[1,2,3,4,5,6,7,8,9,10]
mul=1
for i in lst:
    mul*=i
print("Multiply of ({}) is {}".format(lst,mul))