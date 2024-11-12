#Write a Python program to find the second largest number in a list.
lst=[2,1,3,6,7,8,9,11,12,10,13]
print("given list:",lst)
lst.sort()
print("second largest number in a given list:",lst[-2])