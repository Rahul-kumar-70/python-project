"""
109. Write a Python program to rotate a given list by specified number of items to the right or left direction.
original List:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Rotate the said list in left direction by 4:
[4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
Rotate the said list in left direction by 2:
[3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
Rotate the said list in Right direction by 4:
[8, 9, 10, 1, 2, 3, 4, 5, 6]
Rotate the said list in Right direction by 2:
[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
"""
lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""print("----------------------")
print("1.left direction")
print("2.right direction")
print("3.exit")
print("----------------------")"""
"""while True:
    n=int(input("enter the option:"))
    match(n):
        case 1:
            print("Rotate the said list in left direction by:")
            no=int(input())
            for i in range(len(lst)):
                if n in lst:
                    
            
        case 2:
            print("Rotate the said list in right  direction by:")
        case _:
            break"""
n=int(input())
lst1=[]
for i in range(lst.index(n)):
    print(lst.pop(lst[0]))
    #print(a)
    #lst.append(a)
print(lst)
