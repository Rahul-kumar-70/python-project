#Write a Python program access the index of a list.
lst=[2,4,5,7,9,11,45,23,22]
print("="*40)
print("\tindex\tvalue")
print("="*40)
for i,j in enumerate(lst):
    print("\t",i,"--->",j)