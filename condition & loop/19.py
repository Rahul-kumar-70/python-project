# Write a Python program to print the alphabet pattern 'E'.
"""

 *****
 *
 *
 ****
 *
 *
 *****
"""
for i in range(7):
    for j in range(5):
        if (i in {0,6} and j in {0,1,2,3,4}) or (i in {1,2,4,5} and j==0) or (i==3 and j in {0,1,2,3}):
            print("*",end="")
        else:
            print(" ",end="")
    print()