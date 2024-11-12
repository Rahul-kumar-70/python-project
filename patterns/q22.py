"""
J J J J J J J J J J
I I I I I I I I I
H H H H H H H H
G G G G G G G
F F F F F F
E E E E E
D D D D
C C C
B B
A
"""
n=int(input("enter the number of rows:"))
for i in range(n,-1,-1):
    for j in range(i+1):
        s=chr(65+i)+" "
        print(s,end="")
    print()

