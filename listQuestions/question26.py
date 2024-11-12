# Write a python program to check whether two lists are circularly identical.
# lst1=[1,4,5,0,10,11]
# lst2=[0,10,11,1,4,5]
# lst3=[11,4,1,5,0,10]
# if len(lst1)!=len(lst2):
#     print("not circular")
# else:
#     for i in range(len(lst1)):
#         for j in range(len(lst2)):
#             if lst1[i]==lst2[j]:
#                 print(lst1.index(lst1[i]))
def are_identical(lst1, lst2, lst3):
    return set(lst1) == set(lst2) == set(lst3) and len(lst1) == len(lst2) == len(lst3)

# Test lists
lst1 = [1, 4, 5, 0, 10, 11]
lst2 = [10, 11, 1, 4, 5, 0]
lst3 = [5, 0, 1, 11, 4, 10]

# Check if they are identical
print("lst1, lst2, and lst3 are identical (ignoring order):", are_identical(lst1, lst2, lst3))


