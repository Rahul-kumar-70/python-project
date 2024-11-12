"""
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2
10 9 8 7 6 5 4 3
10 9 8 7 6 5 4
10 9 8 7 6 5
10 9 8 7 6
10 9 8 7
10 9 8
10 9
10
"""
n=int(input("enter the number of rows:"))
for i in range(n,0,-1):
    for j in range(i):
        s=str(n-j)+" "
        print(s,end="")
    print()