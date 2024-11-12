#Write a Python program to print the alphabet pattern 'R'.
"""
 ****
 *   *
 *   *
 ****
 * *
 *  *
 *   *
"""
for i in range(7):
    for j in range(5):
        if (i in {0,3} and j in {0,1,2,3}) or (i in {1,2,6} and j in {0,4}) or (i==4 and j in {0,2}) or (i==5 and j in {0,3}):
            print("*",end="")
        else:
            print(" ",end="")
    print()